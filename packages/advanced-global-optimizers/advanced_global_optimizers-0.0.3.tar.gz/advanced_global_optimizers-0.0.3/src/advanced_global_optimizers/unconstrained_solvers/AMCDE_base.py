import numpy as np
import scipy
import scipy.stats as stats


class AMCDEtool:
    def __init__(self) -> None:
        pass

    def ctb_wo_arc(self, group, best, F):
        NP, dim = group.shape
        NB = best.shape[0]
        Fs = F.repeat(dim).reshape(NP, dim)

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
        v = group + Fs * (xb - group) + Fs * (x1 - x2)

        return v

    def ctb_w_arc(self, group, best, F):
        NP, dim = group.shape
        Arch = np.array(self.Arch)
        NB = best.shape[0]
        NA = Arch.shape[0]
        Fs = F.repeat(dim).reshape(NP, dim)

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
            x2 = np.concatenate((group, Arch), 0)[r2]
        else:
            x2 = group[r2]
        v = group + Fs * (xb - group) + Fs * (x1 - x2)

        return v

    def weighted_rtb(self, group, best, F):
        NP, dim = group.shape
        NB = best.shape[0]
        Fs = F.repeat(dim).reshape(NP, dim)

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
        v = Fs * x1 + Fs * (xb - x2)

        return v

    def binomial(self, x, v, Crs):
        NP, dim = x.shape
        jrand = np.random.randint(dim, size=NP)
        u = np.where(np.random.rand(NP, dim) < Crs, v, x)
        u[np.arange(NP), jrand] = v[np.arange(NP), jrand]
        return u

    def exponential(self, x, v, Crs):
        NP, dim = x.shape
        u = x.copy()
        L = np.random.randint(dim, size=NP).repeat(dim).reshape(NP, dim)
        L = L <= np.arange(dim)
        rvs = np.random.rand(NP, dim)
        L = np.where(rvs > Crs, L, 0)
        u = u * (1 - L) + v * L
        return u
    
    def mean_wL(self, df, s):
        w = df / np.sum(df)
        if np.sum(w * s) > 0.000001:
            return np.sum(w * (s ** 2)) / np.sum(w * s)
        else:
            return 0.5

    # randomly choose step length nad crossover rate from MF and MCr
    def choose_F(self, size):
        # generate Cr can be done simutaneously
        ind_r = np.random.randint(0, self.MF.shape[0], size=size)  # index
        # as for F, need to generate 1 by 1
        cauchy_locs = self.MF[ind_r]
        F = stats.cauchy.rvs(loc=cauchy_locs, scale=0.1, size=size)
        err = np.where(F < 0)[0]
        F[err] = 2 * cauchy_locs[err] - F[err]
        return np.minimum(1, F)

    # update MF and MCr, join new value into the set if there are some successful changes or set it to initial value
    def update_MF(self, SF, df):
        if SF.shape[0] > 0:
            mean_wL = self.mean_wL(df, SF)
            self.MF[self.pointer] = mean_wL
        else:
            self.MF[self.pointer] = 0.5

    def update_archive(self, new_one):
        if len(self.Arch) < self.NA:
            self.Arch.append(new_one)
        else:
            idx = np.random.randint(self.NA)
            self.Arch[idx] = new_one

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
        while len(self.Arch) > self.NA:
            idx = np.random.randint(len(self.Arch))
            del self.Arch[idx]

        return population, cost
    
    def SLSQP_local_search(self, problem, gbest_solution, gbest):
        def sqp_eval(x):
            return self.evaluate(problem, x)
        res = scipy.optimize.minimize(sqp_eval, gbest_solution, method='SLSQP', options={"maxiter": 1})
        if res.fun < gbest:
            gbest_solution = res.x
            gbest = res.fun
            # population[np.argmin(cost)] = gbest_solution
            # cost[np.argmin(cost)] = gbest
        else:
            self.pls = self.pls_fail
        # FEs += res.nfev
        return gbest_solution, gbest, res.nfev
    
    def tri_mutate(self, population, op_indiv_index, F):
        NP, dim = population.shape
        PB12 = max(int(0.25 * NP), 2)
        PB3 = max(int(0.5 * NP), 1)
        best_op12 = population[:PB12]
        best_op3 = population[:PB3]
        group_op1 = population[op_indiv_index == 0]
        group_op2 = population[op_indiv_index == 1]
        group_op3 = population[op_indiv_index == 2]
        # Fs = F.repeat(dim).reshape(NP, dim)
        v1 = self.ctb_wo_arc(group_op1, best_op12, F[op_indiv_index == 0])
        v2 = self.ctb_w_arc(group_op2, best_op12, F[op_indiv_index == 1])
        v3 = self.weighted_rtb(group_op3, best_op3, F[op_indiv_index == 2])
        v = np.zeros((NP, dim))
        v[op_indiv_index == 0] = v1
        v[op_indiv_index == 1] = v2
        v[op_indiv_index == 2] = v3
        return v
    
    def init_population(self, NP, problem):
        dim = problem.dim
        population = np.random.rand(NP, dim)
        cost = self.evaluate(problem, population)
        gbest = np.min(cost)
        gbest_solution = population[np.argmin(cost)]
        return population, cost, gbest_solution, gbest
    
    def crossover(self, v, population, Crs):
        NP, dim = population.shape
        rnd = np.random.rand(NP)
        u = np.zeros((NP, dim))
        be_rate = self.pbc1
        u[rnd < be_rate] = self.exponential(population[rnd < be_rate], v[rnd < be_rate], Crs)
        u[rnd >= be_rate] = self.binomial(population[rnd >= be_rate], v[rnd >= be_rate], Crs)
        u = np.clip(u, 0, 1)
        return u
    
    def update_win_rec(self, cost, ncost, op_indiv_index):
        df_op = np.zeros(3)
        for i in range(3):
            df = (cost - ncost)[op_indiv_index == i]
            if df.shape[0] > 0:
                df_op[i] = np.sum(np.maximum(0, df)) / df.shape[0]
        last_win = np.argmax(df_op)
        last_chosen = np.where(op_indiv_index == last_win)[0]
        return last_win, last_chosen

