import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def F(xbi, p=0.75, q=0.25):
    res = 0.0
    for i,k in enumerate(xbi):
        add=0
        if k == 1:
            add=q
            for j in range(i):
                add *= p if xbi[j] == 1 else q
        res = res + add
    return res

def bits_to_fraction(xbi):
    return sum(Fraction(b, 2**(i+1)) for i, b in enumerate(xbi))

def fraction_to_bits(x, n):
    k = int(x * (2**n))
    s = format(k, f"0{n}b")
    return [int(i) for i in s]

c_frac = Fraction(9, 16)
c_bits = [1,0,0,1]
Fc = F(c_bits)

ns = range(6, 26) 
deltas = []
slopes = []

for n in ns:
    d = Fraction(1, 2**n)

    R = c_frac + d
    Rbi = fraction_to_bits(R, n)  
    FR = F(Rbi)
    deltas.append(float(d))
    slopes.append((FR - Fc) / float(d))

    L = c_frac - d
    Lbi = fraction_to_bits(L, n)
    FL = F(Lbi)
    deltas.append(-float(d))
    slopes.append((FL - Fc) / (-float(d)))

deltas = np.array(deltas)
slopes = np.array(slopes)

idx = np.argsort(deltas)
deltas = deltas[idx]
slopes = slopes[idx]

plt.figure()
plt.plot(deltas, slopes, marker='o', linestyle='-')
plt.xscale('symlog', linthresh=1e-6)  
plt.xlabel(r'$\delta$')
plt.ylabel(r'$(F(c+\delta)-F(c))/\delta$')
plt.show()
