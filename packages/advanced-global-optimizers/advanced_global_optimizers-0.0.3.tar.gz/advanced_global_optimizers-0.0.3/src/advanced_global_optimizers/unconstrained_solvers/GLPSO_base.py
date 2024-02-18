import numpy as np


class GLPSOtool:
    def __init__(self) -> None:
        pass

    def exemplar_crossover(self):
        rand_index=np.random.randint(low=0,high=self.NP,size=(self.NP,self.dim))
        xs=self.particles['pbest_position']
        rand_par=xs[rand_index,np.arange(self.dim)[None,:]]
        rand_pbest_val=self.particles['pbest'][rand_index]
        filter=rand_pbest_val<self.particles['pbest'][:,None]
        r=np.random.rand(self.NP,self.dim)
        uniform_crossover=r*self.particles['pbest_position']+(1-r)*self.particles['gbest_position'][None,:]
        self.new_exemplar=np.where(filter,rand_par,uniform_crossover)

    def exemplar_mutation(self):
        rand_pos=np.random.uniform(low=self.lb,high=self.ub,size=(self.NP,self.dim))
        self.new_exemplar=np.where(np.random.rand(self.NP,self.dim)<self.pm,rand_pos,self.new_exemplar)
    
    def exemplar_selection(self,problem,init=False):
        new_exemplar_cost=self.evaluate(self.new_exemplar,problem)
        if init:
            self.exemplar=self.new_exemplar
            self.exemplar_cost=new_exemplar_cost
        else:
            suv_filter=new_exemplar_cost<self.exemplar_cost
            self.exemplar=np.where(suv_filter[:,None],self.new_exemplar,self.exemplar)
            self.exemplar_stag=np.where(suv_filter,np.zeros_like(self.exemplar_stag),self.exemplar_stag+1)
            self.exemplar_cost=np.where(suv_filter,new_exemplar_cost,self.exemplar_cost)
        
        min_exemplar_cost=np.min(self.exemplar_cost)
        
        self.found_best=np.where(min_exemplar_cost<self.found_best,min_exemplar_cost,self.found_best)

    def exemplar_tour_selection(self):
        rand_index=np.random.randint(low=0,high=self.NP,size=(self.NP,self.nsel))
        rand_exemplar=self.exemplar[rand_index]
        rand_exemplar_cost=self.exemplar_cost[rand_index]
        min_exemplar_index=np.argmin(rand_exemplar_cost,axis=-1)  # bs, ps
        selected_exemplar=rand_exemplar[range(self.NP),min_exemplar_index]
        return selected_exemplar
    
    def exemplar_update(self,problem,init):
        self.exemplar_crossover()
        self.exemplar_mutation()
        self.exemplar_selection(problem,init)
        
        filter=self.exemplar_stag>self.sg
        if np.any(filter):
            self.exemplar=np.where(filter[:,None],self.exemplar_tour_selection(),self.exemplar)
    
    def init_population(self,problem):
        self.ub=1
        self.lb=0
        self.fes=0
        self.exemplar_cost=1e+10
        
        rand_pos=np.random.uniform(low=problem.lb,high=problem.ub,size=(self.NP,self.dim))
        self.max_velocity=self.rho*(problem.ub-problem.lb)
        rand_vel = np.random.uniform(low=-self.max_velocity,high=self.max_velocity,size=(self.NP,self.dim))
        c_cost = self.evaluate(rand_pos,problem) # ps
        
        gbest_val = np.min(c_cost)
        gbest_index = np.argmin(c_cost)
        gbest_position=rand_pos[gbest_index]
        self.max_cost=np.min(c_cost)
        # print("rand_pos.shape:{}".format(rand_pos.shape))

        self.particles={'current_position': rand_pos.copy(), #  ps, dim
                        'c_cost': c_cost.copy(), #  ps
                        'pbest_position': rand_pos.copy(), # ps, dim
                        'pbest': c_cost.copy(), #  ps
                        'gbest_position':gbest_position.copy(), # dim
                        'gbest_val':gbest_val,  # 1
                        'velocity': rand_vel.copy(), # ps,dim
                        'gbest_index':gbest_index # 1
                        }

        self.found_best=self.particles['gbest_val'].copy()
        self.exemplar_update(problem,init=True)

        self.cost = [self.particles['gbest_val']]

    def evaluate(self, x, problem):
        x = x * (problem.ub - problem.lb) + problem.lb
        cost = problem.eval(x)
        self.fes += x.shape[0]
        return cost

