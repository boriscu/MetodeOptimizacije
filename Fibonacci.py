#x**2 - sin(2x)

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    f = x**2-2*x+1
    return f

def fibonaci_broj(n):
    if n<3:
        f = 1
    else:
        fp = 1
        fpp =1
        for i in range(3,n+1):
            f = fp+fpp
            fpp = fp
            fp = f
    return f

def fibonaci_metod(a,b,tol):
    n = 1
    while (abs(b-a)/tol) > fibonaci_broj(n):
        n+=1
    
    print(n,fibonaci_broj(n))

    x1 = a + fibonaci_broj(n-2)/fibonaci_broj(n)*(b-a)
    x2 = a + b - x1

    for i in range(2,n+1):
        if(func(x1)>func(x2)):
            a = x1
            x1 = x2
            x2 = a + b - x1
        else:
            b = x2
            x2 = x1
            x1 = a + b - x2
    
    if(func(x1) < func(x2)):
        x_opt = x1
        f_opt = func(x_opt)
    else:
        x_opt = x2
        f_opt = func(x_opt)
    
    return x_opt,f_opt,n

a = -1
b = 3
tol = 0.1
[x_opt,f_opt,n] = fibonaci_metod(a,b,tol)
print(x_opt,f_opt,n)

x = np.linspace(0, 2, 1000)
f = np.linspace(0,0,len(x))

for i in range(0,len(x)):
    f[i] = func(x[i])

p = plt.plot(x,f,'b--')
p = plt.plot(x_opt,f_opt, '*r', markersize=20)
p = plt.show()