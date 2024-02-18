import numpy as np
class DEtool:
    def __init__(self) -> None:
        pass

    def evaluate(self, x, problem):
        x = x * (problem.ub - problem.lb) + problem.lb
        cost = problem.eval(x)
        # cost[cost < self.terminateErrorValue] = 0.0
        return cost

    def best1(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        x1 = population[r1]
        x2 = population[r2]
        trail = gbest_solution + Fs * (x1 - x2)

        return trail

    def best2(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        r3 = np.random.randint(NP, size=NP)
        duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]
        while duplicate.shape[0] > 0:
            r3[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]

        r4 = np.random.randint(NP, size=NP)
        duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]
        while duplicate.shape[0] > 0:
            r4[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]

        x1 = population[r1]
        x2 = population[r2]
        x3 = population[r3]
        x4 = population[r4]
        trail = gbest_solution + Fs * (x1 - x2) + Fs * (x3 - x4)

        return trail

    def rand2(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        r3 = np.random.randint(NP, size=NP)
        duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]
        while duplicate.shape[0] > 0:
            r3[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]

        r4 = np.random.randint(NP, size=NP)
        duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]
        while duplicate.shape[0] > 0:
            r4[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]

        r5 = np.random.randint(NP, size=NP)
        duplicate = np.where((r5 == np.arange(NP)) + (r5 == r1) + (r5 == r2) + (r5 == r3) + (r5 == r4))[0]
        while duplicate.shape[0] > 0:
            r5[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r5 == np.arange(NP)) + (r5 == r1) + (r5 == r2) + (r5 == r3) + (r5 == r4))[0]

        x1 = population[r1]
        x2 = population[r2]
        x3 = population[r3]
        x4 = population[r4]
        x5 = population[r5]
        trail = x5 + Fs * (x1 - x2) + Fs * (x3 - x4)

        return trail

    def current2rand(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        r3 = np.random.randint(NP, size=NP)
        duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]
        while duplicate.shape[0] > 0:
            r3[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]

        x1 = population[r1]
        x2 = population[r2]
        x3 = population[r3]
        trail = population + Fs * (x1 - population) + Fs * (x2 - x3)

        return trail

    def current2best(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        x1 = population[r1]
        x2 = population[r2]
        trail = population + Fs * (gbest_solution - population) + Fs * (x1 - x2)

        return trail

    def rand2best2(self, population, gbest_solution, Fs):
        NP = population.shape[0]

        r1 = np.random.randint(NP, size=NP)
        duplicate = np.where(r1 == np.arange(NP))[0]
        while duplicate.shape[0] > 0:
            r1[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where(r1 == np.arange(NP))[0]

        r2 = np.random.randint(NP, size=NP)
        duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]
        while duplicate.shape[0] > 0:
            r2[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r2 == np.arange(NP)) + (r2 == r1))[0]

        r3 = np.random.randint(NP, size=NP)
        duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]
        while duplicate.shape[0] > 0:
            r3[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r3 == np.arange(NP)) + (r3 == r1) + (r3 == r2))[0]

        r4 = np.random.randint(NP, size=NP)
        duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]
        while duplicate.shape[0] > 0:
            r4[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r4 == np.arange(NP)) + (r4 == r1) + (r4 == r2) + (r4 == r3))[0]

        r5 = np.random.randint(NP, size=NP)
        duplicate = np.where((r5 == np.arange(NP)) + (r5 == r1) + (r5 == r2) + (r5 == r3) + (r5 == r4))[0]
        while duplicate.shape[0] > 0:
            r5[duplicate] = np.random.randint(NP, size=duplicate.shape[0])
            duplicate = np.where((r5 == np.arange(NP)) + (r5 == r1) + (r5 == r2) + (r5 == r3) + (r5 == r4))[0]

        x1 = population[r1]
        x2 = population[r2]
        x3 = population[r3]
        x4 = population[r4]
        x5 = population[r5]
        trail = x5 + Fs * (gbest_solution - population) + Fs * (x1 - x2) + Fs * (x3 - x4)

        return trail

    def binomial(self, population, trail, Crs):
        NP, dim = population.shape
        jrand = np.random.randint(dim, size=NP)
        u = np.where(np.random.rand(NP, dim) < Crs, trail, population)
        u[np.arange(NP), jrand] = trail[np.arange(NP), jrand]
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
    
    def bound(self, population, type="clip"):
        norm_ub, norm_lb = 1, 0
        if type == "periodic":
            while np.max(population) > norm_ub or np.min(population) < norm_lb:
                population[population > norm_ub] += - norm_ub + norm_lb
                population[population < norm_lb] += - norm_lb + norm_ub
            return population
        elif type == "reflect":
            while np.max(population) > norm_ub or np.min(population) < norm_lb:
                population[population > norm_ub] = 2*norm_ub - population[population > norm_ub]
                population[population < norm_lb] = 2*norm_lb - population[population < norm_lb]
            return population
        elif type == "rand":
            tmp = np.random.rand(population.shape[0], population.shape[1]) * (norm_ub - norm_lb) + norm_lb
            population[population < norm_lb] = tmp[population < norm_lb]
            population[population > norm_ub] = tmp[population > norm_ub]
            return population
        else:  # clip
            return np.clip(population, norm_lb, norm_ub)

