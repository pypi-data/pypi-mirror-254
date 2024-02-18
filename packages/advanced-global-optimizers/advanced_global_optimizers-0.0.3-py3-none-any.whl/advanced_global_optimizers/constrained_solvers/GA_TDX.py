import numpy as np
import time

class GA_TDX:
    def __init__(self, param):
        # self.beta = 0.2
        # self.gamma = 6
        self.m = 1e10 # penalty term
        self.beta = param['beta']
        self.gamma = param['gamma']
        self.NP = param['NP']

    def check_violate(self, problem, x):
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = 0
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v, gs, hs

    def check(self, problem, x):
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = 0
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v, gs, hs

    def evaluate(self, population, problem):
        x = population * (problem.ub - problem.lb) + problem.lb
        cost = problem.eval(x)
        penalty = np.zeros(population.shape[0])
        v = np.zeros(population.shape[0])
        gs = np.maximum(0, problem.g_constrain(x))
        penalty += self.m * np.sum(np.square(gs), -1)
        v += np.sum(gs, -1)
        hs = np.abs(problem.h_constrain(x))
        penalty += self.m * np.sum(np.square(hs), -1)
        v += np.sum(hs, -1)
        self.FEs += population.shape[0]
        penalized_cost = cost + penalty

        pc = cost.copy()
        pc[v > 0] = 1e15 + v[v > 0]
        best_id = np.argmin(pc)
        if v[best_id] < self.gbest[1] or (v[best_id] == self.gbest[1] and cost[best_id] < self.gbest[0]):
            self.gbest = [cost[best_id], v[best_id]]
            self.gbest_solution = population[best_id]

        return penalized_cost

    def select_for_next_generation(self, parents, parents_cost, offsprings, offsprings_cost):
        next_generation = np.zeros_like(parents)
        next_generation_cost = np.zeros_like(parents_cost)
        for idx in range(parents.shape[0]):
            if parents_cost[idx] < offsprings_cost[idx]:
                next_generation[idx] = parents[idx]
                next_generation_cost[idx] = parents_cost[idx]
            else:
                next_generation[idx] = offsprings[idx]
                next_generation_cost[idx] = offsprings_cost[idx]
        return next_generation, next_generation_cost

    def get_sorted_population(self, population, cost):
        idx = np.argsort(cost,axis=-1)
        return population[idx], cost[idx]

    def tdx(self, x1, x2, mean_xn, problem):
        dim = problem.dim
        d1 = x1 - x2
        dp = np.random.rand(dim)
        if d1[-1] == 0:
            dp[-1] = np.sum(d1[:dim - 1] * dp[:dim - 1]) / (-mean_xn + 2 * mean_xn * np.random.rand())
        else:
            dp[-1] = np.sum(d1[:dim - 1] * dp[:dim - 1]) / d1[-1]
        dp = (np.linalg.norm(d1)) / (np.linalg.norm(dp)) * dp
        d2 = (d1 + dp) / 2
        alpha = np.random.rand()
        o1 = x1 + alpha * d1
        o2 = x1 + alpha * d2
        o3 = x2 + alpha * d1
        o4 = x2 + alpha * d2
        cost = self.evaluate(np.vstack([o1, o2, o3, o4]), problem)
        offspring = []
        offspring_cost = []
        if cost[0] < cost[1]:
            offspring.append(o1)
            offspring_cost.append(cost[0])
        else:
            offspring.append(o2)
            offspring_cost.append(cost[1])
        if cost[2] < cost[3]:
            offspring.append(o3)
            offspring_cost.append(cost[2])
        else:
            offspring.append(o4)
            offspring_cost.append(cost[3])
        return offspring, offspring_cost

    def normal_mutation(self, population):
        steps = np.random.rand(*population.shape)
        return population + steps * np.abs(population[0] - population[-1]) / 6

    def nonuniform_mutation(self, population, lb, ub):
        r = np.random.rand(*population.shape)
        decay = 1 - np.power(r, np.power(1-self.FEs/ self.maxFEs,self.gamma))
        return np.where(r <= 0.5, (ub - population) * decay, (lb - population) * decay)

    def gm(self, population, population_cost, problem):
        x_sorted, _ = self.get_sorted_population(population, population_cost)
        x_better = x_sorted[:round(self.beta * self.NP)]
        x_worse = x_sorted[round(self.beta * self.NP):]
        o_better = self.normal_mutation(x_better)
        o_worse = self.nonuniform_mutation(x_worse, 0, 1)
        offspring = np.concatenate([o_better,o_worse])
        offspring_cost = self.evaluate(offspring, problem)
        return offspring, offspring_cost

    def init(self, problem):
        self.FEs = 0
        self.maxFEs = problem.maxFEs
        if (self.NP % 2) != 0:
            self.NP += 1
        self.gbest = [np.inf, np.inf]
        self.gbest_solution = None

    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)
        population = np.random.rand(self.NP, problem.dim)
        population_cost = self.evaluate(population, problem)
        while self.FEs < self.maxFEs:
            # execute TDX corssover
            sorted_population, sorted_population_cost = self.get_sorted_population(population, population_cost) # sorting grouping selection
            X1 = sorted_population[:self.NP // 2]
            X2 = sorted_population[self.NP // 2:]
            offspring = []
            offspring_cost = []
            for i in range(self.NP // 2):
                o,c = self.tdx(X1[i], X2[i], np.mean(sorted_population[:,-1]), problem)
                offspring.append(o)
                offspring_cost.append(c)
            offspring = np.concatenate(offspring)
            offspring_cost = np.concatenate(offspring_cost)
            selected_population, selected_population_cost = self.select_for_next_generation(sorted_population,
                                                                                       sorted_population_cost,
                                                                                       offspring,
                                                                                       offspring_cost)
            # execute Grouped Mutation
            mutated_population, mutated_population_cost = self.gm(selected_population,selected_population_cost,problem)
            population, population_cost = self.select_for_next_generation(selected_population,
                                                                          selected_population_cost,
                                                                          mutated_population,
                                                                          mutated_population_cost)
            # print('best:{}'.format(np.min(population_cost)))
            f, v, gs, hs = self.check(problem, self.gbest_solution)

        ed_time = time.time()
        return {'x': self.gbest_solution * (problem.ub - problem.lb) + problem.lb, 'fun': self.gbest[0], 'maxcv': self.gbest[1], 'runtime': ed_time - st_time, 'nfev': self.FEs}


