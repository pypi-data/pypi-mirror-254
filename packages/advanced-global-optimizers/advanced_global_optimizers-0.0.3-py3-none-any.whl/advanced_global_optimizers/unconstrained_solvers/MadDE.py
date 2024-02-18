import numpy as np
from .MadDE_base import MadDEtool
import time


class MadDE(MadDEtool):
    def __init__(self, param):
        super().__init__()
        # self.p = 0.18
        # self.PqBX = 0.01
        # self.F0 = 0.2
        # self.Cr0 = 0.2
        # self.Arate = 2.3
        # self.NPm = 2
        # self.Hm = 10
        # self.NPmin = 4
        self.p = param['p']
        self.PqBX = param['PqBX']
        self.F0 = param['F0']
        self.Cr0 = param['Cr0']
        self.Arate = param['Arate']
        self.Hm = param['Hm']
        self.NPm = param['NPm']
        self.NPmin = param['NPmin']

    
    def init(self, problem, ):
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
        
    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)

        dim = problem.dim
        NP = self.NPmax
        population = np.random.rand(NP, dim)
        cost = self.evaluate(problem, population)
        gbest = np.min(cost)
        gbest_solution = population[np.argmin(cost)]
        FEs = NP
        maxFEs = problem.maxFEs
        while FEs < maxFEs:
            q = 2 * self.p - self.p * FEs / maxFEs
            Fa = 0.5 + 0.5 * FEs / maxFEs
            Cr, F = self.choose_F_Cr(NP)
            archive = np.array(self.Arch)
            mu = np.random.choice(3, size=NP, p=self.pm)
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
            rvs = np.random.rand(NP)
            Crs = Cr.repeat(dim).reshape(NP, dim)
            u = np.zeros((NP, dim))
            if np.sum(rvs <= self.PqBX) > 0:
                qu = v[rvs <= self.PqBX]
                if archive.shape[0] > 0:
                    qbest = np.concatenate((population, archive), 0)[:max(int(q * (NP + archive.shape[0])), 2)]
                cross_qbest = qbest[np.random.randint(qbest.shape[0], size=qu.shape[0])]
                qu = self.binomial(cross_qbest, qu, Crs[rvs <= self.PqBX])
                u[rvs <= self.PqBX] = qu
            bu = v[rvs > self.PqBX]
            bu = self.binomial(population[rvs > self.PqBX], bu, Crs[rvs > self.PqBX])
            u[rvs > self.PqBX] = bu

            ncost = self.evaluate(problem, u)
            FEs += NP

            optim = np.where(ncost < cost)[0]
            for i in optim:
                self.update_archive(population[i], cost[i])
            SF = F[optim]
            SCr = Cr[optim]
            df = np.maximum(0, cost - ncost)
            self.update_M_F_Cr(SF, SCr, df[optim])
            count_S = np.zeros(3)
            for i in range(3):
                count_S[i] = np.mean(df[mu == i] / cost[mu == i])
            if np.sum(count_S) > 0:
                self.pm = np.maximum(0.1, np.minimum(0.9, count_S / np.sum(count_S)))
                self.pm /= np.sum(self.pm)
            else:
                self.pm = np.ones(3) / 3

            population[optim] = u[optim]
            cost = np.minimum(cost, ncost)

            if np.min(cost) < gbest:
                gbest = np.min(cost)
                gbest_solution = population[np.argmin(cost)]

            # Prune population
            NP = max(self.NPmax - int(np.round((self.NPmax - self.NPmin) * FEs / problem.maxFEs)), self.NPmin)
            population, cost = self.prune(population, cost, NP)

        ed_time = time.time()
        return {'x': gbest_solution * (problem.ub - problem.lb) + problem.lb, 'fun': gbest, 'runtime': ed_time - st_time, 'nfev': FEs}
