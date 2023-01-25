import math
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    f = x**3-0.165*x**2+3.993*10**(-4)
    return f

def dfunc(x):
    f = 3*x**2-0.33*x 
    return f

def ddfunc(x):
    f = 24*x**2-12*x+4
    return f

def secica(x0,x1,tol):
    x_starije = math.inf
    x_staro = x0
    x_novo = x1
    iter = 0

    while(abs(x_staro-x_novo)>tol):
        x_starije = x_staro
        x_staro = x_novo
        x_novo = x_staro - dfunc(x_staro)*(x_staro-x_starije)/(dfunc(x_staro)-dfunc(x_starije))
        print(x_novo)
        iter+=1
    
    x_opt = x_novo
    f_opt = func(x_opt)
    return x_opt, f_opt, iter

x0 = 0.02
x1 = 0.05
tol = 0.001
x_opt,f_opt,iter = secica(x0,x1,tol)
print(x_opt,f_opt,iter)

x = np.linspace(-2,2,1000)
f = np.linspace(0,0,len(x))

for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f,'b--')
p = plt.plot(x_opt,f_opt,'or',markersize = 20, markeredgewidth = 3)
plt.show()