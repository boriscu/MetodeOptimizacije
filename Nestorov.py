import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sp

def func2d(x):
    return x[0]**2*x[1]**3+3*x[0]**2*x[1]

x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
f = 2*x1**2 - 1.05*x1**4 + (x1**6)/6 + x1*x2 + x2**2
dif1 = f.diff(x1)
dif2 = f.diff(x2)
print(dif1,dif2)

def dfunc(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[2*x[0]*x[1]**3+6*x[0]*x[1]],
                [3*x[0]**2*x[1]**2+3*x[0]**2]])
				
def nestorov(x0,gamma,tol,omega,N,gradf):
    x = np.array(x0).reshape(len(x0),1)
    v = np.zeros(shape=x.shape)

    for i in range(N):
        xp = x - omega*v
        g = gradf(xp)
        v = omega*v + gamma*g
        x = x - v
        if np.linalg.norm(g) < tol:
            break
    
    return x,func2d(x),i+1
	
x02 = [-5,5]
gamma = 0.01
omega = 0.1 
tol = 0.0001
N = 100

[x_opt,f_opt,iter] = nestorov(x02,gamma,tol,omega, N,lambda x : dfunc(x))
print("Nestorov: ", x_opt,f_opt,iter)