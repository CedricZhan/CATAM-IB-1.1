import random
import numpy as np
import matplotlib.pyplot as plt

n=30
p=2/3
N=100000

def generate_Ui(p):
    return 1 if random.random() < p else 0

def indicator(X,x):
    return 1 if X <= x else 0

def generate_Xn(n, p):
    Xn = 0
    for i in range(n):
        Xn += generate_Ui(p)/2**(i+1)
    return Xn

samples = np.array([generate_Xn(n, p) for _ in range(N)])

Xs = np.sort(samples)
Ys = np.arange(1, N+1) / N


plt.step(Xs, Ys, where="post")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel(r"$\hat F(x)$")
plt.grid(True, alpha=0.3)
plt.show()