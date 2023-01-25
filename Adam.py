import numpy as np
import sympy as sp

def func(x):
    return 0.01*((x[0]-4)**2+2*(x[1]-4)**2)*((x[0]+5)**2+2*(x[1]-5)**2+7)

x1 = sp.symbols('x1')
x2 = sp.symbols('x2')
f=0.01*((x1-4)**2+2*(x2-4)**2)*((x1+5)**2+2*(x2-5)**2+7)
dx1=f.diff(x1)
dx2=f.diff(x2)
print(dx1, dx2)

def dfunc(x):
    x = np.array(x).reshape(np.size(x))
    return np.asarray([[(0.02*x[0] - 0.08)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (2*x[0] + 10)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)],
                [(0.04*x[1] - 0.16)*((x[0] + 5)**2 + 2*(x[1] - 5)**2 + 7) + (4*x[1] - 20)*(0.01*(x[0] - 4)**2 + 0.02*(x[1] - 4)**2)]])

def adam(dfunc,x0,gamma,omega1,omega2,tol,N):
    x = np.array(x0).reshape(len(x0),1)
    v = np.zeros(shape=x.shape)
    m = np.ones(shape = x.shape)

    for i in range(N):
        g = dfunc(x)
        m = m*omega1 + (1-omega1)*g
        v = v*omega2 + (1-omega2)*np.multiply(g,g)
        mk = m/(1-omega1)
        vk = abs(v/(1-omega2))
        x = x - gamma*mk/np.sqrt(vk+tol)
        if(np.linalg.norm(g) < tol):
            break
    return x, i+1