import numpy as np
import scipy.stats as stats
import time


class HECODE:
    def __init__(self, param):
        # self.NPm = 12
        # self.NPmin = 40
        # self.Arate = 4
        # self.Hm = 5
        # self.F0 = 0.5
        # self.Cr0 = 0.5
        # self.lamda = 40
        # self.n0 = 2
        # self.gamma = 0.1
        self.NPm = param['NPm']
        self.NPmin = param['NPmin']
        self.Arate = param['Arate']
        self.Hm = param['Hm']
        self.F0 = param['F0']
        self.Cr0 = param['Cr0']
        self.lamda = param['lamda']
        self.n0 = param['n0']
        self.gamma = param['gamma']

        self.strategy = [
            {'mutate': self.ctb_w_arc, 'crossover': self.binomial},
            {'mutate': self.ctb_w_arc, 'crossover': self.exponential},
            {'mutate': self.rand1, 'crossover': self.binomial},
            {'mutate': self.rand1, 'crossover': self.exponential},
        ]

    def ctb_w_arc(self, group, all, xb, Fs):
        NP, dim = group.shape
        Arch = np.array(self.Arch)
        NA = Arch.shape[0]
        NALL = all.shape[0]

        r1 = np.random.randint(NALL, size=NP)
        r2 = np.random.randint(NALL + NA, size=NP)

        x1 = all[r1]
        if NA > 0:
            x2 = np.concatenate((all, Arch), 0)[r2]
        else:
            x2 = all[r2]
        v = group + Fs * (xb - group) + Fs * (x1 - x2)

        return v

    def rand1(self, group, all, best, Fs):
        NP = group.shape[0]
        NALL = all.shape[0]

        r1 = np.random.randint(NALL, size=NP)
        r2 = np.random.randint(NALL, size=NP)
        r3 = np.random.randint(NALL, size=NP)

        x1 = all[r1]
        x2 = all[r2]
        x3 = all[r3]
        trail = x1 + Fs * (x2 - x3)

        return trail

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

    def init(self, problem):
        dim = problem.dim

        self.NPmax = int(np.round(self.NPm * dim))
        self.NPmax = max(self.NPmax, self.NPmin)
        self.NA = self.Arate * self.NPmax
        self.NM = self.Hm * dim
        self.pointer = 0

        self.MF = np.ones(self.NM) * self.F0
        self.MCr = np.ones(self.NM) * self.Cr0
        self.Arch = []
        self.q_strategy = np.ones(4) * self.n0

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

    def update_archive(self, new_one):
        if len(self.Arch) < self.NA:
            self.Arch.append(new_one)
        else:
            idx = np.random.randint(self.NA)
            self.Arch[idx] = new_one

    def get_fv(self, problem, x):
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = np.zeros(x.shape[0])
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(np.abs(gs), -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v
    
    def prune(self, population, cost, cost_f, cost_v, nsize):
        order = np.argsort(cost)
        population = population[order]
        cost = cost[order]
        population = population[:nsize]
        cost = cost[:nsize]
        cost_f = cost_f[:nsize]
        cost_v = cost_v[:nsize]

        self.NA = int(np.round(self.Arate * nsize))
        while len(self.Arch) > self.NA:
            idx = np.random.randint(len(self.Arch))
            del self.Arch[idx]

        return population, cost, cost_f, cost_v
    
    def bound(self, population):
        population[population < 0] = np.minimum(1, 2 * 0 - population[population < 0])
        population[population > 1] = np.maximum(0, 2 * 1 - population[population > 1])
        return population
    
    def strategy_opt(self, strategy, lamda_pop, population, cost, F, Cr):
        mutate = strategy['mutate']
        crossover = strategy['crossover']
        NP, dim = population.shape        
        Fs = F.repeat(dim).reshape(NP, dim)
        Crs = Cr.repeat(dim).reshape(NP, dim)
        xb = lamda_pop[np.argmin(cost)]
        v = mutate(population, lamda_pop, xb, Fs)
        v = self.bound(v)
        u = crossover(population, v, Crs)
        return u

    def get_w(self, FEs, maxFEs, lamda):
        wi = (np.arange(lamda) + 1) / self.lamda
        wt = FEs / maxFEs
        w1 = wi * wt
        w2 = w1 + self.gamma
        w3 = (1 - wi) * (1 - wt)
        return w1, w2, w3

    def find_FR_best(self, cost_f, cost_v):
        if (cost_v == 0).sum() < 1:  # all violate
            return np.argmin(cost_v)
        else:
            cost_f[cost_v > 0] = np.max(cost_f)+1e15
            return np.argmin(cost_f)

    def evaluate(self, problem, x, FEs):
        cost_f, cost_v = self.get_fv(problem, x)
        best_index = self.find_FR_best(cost_f, cost_v)
        cost_e = np.fabs(cost_f - cost_f[best_index])
        w1, w2, w3 = self.get_w(FEs, problem.maxFEs, x.shape[0])
        cost = w1 * (cost_e - np.min(cost_e)) / (np.max(cost_e) - np.min(cost_e)) + \
               w2 * (cost_v - np.min(cost_v)) / (np.max(cost_v) - np.min(cost_v)) + \
               w3 * (cost_f - np.min(cost_f)) / (np.max(cost_f) - np.min(cost_f))
        return cost_f, cost_v, cost_e, cost

    def check(self, problem, x):
        x = (x - 0) / (1 - 0)
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = 0
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v, gs, hs
    
    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)

        NP = self.NPmax
        dim = problem.dim
        FEs = 0

        population = np.random.rand(NP, dim) * (1 - 0) + 0
        cost_f, cost_v, cost_e, cost = self.evaluate(problem, population, FEs)
        
        best_index = self.find_FR_best(cost_f, cost_v)
        gbest = [cost_f[best_index], cost_v[best_index]]
        gbest_solution = population[best_index]
        FEs = NP
        while FEs < problem.maxFEs:
            lamda_idx = np.random.choice(np.arange(NP), size=self.lamda, replace=False)
            lamda_pop = population[lamda_idx]
            lamda_cost = cost[lamda_idx]
            lamda_f, lamda_v = cost_f[lamda_idx], cost_v[lamda_idx]

            op_indiv_index = np.random.choice(4, size=self.lamda, p=self.q_strategy/np.sum(self.q_strategy))
            Cr, F = self.choose_F_Cr(self.lamda)
            u = np.zeros((self.lamda, dim))
            for i in range(4):            
                if np.sum(op_indiv_index == i) < 1:
                    continue
                group_op = lamda_pop[op_indiv_index == i]
                F_op = F[op_indiv_index == i]
                Cr_op = Cr[op_indiv_index == i]
                u[op_indiv_index == i] = self.strategy_opt(self.strategy[i], lamda_pop, group_op, lamda_cost, F_op, Cr_op)
            ncost_f, ncost_v, ncost_e, ncost = self.evaluate(problem, u, FEs)
            FEs += self.lamda
            SF = F[ncost < lamda_cost]
            SCr = Cr[ncost < lamda_cost]
            df = (lamda_cost - ncost)[ncost < lamda_cost]
            self.update_M_F_Cr(SF, SCr, df)
            optim = np.where(ncost < lamda_cost)[0]
            
            for i in range(4):
                self.q_strategy[i] += np.intersect1d(optim, np.where(op_indiv_index == i)[0]).shape[0]
            lamda_pop[optim] = u[optim]
            lamda_cost = np.minimum(lamda_cost, ncost)
            lamda_f[optim] = ncost_f[optim]
            lamda_v[optim] = ncost_v[optim]
            
            population[lamda_idx] = lamda_pop
            cost[lamda_idx] = lamda_cost
            cost_f[lamda_idx] = lamda_f
            cost_v[lamda_idx] = lamda_v

            best_index = self.find_FR_best(cost_f, cost_v)
            if cost_v[best_index] < gbest[1] or (cost_v[best_index] == gbest[1] and cost_f[best_index] < gbest[0]):
                gbest = [cost_f[best_index], cost_v[best_index]]
                gbest_solution = population[best_index]
            # Prune population
            NP = max(self.NPmin, self.NPmax - int(np.round((self.NPmax - self.NPmin) * FEs / problem.maxFEs)))
            population, cost, cost_f, cost_v = self.prune(population, cost, cost_f, cost_v,NP)
            f, _, gs, hs = self.check(problem, gbest_solution)
        ed_time = time.time()
        return {'x': gbest_solution * (problem.ub - problem.lb) + problem.lb, 'fun': gbest[0], 'maxcv': gbest[1], 'runtime': ed_time - st_time, 'nfev': FEs}

