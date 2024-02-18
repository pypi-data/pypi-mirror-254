import numpy as np
from .GLPSO_base import GLPSOtool
import time


class GLPSO(GLPSOtool):
    def __init__(self, param):
        # self.pm=0.01
        # self.NP=100
        # self.nsel=10
        # self.w=0.7298
        # self.c1=1.49618
        # self.sg=7
        # self.rho=0.2
        self.pm = param['pm']
        self.NP = param['NP']
        self.nsel = param['nsel']
        self.w = param['w']
        self.c1 = param['c1']
        self.sg = param['sg']
        self.rho = param['rho']

    def init(self, problem):
        self.dim = problem.dim
        self.exemplar_stag=np.zeros(self.NP)
    
    def optimize(self, problem):
        st_time = time.time()
        self.init(problem)
        self.init_population(problem)
        while self.fes < problem.maxFEs:
        
            rand=np.random.rand(self.NP,self.dim)
            new_velocity=self.w*self.particles['velocity']+self.c1*rand*(self.exemplar-self.particles['current_position'])
            new_velocity=np.clip(new_velocity,-self.max_velocity,self.max_velocity)

            new_position=self.particles['current_position']+new_velocity

            new_velocity=np.where(new_position>self.ub,new_velocity*-0.5,new_velocity)
            new_velocity=np.where(new_position<self.lb,new_velocity*-0.5,new_velocity)
            new_position=np.clip(new_position,self.lb,self.ub)

            new_cost=self.evaluate(new_position,problem)

            filters = new_cost < self.particles['pbest']
            new_cbest_val = np.min(new_cost)
            new_cbest_index = np.argmin(new_cost)

            filters_best_val=new_cbest_val<self.particles['gbest_val']
            # update particles
            new_particles = {'current_position': new_position, # bs, ps, dim
                                'c_cost': new_cost, # bs, ps
                                'pbest_position': np.where(np.expand_dims(filters,axis=-1),
                                                            new_position,
                                                            self.particles['pbest_position']),
                                'pbest': np.where(filters,
                                                    new_cost,
                                                    self.particles['pbest']),
                                'velocity': new_velocity,
                                'gbest_val':np.where(filters_best_val,
                                                        new_cbest_val,
                                                        self.particles['gbest_val']),
                                'gbest_position':np.where(np.expand_dims(filters_best_val,axis=-1),
                                                            new_position[new_cbest_index],
                                                            self.particles['gbest_position']),
                                'gbest_index':np.where(filters_best_val,new_cbest_index,self.particles['gbest_index'])
                                }
        
            self.particles=new_particles
            self.exemplar_update(problem,init=False)

            self.found_best=np.where(self.particles['gbest_val']<self.found_best,self.particles['gbest_val'],self.found_best)

        ed_time = time.time()
        return {'x': self.particles['gbest_position'] * (problem.ub - problem.lb) + problem.lb, 'fun': self.particles['gbest_val'], 'runtime': ed_time - st_time, 'nfev': self.fes}
    