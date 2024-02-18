import numpy as np


class DTPSOtool:
    def __init__(self) -> None:
        pass

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

    def violate_compare(self, i, new_DT, cost_DT, violate_DT, new_DT_vel, new_DT_if, cost_DT_if, violate_DT_if, new_DT_if_vel):
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
        return new_DT, cost_DT, violate_DT, new_DT_vel, new_DT_if, cost_DT_if, violate_DT_if, new_DT_if_vel

    def exchange_DT(self, i, new_DT, new_DT_vel, cost_DT, violate_DT):
        self.pop['infeasible'][i] = True
        self.pop['if_position'][i] = new_DT.copy()
        self.pop['if_velocity'][i] = new_DT_vel.copy()
        self.pop['if_cost'][i] = cost_DT
        self.pop['if_violate'][i] = violate_DT
        new_DT = self.pop['current_position'][i].copy()
        new_DT_vel = self.pop['velocity'][i].copy()
        cost_DT = self.pop['c_cost'][i]
        violate_DT = self.pop['violate'][i]
        return new_DT, new_DT_vel, cost_DT, violate_DT

    def update_pop(self, new_DT, cost_DT, violate_DT):
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

    def evaluate(self, x, problem, detailed=False):
        x = (x - self.config.norm_lb) / (self.config.norm_ub - self.config.norm_lb)
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = 0
        # for g in problem.g:
        #     v += np.maximum(0, g(x[None, :]))[0]
        # for h in problem.h:
        #     v += np.fabs(h(x[None, :]))[0]
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        if detailed:
            return f, v, gs, hs
        return f, v
    
    def evaluate_all(self, x, problem):
        x = (x - self.config.norm_lb) / (self.config.norm_ub - self.config.norm_lb)
        x = x * (problem.ub - problem.lb) + problem.lb
        f = problem.eval(x)
        v = np.zeros(x.shape[0])
        # for g in problem.g:
        #     v += np.maximum(0, g(x))
        # for h in problem.h:
        #     v += np.fabs(h(x))
        gs = np.maximum(0, problem.g_constrain(x))
        v += np.sum(gs, -1)
        hs = problem.h_constrain(x)
        v += np.sum(np.abs(hs), -1)
        return f, v
    
    def update_unused(self, ):
        if np.sum(self.pop['unused']) > 0:
            idx = np.argmax(self.pop['unused'])
            self.pop['role'][idx] = 1
            self.pop['unused'][idx] = False
            self.pop['infeasible'][idx] = False

    def update_indiv(self, i, new_DT, new_DT_vel, cost_DT, violate_DT):
        self.pop['current_position'][i] = new_DT.copy()
        self.pop['velocity'][i] = new_DT_vel.copy()
        self.pop['c_cost'][i] = cost_DT
        self.pop['violate'][i] = violate_DT

    def get_DT_vel(self, i, w):
        dist = np.sqrt(np.sum((self.pop['current_position'][i] - self.pop['current_position']) ** 2, -1))
        dist[dist <= self.radius] = -1
        ng = np.argmin(dist, -1)
        new_DT_vel = w * self.pop['velocity'][i]\
            + self.c11 * np.random.rand(self.dim) * (self.pop['pbest_position'][i] - self.pop['current_position'][i])\
            + self.c12 * np.random.rand(self.dim) * ((1 - self.u1) * (self.pop['current_position'][ng] - self.pop['current_position'][i]) + self.u1 * (self.bfs - self.pop['current_position'][i]))
        return new_DT_vel
    
    def get_DT_if_vel(self, i, w):
        dist = np.sqrt(np.sum((self.pop['if_position'][i] - self.pop['current_position']) ** 2, -1))
        dist[dist <= self.radius] = -1
        ng = np.argmin(dist, -1)
        new_DT_if_vel = w * self.pop['if_velocity'][i]\
                    + self.c21 * np.random.rand(self.dim) * (self.pop['pbest_position'][i] - self.pop['if_position'][i])\
                    + self.c22 * np.random.rand(self.dim) * ((1 - self.u2) * (self.pop['current_position'][ng] - self.pop['if_position'][i]) + self.u2 * (self.bfs - self.pop['if_position'][i]))
        return new_DT_if_vel
