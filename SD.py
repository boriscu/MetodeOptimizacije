import sympy as sp
import numpy as np

def sd (gradf,x0,tol,gamma,N):
    x = np.array(x0).reshape(len(x0),1)

    for i in range(N):
        g = gradf(x)
        x = x - gamma*g

        if(np.linalg.norm(g) < tol):
            break
    
    return x, func(x), i+1

def func(x):
    return 0.01*((x[0]-4)**2+2*(x[1]-4)**2)*((x[0]+5)**2+2*(x[1]-5)**2+7)

def dfunc(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[(0.02*x[0] - 0.08)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (2*x[0] + 10)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)],
                [(0.04*x[1] - 0.16)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (4*x[1] - 20)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)]])

x0 = [-1,1]
gamma = 0.2
N = 100
tol = 0.0001
x_opt, f_opt, it = sd(lambda x : dfunc(x), x0,tol,gamma,N)
print(x_opt,it,f_opt)
