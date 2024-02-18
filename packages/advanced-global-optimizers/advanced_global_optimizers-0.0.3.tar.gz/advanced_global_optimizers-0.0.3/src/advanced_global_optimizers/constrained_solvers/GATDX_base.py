import numpy as np


class GATDXtool:
    def __init__(self) -> None:
        pass

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

