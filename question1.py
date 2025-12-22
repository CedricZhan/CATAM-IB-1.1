import random
import numpy as np
import matplotlib.pyplot as plt

n=30
p=2/3

def generate_Ui(p):
    return 1 if random.random() < p else 0

def indicator(X,x):
    return 1 if X <= x else 0

def generate_Xn(n, p):
    Xn = 0
    for i in range(n):
        Xn += generate_Ui(p)/2**(i+1)
    return Xn

def CDFapprox(x, n, p, N):
    F = 0
    for i in range(N):
        Xn = indicator(generate_Xn(n,p),x)
        F+=Xn
    F=F/N
    return F

xs = np.linspace(0, 1, 20)

N = 10000
Fs = [CDFapprox(x, n, p, N) for x in xs]

plt.plot(xs, Fs)
plt.xlabel("x")
plt.ylabel(r"$\hat{F}(x)$")
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.grid(True)
plt.show()