import numpy as np
import scipy.stats as stats


class MadDEtool:
    def __init__(self):
        pass

    def init(self, problem):
        dim = problem.dim
        self.NPmax = int(np.round(self.NPm * dim * dim))
        self.NPmax = max(self.NPmax, self.NPmin)
        self.NA = self.Arate * self.NPmax
        self.NM = self.Hm * dim
        self.pointer = 0
        self.pm = np.ones(3) / 3
        self.MF = np.ones(self.NM) * self.F0
        self.MCr = np.ones(self.NM) * self.Cr0
        self.Arch = []
        self.Arch_cost = []
    
    def init_population(self, NP, problem):
        dim = problem.dim
        population = np.random.rand(NP, dim)
        cost = self.evaluate(problem, population)
        gbest = np.min(cost)
        gbest_solution = population[np.argmin(cost)]
        return population, cost, gbest_solution, gbest

    def ctb_w_arc(self, group, best, archive, Fs):
        NP, dim = group.shape
        NB = best.shape[0]
        NA = archive.shape[0]

        count = 0
        rb = np.random.randint(NB, size=NP)
        duplicate = np.where(rb == np.arange(NP))[0]
        while duplicate.shape[0] > 0 and count < 25:
            rb[duplicate] = np.random.randint(NB, size=duplicate.shape[0])
            duplicate = np.where(rb == np.arange(NP))[0]
            count += 1

        count = 0
        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where((r1 == rb) + (r1 == np.arange(NP)))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r1 == rb) + (r1 == np.arange(NP)))[0]
            count += 1

        count = 0
        r2 = np.random.randint(NP + NA, size=NP)
        duplicate = np.where((r2 == rb) + (r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r2[duplicate] = np.random.randint(NP + NA, size=duplicate.shape[0])
            duplicate = np.where((r2 == rb) + (r2 == np.arange(NP)) + (r2 == r1))[0]
            count += 1

        xb = best[rb]
        x1 = group[r1]
        if NA > 0:
            x2 = np.concatenate((group, archive), 0)[r2]
        else:
            x2 = group[r2]
        v = group + Fs * (xb - group) + Fs * (x1 - x2)

        return v

    def ctr_w_arc(self, group, archive, Fs):
        NP, dim = group.shape
        NA = archive.shape[0]

        count = 0
        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where((r1 == np.arange(NP)))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r1 == np.arange(NP)))[0]
            count += 1

        count = 0
        r2 = np.random.randint(NP + NA, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r2[duplicate] = np.random.randint(NP + NA, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
            count += 1

        x1 = group[r1]
        if NA > 0:
            x2 = np.concatenate((group, archive), 0)[r2]
        else:
            x2 = group[r2]
        v = group + Fs * (x1 - x2)

        return v

    def weighted_rtb(self, group, best, Fs, Fas):
        NP, dim = group.shape
        NB = best.shape[0]

        count = 0
        rb = np.random.randint(NB, size=NP)
        duplicate = np.where(rb == np.arange(NP))[0]
        while duplicate.shape[0] > 0 and count < 25:
            rb[duplicate] = np.random.randint(NB, size=duplicate.shape[0])
            duplicate = np.where(rb == np.arange(NP))[0]
            count += 1

        count = 0
        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where((r1 == rb) + (r1 == np.arange(NP)))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r1 == rb) + (r1 == np.arange(NP)))[0]
            count += 1

        count = 0
        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == rb) + (r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0 and count < 25:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == rb) + (r2 == np.arange(NP)) + (r2 == r1))[0]
            count += 1

        xb = best[rb]
        x1 = group[r1]
        x2 = group[r2]
        v = Fs * x1 + Fs * Fas * (xb - x2)

        return v

    def binomial(self, x, v, Crs):
        NP, dim = x.shape
        jrand = np.random.randint(dim, size=NP)
        u = np.where(np.random.rand(NP, dim) < Crs, v, x)
        u[np.arange(NP), jrand] = v[np.arange(NP), jrand]
        return u
    
    def mean_wL(self, df, s):
        w = df / np.sum(df)
        if np.sum(w * s) > 0.000001:
            return np.sum(w * (s ** 2)) / np.sum(w * s)
        else:
            return 0.5

    # randomly choose step length nad crossover rate from MF and MCr
    def choose_F_Cr(self, size):
        # generate Cr can be done simutaneously
        ind_r = np.random.randint(0, self.MF.shape[0], size=size)  # index
        C_r = np.minimum(1, np.maximum(0, np.random.normal(loc=self.MCr[ind_r], scale=0.1, size=size)))
        # as for F, need to generate 1 by 1
        cauchy_locs = self.MF[ind_r]
        F = stats.cauchy.rvs(loc=cauchy_locs, scale=0.1, size=size)
        err = np.where(F < 0)[0]
        F[err] = 2 * cauchy_locs[err] - F[err]
        return C_r, np.minimum(1, F)

    # update MF and MCr, join new value into the set if there are some successful changes or set it to initial value
    def update_M_F_Cr(self, SF, SCr, df):
        if SF.shape[0] > 0:
            mean_wL = self.mean_wL(df, SF)
            self.MF[self.pointer] = mean_wL
            mean_wL = self.mean_wL(df, SCr)
            self.MCr[self.pointer] = mean_wL
            self.pointer = (self.pointer + 1) % self.NM
        else:
            self.MF[self.pointer] = 0.5
            self.MCr[self.pointer] = 0.5

    def update_archive(self, new_one, cost):
        if len(self.Arch) < self.NA:
            self.Arch.append(new_one)
            self.Arch_cost.append(cost)
        else:
            idx = np.random.randint(self.NA)
            self.Arch[idx] = new_one
            self.Arch_cost[idx] = cost

    def evaluate(self, problem, x):
        x = x * (problem.ub - problem.lb) + problem.lb
        return problem.eval(x)
    
    def prune(self, population, cost, nsize):
        order = np.argsort(cost)
        population = population[order]
        cost = cost[order]
        population = population[:nsize]
        cost = cost[:nsize]

        self.NA = int(np.round(self.Arate * nsize))
        if len(self.Arch) > self.NA:
            order = np.argsort(self.Arch_cost)
            rm_idx = order[-(len(self.Arch) - self.NA):]
            rm_idx = np.sort(rm_idx)[::-1]
            for idx in rm_idx:
                del self.Arch[idx]
                del self.Arch_cost[idx]

        return population, cost
        
    def three_mutates(self, population, archive, mu, F, q, Fa):
        NP, dim = population.shape
        p1 = population[mu == 0]
        p2 = population[mu == 1]
        p3 = population[mu == 2]
        pbest = population[:max(int(self.p * NP), 2)]
        qbest = population[:max(int(q * NP), 2)]
        Fs = F.repeat(dim).reshape(NP, dim)
        v1 = self.ctb_w_arc(p1, pbest, archive, Fs[mu == 0])
        v2 = self.ctr_w_arc(p2, archive, Fs[mu == 1])
        v3 = self.weighted_rtb(p3, qbest, Fs[mu == 2], Fa)
        v = np.zeros((NP, dim))
        v[mu == 0] = v1
        v[mu == 1] = v2
        v[mu == 2] = v3
        v[v < 0] = (population[v < 0] + 0) / 2
        v[v > 1] = (population[v > 1] + 1) / 2
        return v