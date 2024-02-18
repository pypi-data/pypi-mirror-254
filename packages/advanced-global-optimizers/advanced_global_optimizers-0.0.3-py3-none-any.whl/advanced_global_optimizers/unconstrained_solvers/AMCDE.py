import numpy as np
import time
from .AMCDE_base import AMCDEtool


class AMCDE(AMCDEtool):
    def __init__(self, param):
        # self.Gn = 5
        # self.pbc1 = 0.4
        # self.pbc2 = 0.4
        # self.pw = 0.2
        # self.pr = 0.01
        # self.NPm = 6
        # self.NPmin = 4
        # self.Arate = 2.6
        # self.Hm = 20
        # self.pls_succ = 0.1
        # self.pls_fail = 0.0001
        # self.F0 = 0.2
        self.Gn = param['Gn']
        self.pbc1 = param['pbc1']
        self.pbc2 = param['pbc2']
        self.pw = param['pw']
        self.pr = param['pr']
        self.NPm = param['NPm']
        self.NPmin = param['NPmin']
        self.Arate = param['Arate']
        self.Hm = param['Hm']
        self.pls_succ = param['pls_succ']
        self.pls_fail = param['pls_fail']
        self.F0 = param['F0']


    def init(self, problem):
        dim = problem.dim
        self.pls = self.pls_succ
        self.NPmax = int(np.round(self.NPm * dim * dim))
        self.NPmax = max(self.NPmax, self.NPmin)
        self.NA = self.Arate * self.NPmax
        self.NM = self.Hm * dim
        self.pointer = 0
        self.mutate = [self.ctb_wo_arc, self.ctb_w_arc, self.weighted_rtb]

        self.MF = np.ones(self.NM) * self.F0
        self.MCr = np.zeros(self.NM)
        self.Arch = []
        
    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)

        mutate = self.ctb_w_arc
        gn = 0
        NP = self.NPmax
        maxFEs = problem.maxFEs
        population, cost, gbest_solution, gbest = self.init_population(NP, problem)
        FEs = NP
        last_chosen, last_win = None, None
        while FEs < maxFEs:

            PB12 = max(int(0.25 * NP), 2)
            if gn < self.Gn:
                F = self.choose_F(NP)
                Crs = 0 if FEs < 0.5 * maxFEs else (FEs / maxFEs - 0.5) * 2
                v = mutate(population, population[:PB12], F)
                u = self.crossover(v, population, Crs)
                ncost = self.evaluate(problem, u)
                FEs += NP
                SF = F[ncost < cost]
                df = (cost - ncost)[ncost < cost]
                self.update_MF(SF, df)

                optim = np.where(ncost < cost)[0]
                for i in optim:
                    self.update_archive(population[i])
                population[optim] = u[optim]
                cost = np.minimum(cost, ncost)
                
                if np.min(cost) < gbest:
                    gbest = np.min(cost)
                    gbest_solution = population[np.argmin(cost)]
                    gn = 0
            else:
                # according to performance of 3 ops, randomly assign indiv
                op_indiv_index = np.random.choice(3, size=NP)
                
                if last_win is not None and last_chosen.shape[0] > 0:
                    last_chosen = last_chosen[last_chosen < NP]
                    op_indiv_index[last_chosen] = last_win

                F = self.choose_F(NP)
                v = self.tri_mutate(population, op_indiv_index, F)
                Crs = 0 if FEs < 0.5 * maxFEs else (FEs / maxFEs - 0.5) * 2
                u = self.crossover(v, population, Crs)
                ncost = self.evaluate(problem, u)
                FEs += NP
                SF = F[ncost < cost]
                df = (cost - ncost)[ncost < cost]
                self.update_MF(SF, df)
                worst = np.sort(cost)[-max(int(self.pw*NP), 1)]
                optim = np.where((ncost < cost)+(cost >= worst))[0]
                
                for i in optim:
                    if (cost[i] > worst and np.random.rand() < self.pr) or ncost[i] < cost[i]:
                        population[i] = u[i]
                        cost[i] = ncost[i]
                        self.update_archive(population[i])
                last_win, last_chosen = self.update_win_rec(cost, ncost, op_indiv_index)
            
                if np.min(cost) < gbest:
                    mutate = self.mutate[last_win]
                    gbest = np.min(cost)
                    gbest_solution = population[np.argmin(cost)]
                    gn = 0
                    self.Gn += 1
                    last_chosen = None
                    last_win = None
            gn += 1
            if FEs < maxFEs and FEs >= 0.85 * maxFEs and np.random.rand() < self.pls:
                gbest_solution, gbest, nfev = self.SLSQP_local_search(problem, gbest_solution, gbest)
                FEs += nfev
                population[np.argmin(cost)] = gbest_solution
                cost[np.argmin(cost)] = gbest
            # Prune population
            NP = max(self.NPmax - int(np.round((self.NPmax - self.NPmin) * FEs / maxFEs)), self.NPmin)
            population, cost = self.prune(population, cost, NP)
        ed_time = time.time()
        return {'x': gbest_solution * (problem.ub - problem.lb) + problem.lb, 'fun': gbest, 'runtime': ed_time - st_time, 'nfev': FEs}
    