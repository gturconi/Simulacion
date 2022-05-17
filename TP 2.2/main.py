import random
import matplotlib.pyplot as plt
from numpy.random import random
from numpy import floor, log as ln, exp

#En esta parte del codigo estan las distribuciones

# Genenador distribucion Uniforme
def uniform (a,b):
    r = random()
    x= a+(b-a)*r
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
def normal(ex,stdx):
    sum = 0
    for i in range (12):
        r=random()
        sum += r
    x = stdx*(sum-6.0)+ex
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
        if (r - p) <= 0:
            x += 1
    return x

#Genenador distribucion Hypergeometrica
def hypergeometric(tn, ns, p):
    x = 0
    for i in range(1, ns):
        r = random()
        if (r - p )<= 0:
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
    while (tr-b) >= 0:
        r = random()
        tr = tr * r
        x += 1
    return x

#Genenador distribucion Empirica

#------------esto falta----------------




#Definir parametros de la distribucion uniforme
uni_a = 1
uni_b = 4
dist_uniforme = []

#Definir parametros de la distribucion exponencial
ex_ex = 7
dist_exponencial = []

#Definir parametros de la distribucion gamma
gamma_k = 10
gamma_alpha = 3
dist_gamma = []

#Definir parametros de la distribucion normal
nor_ex = 2.5
nor_stdx = 25
dist_normal = []

#Definir parametros de la distribucion pascal
pas_k = 4
pas_q = 0.8
dist_pascal = []

#Definir parametros de la distribucion binomial
bin_n = 100
bin_p = 0.5
dist_binomial = []

#Definir parametros de la distribucion Hipergeometrica
hiper_tn = 500
hiper_ns = 80
hiper_p = 0.6
dist_hipergeometrica = []

#Definir parametros de la distribucion Poisson
poisson_p = 10
dist_poisson = []

for i in range(500):
    dist_uniforme.append(uniform(uni_a, uni_b))
    dist_exponencial.append(exponential(ex_ex))
    dist_gamma.append(gamma(gamma_k, gamma_alpha))
    dist_normal.append(normal(nor_ex, nor_stdx))
    dist_pascal.append(pascal(pas_k, pas_q))
    dist_binomial.append(binomial(bin_n, bin_p))
    dist_hipergeometrica.append(hypergeometric(hiper_tn, hiper_ns, hiper_p))
    dist_poisson.append(poisson(poisson_p))

#En esta parte del codigo estan las graficas a las distribuciones

def graficar(n, u, e, g, p, b, h, po):
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

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(p)
    plt.title('Pascal')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(b)
    plt.title('Binomial')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(h)
    plt.title('Hipergeometrica')
    plt.show()

    plt.ylabel('')
    plt.xlabel('')
    plt.hist(po)
    plt.title('Poisson')
    plt.show()


graficar(dist_normal, dist_uniforme, dist_exponencial, dist_gamma, dist_pascal, dist_binomial, dist_hipergeometrica, dist_poisson);
