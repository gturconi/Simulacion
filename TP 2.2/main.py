import random
import matplotlib.pyplot as plt
import numpy
import numpy as np
import scipy
import sm as sm
import stats
from numpy.random import random, poisson
from numpy import floor, log as ln, exp
from scipy.stats import chisquare
import collections
import copy
from scipy.stats import kstest
from statsmodels.distributions.empirical_distribution import ECDF


#En esta parte del codigo estan las distribuciones

# Genenador distribucion Uniforme
from scipy.stats._stats_py import KstestResult


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

def empirica(sample):
    x=[]
    for i in range(100):
        r = random()
        a=0
        z=1
        for j in sample:
            a+=j
            if(r<=a):
                break
            else:
                z+=1
        x.append(z)
    return x



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
hiper_tn = 50
hiper_ns = 50
hiper_p = 0.6
dist_hipergeometrica = []

#Definir parametros de la distribucion Poisson
poisson_p = 10
dist_poisson = []

#Definir parametros de la distribucion Empirica
em_sample = [0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
dist_empirica = []


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



#graficar(dist_normal, dist_uniforme, dist_exponencial, dist_gamma, dist_pascal, dist_binomial, dist_hipergeometrica, dist_poisson);

for j in range(10):
    for i in range(100):
        dist_uniforme.append(uniform(uni_a, uni_b))
        dist_exponencial.append(exponential(ex_ex))
        dist_gamma.append(gamma(gamma_k, gamma_alpha))
        dist_normal.append(normal(nor_ex, nor_stdx))
        dist_pascal.append(pascal(pas_k, pas_q))
        dist_binomial.append(binomial(bin_n, bin_p))
        dist_hipergeometrica.append(hypergeometric(hiper_tn, hiper_ns, hiper_p))
        dist_poisson.append(poisson(poisson_p))

    #test de Kolmogorov Smirnov

    p_uniforme = []
    uniforme_gen = np.random.uniform(1, 4, 100)
    stats, p = kstest(uniforme_gen, dist_uniforme)
    p_uniforme.append(p)

    p_exponencial= []
    exponencial_gen = np.random.exponential(7, 100)
    stats, p = kstest(exponencial_gen, dist_exponencial)
    p_exponencial.append(p)

    p_gamma = []
    gamma_gen = np.random.gamma(10,3, 100)
    stats, p = kstest(gamma_gen, dist_gamma)
    p_gamma.append(p)

    p_normal = []
    normal_gen = np.random.normal(2.5, 25, 100)
    stats, p = kstest(normal_gen, dist_normal)
    p_normal.append(p)

    p_pascal = []
    pascal_gen = np.random.negative_binomial(4, 0.8, 100)
    stats, p = kstest(pascal_gen, dist_pascal)
    p_pascal.append(p)

    p_binomial = []
    binomial_gen = np.random.binomial(100, 0.5, 100)
    stats, p = kstest(binomial_gen, dist_binomial)
    p_binomial.append(p)

    p_hipergeometrica = []
    hipergeometrica_gen = np.random.hypergeometric(50,50,100,100)
    stats, p = kstest(hipergeometrica_gen, dist_hipergeometrica)
    p_hipergeometrica.append(p)

    p_poisson= []
    poisson_gen = np.random.poisson(10, 100)
    stats,p =kstest(poisson_gen,dist_poisson)
    p_poisson.append(p)

for j in range(10):
    dist_empirica = empirica(em_sample)
    empirica_gen = np.random.normal(0,1,100)
    normalized_empirica = dist_empirica/np.linalg.norm(dist_empirica)
    stats,p =kstest(empirica_gen,normalized_empirica)
    print(p)


