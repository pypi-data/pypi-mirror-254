import numpy as np
from .sDMS_base import sDMStool
import time

class sDMS_PSO(sDMStool):
    def __init__(self,param):
        # self.w,self.c1,self.c2=0.729,1.49445,1.49445
        # self.m,self.R,self.LP,self.LA,self.L,self.L_FEs=3,10,10,8,100,200
        # self.NP=99
        self.w=param['w']
        self.NP=param['NP']
        self.c1=param['c1']
        self.c2=param['c2']
        self.m=param['m']
        self.R=param['R']
        self.LP=param['LP']
        self.LA=param['LA']
        self.L=param['L']
        self.L_FEs=param['L_FEs']
        
    def init(self, problem, ):
        self.dim = problem.dim
        self.n_swarm=self.NP//self.m

        self.cur_mode='ls'
        self.gen=0
        self.fes=0
        self.n_swarm=self.NP//self.m
        self.learning_period=True
        self.group_index=np.zeros(self.NP,dtype=np.int8)
        self.per_no_improve=np.zeros(self.NP)
        self.lbest_no_improve=np.zeros(self.n_swarm)
        
        assert self.NP%self.m==0, 'population cannot be update averagely'
        for sub_swarm in range(self.n_swarm):
            if sub_swarm!=self.n_swarm-1:
                self.group_index[sub_swarm*self.m:(sub_swarm+1)*self.m]=sub_swarm
            else:
                self.group_index[sub_swarm*self.m:]=sub_swarm
        
        self.parameter_set=[]
        self.success_num=np.zeros((self.n_swarm))

    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)

        self.initilize(problem)
        self.random_regroup()
        self.update_lbest(init=True)
        self.fes_eval=np.zeros_like(self.fes)
        self.cost = [self.particles['gbest_val']]
        maxFEs = problem.maxFEs
        while self.fes < maxFEs:

            while self.fes<0.95*maxFEs:
                self.cur_mode='ls'
                self.gen+=1
                self.w-=0.5/(maxFEs/self.NP)
                self.success_num-=self.success_num
                for j in range(self.LP):
                    self.update(problem)
                self.update_parameter_set()
                if self.gen%self.L==0:
                    self.quasi_Newton(problem)

                if self.gen%self.R==0:
                    self.random_regroup()
                    self.update_lbest(init=True)

            while self.fes<maxFEs:
                self.cur_mode='gs'
                self.update(problem)
        ed_time = time.time()
        return {'x': self.particles['gbest_position'] * (problem.ub - problem.lb) + problem.lb, 'fun': self.particles['gbest_val'], 'runtime': ed_time - st_time, 'nfev': self.fes}
    
