import numpy as np

def rotatefunc(x, Mr):
    return np.matmul(Mr, x.transpose()).transpose()


def sr_func(x, Os, Mr):  # shift and rotate
    y = x - Os
    # x, Os belongs to [-100, 100]
    if len(x.shape) < 2:
        y = y[None, :]
        res = rotatefunc(y, Mr)
        return res[0]
    else:
        return rotatefunc(y, Mr)


def rotate_gen(dim):  # Generate a rotate matrix
    random_state = np.random
    H = np.eye(dim)
    D = np.ones((dim,))
    mat = np.eye(dim)
    for n in range(1, dim):
        x = random_state.normal(size=(dim - n + 1,))
        D[n - 1] = np.sign(x[0])
        x[0] -= D[n - 1] * np.sqrt((x * x).sum())
        # Householder transformation
        Hx = (np.eye(dim - n + 1) - 2. * np.outer(x, x) / (x * x).sum())
        mat[n - 1:, n - 1:] = Hx
    H = np.dot(H, mat)
    # Fix the last sign such that the determinant is 1
    D[-1] = (-1) ** (1 - (dim % 2)) * D.prod()
    # Equivalent to np.dot(np.diag(D), H) but faster, apparently
    H = (D * H.T).T
    return H



class Problem:
    def __init__(self, dim, obj_func, bounds, maxFEs, args=(), constraints=[]):
        self.dim = dim
        self.obj_func = obj_func
        self.maxFEs = maxFEs
        bounds = np.array(bounds)
        self.ub = bounds[:,1]
        self.lb = bounds[:,0]
        self.constrained = False if len(constraints) < 1 else True
        self.constraints = constraints
        self.args = args
        if not isinstance(args, tuple):
            self.args = (args,)
        self.g_sep_constrains, self.h_sep_constrains = [], []
        if self.constrained:
            if not isinstance(constraints, list):
                constraints = [constraints]
            for item in constraints:
                assert isinstance(item, dict)
                assert 'type' in item.keys()
                assert 'fun' in item.keys()
                if item['type'] == 'eq':
                    self.h_sep_constrains.append(item['fun'])
                elif item['type'] == 'ineq':
                    self.g_sep_constrains.append(item['fun'])
                else:
                    raise TypeError('Unknown constraint type')

    def g_constrain(self, x):
        x_in = x.copy()
        if len(x.shape) < 2:
            x_in = x[None, :]
        res = []
        for g_fun in self.g_sep_constrains:
            fs = []
            for xi in x_in:
                f = g_fun(xi)
                fs.append(f)
            if len(x.shape) < 2:
                fs = fs[0]
            res.append(fs)
        if len(res) == 0:
            return np.zeros(1) if len(x.shape) < 2 else np.zeros((x.shape[0], 1))
        return np.transpose(np.array(res))
    
    def h_constrain(self, x):
        x_in = x.copy()
        if len(x.shape) < 2:
            x_in = x[None, :]
        res = []
        for h_fun in self.h_sep_constrains:
            fs = []
            for xi in x_in:
                f = h_fun(xi)
                fs.append(f)
            if len(x.shape) < 2:
                fs = fs[0]
            res.append(fs)
        if len(res) == 0:
            return np.zeros(1) if len(x.shape) < 2 else np.zeros((x.shape[0], 1))
        return np.transpose(res)

    def eval(self, x):
        x_in = x.copy()
        x_in = np.clip(x_in, a_min=self.lb, a_max=self.ub)
        if len(x_in.shape) < 2:
            return self.obj_func(x_in, *self.args)
        else:
            fs = []
            for xi in x_in:
                f = self.obj_func(xi, *self.args)
                fs.append(f)
            return np.array(fs)
        
