import numpy as np
from .DE_base import DEtool
import time

class basic_DE(DEtool):
    def __init__(self, param):
        self.popsize = param['popsize']
        self.F = param['F']
        self.Cr = param['Cr']
        self.mutation = param['mutation']
        self.bounds = param['bound']

    def optimize(self,
                    problem,
                    ):
        # Initialize population
        st_time = time.time()
        dim = problem.dim
        NP = self.popsize
        population = np.random.rand(NP, dim)
        cost = self.evaluate(population, problem)
        gbest = np.min(cost)
        gbest_solution = population[np.argmin(cost)]
        FEs = NP
        while FEs < problem.maxFEs:
            Fs = self.F
            Crs = self.Cr
            trail = eval("self."+self.mutation)(population, gbest_solution, Fs)
            trail = self.binomial(population, trail, Crs)
            trail = self.bound(trail, self.bounds)

            new_cost = self.evaluate(trail, problem)
            replace_id = np.where(new_cost < cost)[0]

            population[replace_id] = trail[replace_id]
            cost[replace_id] = new_cost[replace_id]
            FEs += NP

            if gbest > np.min(cost):
                gbest = np.min(cost)
                gbest_solution = population[np.argmin(cost)]

        ed_time = time.time()
        return {'x': gbest_solution * (problem.ub - problem.lb) + problem.lb, 'fun': gbest, 'runtime': ed_time - st_time, 'nfev': FEs}
    
