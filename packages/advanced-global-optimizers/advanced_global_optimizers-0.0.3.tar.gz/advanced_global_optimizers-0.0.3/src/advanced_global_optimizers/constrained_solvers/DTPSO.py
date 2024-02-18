import numpy as np
import time


class DTPSO:
    def __init__(self, param) -> None:
        # self.p = 0.9
        # self.sigma = 0.25
        # self.gamma = 0.5
        # self.u1 = 0.5
        # self.u2 = 0
        # self.c11 = 0
        # self.c12 = 1.711897
        # self.c21 = 1.711897
        # self.c22 = 1.711897
        # self.ws = 0.9
        # self.we = 0.4
        # self.NPinit = 50
        # self.radius = 0.1
        self.p = param['p']
        self.sigma = param['sigma']
        self.gamma = param['gamma']
        self.u1 = param['u1']
        self.u2 = param['u2']
        self.c11 = param['c11']
        self.c12 = param['c12']
        self.c21 = param['c21']
        self.c22 = param['c22']
        self.ws = param['ws']
        self.we = param['we']
        self.NPinit = param['NPinit']
        self.radius = param['radius']

    def evaluate(self, x, problem, detailed=False):
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = 0
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        if detailed:
            return f, v, gs, hs
        return f, v
    
    def evaluate_all(self, x, problem):
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = np.zeros(x.shape[0])
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v

    def init(self, problem,):

        self.max_velocity=0.1*(1-0)
        self.NP = self.NPinit
        self.dim = problem.dim

    def initilize(self,problem):
        rand_pos=np.random.uniform(low=0,high=1,size=(self.NP,self.dim))
        self.max_velocity=0.1*(1-0)
        rand_vel = np.random.uniform(low=-self.max_velocity,high=self.max_velocity,size=(self.NP,self.dim))

        cost, violate = self.evaluate_all(rand_pos,problem) # ps
        cost[violate > 0] = 1e15 + violate[violate > 0]
        order = np.argsort(cost)
        cost = cost[order]
        violate = violate[order]
        rand_pos = rand_pos[order]
        self.pop = {}

        self.pop['current_position'] = rand_pos.copy()
        self.pop['velocity'] = rand_vel.copy()
        self.pop['c_cost'] = cost.copy()
        self.pop['violate'] = violate.copy()

        self.pop['pbest_position'] = rand_pos.copy()
        self.pop['pbest'] = rand_vel.copy()

        self.pop['if_position'] = rand_pos.copy()
        self.pop['if_velocity'] = rand_vel.copy()
        self.pop['if_cost'] = cost
        self.pop['if_violate'] = violate
        self.pop['infeasible'] = np.zeros(self.NP)
        self.pop['infeasible'][violate > 0] = True
        self.pop['unused'] = np.zeros(self.NP)
        self.pop['role'] = np.zeros(self.NP)

        if np.sum(violate == 0) < 1:
            self.pop['role'] = np.ones(self.NP)
        else:
            NDT = int(self.p * self.NP)
            self.pop['unused'][NDT:] = 1

        self.bfs = rand_pos[0].copy()
        self.cost_bfs = cost[0] - 1e15 if violate[0] > 0 else cost[0]
        self.violate_bfs = violate[0]

    def bound(self, x):
        return np.clip(x, 0, 1)

    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)
        self.initilize(problem)
        FEs = 0
        maxFEs = problem.maxFEs
        count = 0
        while FEs < maxFEs:
            w = self.ws - (self.ws - self.we) * FEs / maxFEs
            for i in range(self.NP):
                if self.pop['unused'][i]:
                    continue
                if self.pop['role'][i] == 0: # DT
                    dist = np.sqrt(np.sum((self.pop['current_position'][i] - self.pop['current_position']) ** 2, -1))
                    dist[dist <= self.radius] = -1
                    ng = np.argmin(dist, -1)
                    new_DT_vel = w * self.pop['velocity'][i]\
                            + self.c11 * np.random.rand(self.dim) * (self.pop['pbest_position'][i] - self.pop['current_position'][i])\
                            + self.c12 * np.random.rand(self.dim) * ((1 - self.u1) * (self.pop['current_position'][ng] - self.pop['current_position'][i]) + self.u1 * (self.bfs - self.pop['current_position'][i]))
                    new_DT = self.pop['current_position'][i] + new_DT_vel
                    new_DT = self.bound(new_DT)
                    cost_DT, violate_DT = self.evaluate(new_DT, problem)
                    FEs += 1
                    if self.pop['infeasible'][i]:
                        dist = np.sqrt(np.sum((self.pop['if_position'][i] - self.pop['current_position']) ** 2, -1))
                        dist[dist <= self.radius] = -1
                        ng = np.argmin(dist, -1)
                        new_DT_if_vel = w * self.pop['if_velocity'][i]\
                                    + self.c21 * np.random.rand(self.dim) * (self.pop['pbest_position'][i] - self.pop['if_position'][i])\
                                    + self.c22 * np.random.rand(self.dim) * ((1 - self.u2) * (self.pop['current_position'][ng] - self.pop['if_position'][i]) + self.u2 * (self.bfs - self.pop['if_position'][i]))
                        new_DT_if = self.pop['if_position'][i] + new_DT_if_vel
                        new_DT_if = self.bound(new_DT_if)
                        cost_DT_if, violate_DT_if = self.evaluate(new_DT_if, problem)
                        FEs += 1
                        if violate_DT == 0 and violate_DT_if == 0: # all feasible
                            if cost_DT_if < cost_DT:
                                cost_DT = cost_DT_if
                                new_DT = new_DT_if.copy()
                                new_DT_vel = new_DT_if_vel.copy()
                            self.pop['infeasible'][i] = False
                        elif violate_DT > 0 and violate_DT_if == 0: # DT infeasible
                            cost_DT, cost_DT_if = cost_DT_if, cost_DT
                            new_DT_vel, new_DT_if_vel = new_DT_if_vel, new_DT_vel
                            new_DT, new_DT_if = new_DT_if, new_DT
                            violate_DT, violate_DT_if = violate_DT_if, violate_DT
                        elif violate_DT > 0 and violate_DT_if > 0: # all infeasible
                            cost_DT = self.pop['c_cost'][i]
                            new_DT = self.pop['current_position'][i]
                            new_DT_vel = self.pop['velocity'][i]
                        if self.pop['infeasible'][i]:
                            self.pop['if_position'][i] = new_DT_if.copy()
                            self.pop['if_velocity'][i] = new_DT_if_vel.copy()
                            self.pop['if_cost'][i] = cost_DT_if
                            self.pop['if_violate'][i] = violate_DT_if
                    else:
                        if violate_DT > 0:
                            self.pop['infeasible'][i] = True
                            self.pop['if_position'][i] = new_DT.copy()
                            self.pop['if_velocity'][i] = new_DT_vel.copy()
                            self.pop['if_cost'][i] = cost_DT
                            self.pop['if_violate'][i] = violate_DT
                            new_DT = self.pop['current_position'][i].copy()
                            new_DT_vel = self.pop['velocity'][i].copy()
                            cost_DT = self.pop['c_cost'][i]
                            violate_DT = self.pop['violate'][i]
                else: # NL
                    r3j = np.random.rand(self.dim)
                    r4j = np.random.rand(self.dim)
                    D = np.ones(self.dim)
                    D[r4j < self.gamma] = -1
                    S = np.sign(self.pop['velocity'][i])
                    new_DT_vel = D * S * r3j * self.max_velocity
                    new_DT = self.pop['current_position'][i] + new_DT_vel
                    new_DT = self.bound(new_DT)
                    cost_DT, violate_DT = self.evaluate(new_DT, problem)
                    FEs += 1
                self.pop['current_position'][i] = new_DT.copy()
                self.pop['velocity'][i] = new_DT_vel.copy()
                self.pop['c_cost'][i] = cost_DT
                self.pop['violate'][i] = violate_DT
                if violate_DT < self.violate_bfs or (violate_DT == self.violate_bfs and cost_DT < self.cost_bfs):
                    count = 0
                    self.violate_bfs = violate_DT
                    self.cost_bfs = cost_DT
                    self.bfs = new_DT
                    cost_tmp = self.pop['c_cost'].copy()
                    cost_tmp[self.pop['violate'] > 0] = 1e15 + self.pop['violate'][self.pop['violate'] > 0]
                    DTN = int(self.p * self.NP)
                    order = np.argsort(cost_tmp)[:DTN]
                    self.pop['unused'] = np.ones(self.NP)
                    self.pop['unused'][order] = False
                    self.pop['role'] = np.ones(self.NP)
                    self.pop['role'][order] = 0
                else:
                    count += 1
                    if count >= self.sigma:
                        count = 0
                        if np.sum(self.pop['unused']) > 0:
                            idx = np.argmax(self.pop['unused'])
                            self.pop['role'][idx] = 1
                            self.pop['unused'][idx] = False
                            self.pop['infeasible'][idx] = False
        ed_time = time.time()
        return {'x': self.bfs * (problem.ub - problem.lb) + problem.lb, 'fun': self.cost_bfs, 'maxcv': self.violate_bfs, 'runtime': ed_time - st_time, 'nfev': FEs}

                
