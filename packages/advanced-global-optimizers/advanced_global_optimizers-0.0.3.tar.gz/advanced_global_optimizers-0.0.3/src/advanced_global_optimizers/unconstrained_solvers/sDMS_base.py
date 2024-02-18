import numpy as np
from scipy.optimize import minimize


class sDMStool:
    def __init__(self) -> None:
        pass

    def evaluate(self, x, problem):
        x = x * (problem.ub - problem.lb) + problem.lb
        cost = problem.eval(x)
        self.fes += x.shape[0]
        # cost[cost < self.terminateErrorValue] = 0.0
        return cost

    def initilize(self,problem):
        rand_pos=np.random.uniform(low=0,high=1,size=(self.NP,self.dim))
        self.max_velocity=0.1*(1-0)
        rand_vel = np.random.uniform(low=-self.max_velocity,high=self.max_velocity,size=(self.NP,self.dim))

        c_cost = self.evaluate(rand_pos,problem) # ps

        gbest_val = np.min(c_cost)
        gbest_index = np.argmin(c_cost)
        gbest_position=rand_pos[gbest_index]
        self.max_cost=np.min(c_cost)

        self.particles={'current_position': rand_pos.copy(), #  ps, dim
                          'c_cost': c_cost.copy(), #  ps
                          'pbest_position': rand_pos.copy(), # ps, dim
                          'pbest': c_cost.copy(), #  ps
                          'gbest_position':gbest_position.copy(), # dim
                          'gbest_val':gbest_val,  # 1
                          'velocity': rand_vel.copy(), # ps,dim
                          }
        self.particles['lbest_cost']=np.zeros(self.n_swarm)
        self.particles['lbest_position']=np.zeros((self.n_swarm,self.dim))
        
    def random_regroup(self):
        regroup_index=np.random.permutation(self.NP)
        self.lbest_no_improve-=self.lbest_no_improve
        self.regroup_index=regroup_index
        self.particles['current_position']=self.particles['current_position'][regroup_index] # bs, ps, dim
        self.particles['c_cost']= self.particles['c_cost'][regroup_index] # bs, ps
        self.particles['pbest_position']=self.particles['pbest_position'][regroup_index] # bs, ps, dim
        self.particles['pbest']= self.particles['pbest'][regroup_index] # bs, ps
        self.particles['velocity']=self.particles['velocity'][regroup_index]
        self.per_no_improve=self.per_no_improve[regroup_index]
        
    def update_lbest(self,init=False):
        if init:
            grouped_pbest=self.particles['pbest'].reshape(self.n_swarm,self.m)
            grouped_pbest_pos=self.particles['pbest_position'].reshape(self.n_swarm,self.m,self.dim)

            self.particles['lbest_cost']=np.min(grouped_pbest,axis=-1)
            index=np.argmin(grouped_pbest,axis=-1)
            self.lbest_index=index+np.arange(self.n_swarm)*self.m   # n_swarm,
            self.particles['lbest_position']=grouped_pbest_pos[range(self.n_swarm),index]
            
        else:
            grouped_pbest=self.particles['pbest'].reshape(self.n_swarm,self.m)
            grouped_pbest_pos=self.particles['pbest_position'].reshape(self.n_swarm,self.m,self.dim)
            lbest_cur=np.min(grouped_pbest,axis=-1)
            index=np.argmin(grouped_pbest,axis=-1)
            
            lbest_pos_cur=grouped_pbest_pos[range(self.n_swarm),index]
            filter_lbest=lbest_cur<self.particles['lbest_cost']
            self.lbest_index=np.where(filter_lbest,index+np.arange(self.n_swarm)*self.m,self.lbest_index)

            # update success_num
            
            success=np.sum(grouped_pbest<self.particles['lbest_cost'][:,None],axis=-1)
            
            self.success_num+=success
            
            self.particles['lbest_cost']=np.where(filter_lbest,lbest_cur,self.particles['lbest_cost'])
            self.particles['lbest_position']=np.where(filter_lbest[:,None],lbest_pos_cur,self.particles['lbest_position'])
            self.lbest_no_improve=np.where(filter_lbest,np.zeros_like(self.lbest_no_improve),self.lbest_no_improve+1)

    def get_iwt(self):
        if len(self.parameter_set)<self.LA or np.sum(self.success_num)<=self.LP:
            self.iwt=0.5*np.random.rand(self.n_swarm)+0.4

        else:
            self.iwt=np.random.normal(loc=np.median(self.parameter_set),scale=0.1,size=(self.n_swarm,))

    def update(self,problem):
        rand1=np.random.rand(self.NP,1)
        rand2=np.random.rand(self.NP,1)
        c1=self.c1
        c2=self.c2
        v_pbest=rand1*(self.particles['pbest_position']-self.particles['current_position'])
        if self.cur_mode=='ls':
            v_lbest=rand2*(self.particles['lbest_position'][self.group_index]-self.particles['current_position'])
            self.get_iwt()
            new_velocity=self.iwt[self.group_index][:,None]*self.particles['velocity']+c1*v_pbest+c2*v_lbest
        elif self.cur_mode=='gs':
            v_gbest=rand2*(self.particles['gbest_position'][None,:]-self.particles['current_position'])
            new_velocity=self.w*self.particles['velocity']+c1*v_pbest+c2*v_gbest
        new_velocity=np.clip(new_velocity,-self.max_velocity,self.max_velocity)
        raw_position=self.particles['current_position']+new_velocity
        new_position = np.clip(raw_position,problem.lb,problem.ub)
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
                            'lbest_position':self.particles['lbest_position'],
                            'lbest_cost':self.particles['lbest_cost']
                            }
        self.particles=new_particles

        if self.cur_mode=='ls':
            self.update_lbest()
        
    def update_parameter_set(self):
        max_success_index=np.argmax(self.success_num)
        if len(self.parameter_set)<self.LA:
            self.parameter_set.append(self.iwt[max_success_index])
        else:
            del self.parameter_set[0]
            self.parameter_set.append(self.iwt[max_success_index])

    def quasi_Newton(self, problem):
        sorted_index=np.argsort(self.particles['lbest_cost'])
        refine_index=sorted_index[:int(self.n_swarm//4)]
        refine_pos=self.particles['lbest_position'][refine_index]
        for i in range(refine_pos.shape[0]):
            res=minimize(problem.eval,refine_pos[i],method='BFGS',options={'maxiter':9})
            self.fes+=res.nfev
            if self.particles['lbest_cost'][refine_index[i]]>res.fun:
                self.particles['lbest_position'][refine_index[i]]=res.x
                self.particles['lbest_cost'][refine_index[i]]=res.fun
                # uodate pbest
                self.particles['pbest_position'][self.lbest_index[refine_index[i]]]=res.x
                self.particles['pbest'][self.lbest_index[refine_index[i]]]=res.fun

