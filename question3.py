import numpy as np
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


def F(xbi, p=0.75, q=0.25):
    if xbi == 1:
        return 1
    res = 0.0
    for i,k in enumerate(xbi):
        add=0
        if k == 1:
            add=q
            for j in range(i):
                add *= p if xbi[j] == 1 else q
        res = res + add
    return res

Xs = np.arange(2049) / (2**11)
Ys = np.array([F(binary_expand_x_over_2_11(j)) for j in range(2049)])

plt.step(Xs, Ys, where="post")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("x")
plt.ylabel(r"$F(x)$")
plt.grid(True, alpha=0.3)
plt.show()