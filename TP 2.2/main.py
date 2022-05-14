
from numpy.random import random
from numpy import floor, log as ln, exp


# Genenador distribucion Uniforme
def uniform(a, b):
    r = random()
    x = a + (b - a) * r
    return x

# Genenador distribucion Exponencial
def exponential(ex):
    r = random()
    x = -ex * ln(r)
    return x

# Genenador distribucion Gamma
def gamma(k, alpha):
    tr = 1
    for i in range(k):
        r = random()
        tr = tr * r
    x = -ln(tr) / alpha
    return x

# Genenador distribucion Normal
def normal(ex, stdx):
    sum = 0
    for i in range(12):
        r = random()
        sum += r
    x = stdx * (sum - 6) + ex
    return x

# Genenador distribucion Pascal
def pascal(k,q):
    tr = 1
    qr = ln(q)
    for i in range(k):
        r = random()
        tr = tr * r
    x = floor(ln(tr)/qr)
    return x

#Genenador distribucion Binomial
def binomial(n, p):
    x = 0
    for i in range(1, n):
        r = random()
        if ((r - p) <= 0):
            x += 1
    return x

#Genenador distribucion Hypergeometrica
def hypergeometric(tn, ns, p):
    x = 0
    for i in range(1, ns):
        r = random()
        if ((r - p )<= 0):
            s = 1
            x += 1
        else:
            s = 0
        p = (tn * p - s) / (tn - 1)
        tn = tn - 1
    return x

#Genenador distribucion Poisson
def poisson(p):
    x = 0
    b = exp(-p)
    tr = 1
    while((tr-b) >= 0):
        r = random()
        tr = tr * r
        x += 1
    return x

#Genenador distribucion Empirica
