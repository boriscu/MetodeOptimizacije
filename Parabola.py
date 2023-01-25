import numpy as np

def func(x):
    return 2*x**4 - 3*x

X = np.array([[1,0.5357,0.5357**2],[1,0.64,0.64**2],[1,1,1]])
F = np.array([func(0.5357),func(0.64),func(1)])
abc = np.linalg.solve(X,F) 
print(abc)
print(func(0.64))