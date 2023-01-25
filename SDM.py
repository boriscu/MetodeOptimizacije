import numpy as np
import sympy as sp

def func(x):
   return 0.01*((x[0]-4)**2+2*(x[1]-4)**2)*((x[0]+5)**2+2*(x[1]-5)**2+7)

x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
f=0.01*((x1-4)**2+2*(x2-4)**2)*((x1+5)**2+2*(x2-5)**2+7)

dx1 = f.diff(x1)
dx2 = f.diff(x2)
print(dx1,dx2)

def dfunc(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[(0.02*x[0] - 0.08)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (2*x[0] + 10)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)],
                [(0.04*x[1] - 0.16)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (4*x[1] - 20)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)]])

def sdm(dfunc,x0,tol,gamma,omega,N):
    x = np.array(x0).reshape(len(x0),1)
    v = np.zeros(shape=x.shape)

    for i in range(N):
        g = dfunc(x)
        v = omega*v + gamma*g
        x = x - v
        if(np.linalg.norm(g) < tol):
            break
    
    return x, func(x), i+1

x0 = [-1,1]
gamma = 0.2
N = 100
tol = 0.0001
omega = 0.1
x_opt, f_opt, it = sdm(lambda x : dfunc(x), x0,tol,gamma, omega, N)
print(x_opt,it,f_opt)
