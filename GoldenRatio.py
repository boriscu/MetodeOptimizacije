import numpy as np
import matplotlib.pyplot as plt
import math

def func(x):
    f = 3*np.sin(2*x) + 5*x - 1
    return f

def zlatniPresek(a,b,tol):
    c = (3 - math.sqrt(5))/2
    x1 = a + c*(b-a)
    x2 = a + b - x1
    n = 1
    while abs(b-a)>tol:
        n+=1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c*(b-a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c*(b-a)
            x2 = a + b -x1
    
    if func(x1) < func(x2):
        x_opt = x1
        f_opt = func(x_opt)
    else:
        x_opt = x2
        f_opt = func(x_opt)

    return x_opt,f_opt,n

a = 1.5
b = 4
tol = 0.1
[x_opt,f_opt,n] = zlatniPresek(a,b,tol)
print(x_opt,f_opt,n)

x = np.linspace(1.5,4,1000)
f = np.linspace(0,0,len(x))

for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f,'b--')
p = plt.plot(x_opt,f_opt,'r*',markersize=20)
plt.show()