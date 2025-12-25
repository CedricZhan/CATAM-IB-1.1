import numpy as np
import random
import matplotlib.pyplot as plt

def binary_expand_x_over_2_11(x):
    if x > 2048 or x < 0 or not float(x).is_integer():
        raise ValueError("x must be an integer within [0, 2^11]")
    x = int(x)
    if x == 2048:
        return 1

    res = [0]*11
    q = x
    pos = 10
    while q > 0 and pos >= 0:
        q, r = divmod(q, 2)
        res[pos] = r
        pos -= 1
    return res


def F(xbi):
    if xbi == 1:
        return 1
    else:
        res = 0
        for k in range(11):
            if xbi[k] == 1:
                add = 1/4
                for i in range(k):
                    add *= 3/4 if xbi[i] == 1 else 1/4
                res += add
        return res


Xs_exact = np.arange(2049) / (2**11)
Ys_exact = np.array([F(binary_expand_x_over_2_11(j)) for j in range(2049)])

n = 30
p = 3/4
N = 100000

def generate_Ui(p):
    return 1 if random.random() < p else 0

def generate_Xn(n, p):
    Xn = 0
    for i in range(n):
        Xn += generate_Ui(p) / 2**(i+1)
    return Xn

samples = np.array([generate_Xn(n, p) for _ in range(N)])

Xs_mc = np.sort(samples)
Ys_mc = np.arange(1, N+1) / N

grid = np.arange(2049) / (2**11)   

Fhat = np.array([np.mean(samples <= x) for x in grid])

MSE = np.mean((Fhat - Ys_exact)**2)

print("MSE =", MSE)

