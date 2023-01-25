import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    f = x**4 - 5*x**3 - 2*x**2 + 24*x
    return f

def dfunc(x):
    f = 4*x**3 - 15*x**2 - 4*x + 24
    return f

def ddfunc(x):
    f = 12*x**2 - 30*x - 4
    return f

def newtonRaphson(x0, tol):
    x_novo = x0
    x_staro = math.inf
    iter = 0

    while(abs(x_novo-x_staro)>tol):
        x_staro = x_novo
        x_novo = x_staro - dfunc(x_staro)/ddfunc(x_staro)
        iter+=1
    
    x_opt = x_novo
    f_opt = func(x_opt)
    return x_opt, f_opt, iter


x0 = 1
tol = 0.0001
[x_opt,f_opt, iter] = newtonRaphson(x0,tol)
print(x_opt,f_opt,iter)

##Test
x = np.linspace(0,3,1000)
f = np.linspace(0,0,len(x))

for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f, 'b--')
p = plt.plot(x_opt, f_opt, 'or', markersize = 20, markeredgewidth = 3)
plt.show()