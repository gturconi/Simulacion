import random
import matplotlib.pyplot as plt
from numpy.random import random
from numpy import floor, log as ln, exp

#En esta parte del codigo estan las distribuciones

# Genenador distribucion Uniforme
def uniform (a,b):
    x = []
    for i in range(500):
        r = random()
        x.append(a+(b-a)*r)
    return x
dist_uniforme=(uniform(1,4))


# Genenador distribucion Exponencial
def exponential(ex):
    x = []
    for i in range(500):
        r = random()
        x += [-ex * ln(r)]
    return x
dist_exponencial=(exponential(7))


# Genenador distribucion Gamma
def gamma(k, alpha):
    x = []
    for j in range(500):
        tr = 1
        for i in range(k):
            r = random()
            tr = tr * r
            x.append(-ln(tr) / alpha)
    return x
dist_gamma=(gamma(5,10))


# Genenador distribucion Normal
def normal(ex,stdx):
    x=[]
    for i in range(500):
        sum = 0
        for j in range (12):
            r=random()
            sum += r
        x+=[stdx*(sum-6.0)+ex]
    return x
dist_normal = normal(2.35, 30)


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






#En esta parte del codigo estan las graficas a las distribuciones

def graficar(n,u,e,g):
    plt.ylabel('')
    plt.xlabel('')
    plt.hist(n)
    plt.title('Normal')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(u)
    plt.title('Uniforme')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(e)
    plt.title('Exponencial')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(g)
    plt.title('Gamma')
    plt.show()


graficar(dist_normal, dist_uniforme, dist_exponencial, dist_gamma);