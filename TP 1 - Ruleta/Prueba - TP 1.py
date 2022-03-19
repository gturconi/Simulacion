import random as ran
import statistics as stat
import matplotlib.pyplot as plt


class Tirada:
    def __init__(self, numeros, promedio, varianza, desvio, frecuencia):
        self.numeros = numeros
        self.promedio = promedio
        self.varianza = varianza
        self.desvio = desvio
        self.frecuencia = frecuencia


def rel_freq(l, x):
    return l.count(x) / len(l);


arrayTiradas = []


def constante(n, len):
    numeros = []
    for i in range(len):
        numeros.append(n)
    return numeros


def funcionFrecuencia(l, x):
    frecuencias = []
    for i in range(len(l)):
        frecuencias.append(rel_freq(l[:i + 1], x))
    return frecuencias


def graficarFrecuencia(list1, list2):
    plt.plot(list1)
    plt.plot(list2)
    plt.xlabel("n(numero de tiradas)")
    plt.ylabel("fr(frecuencia relativa)")
    plt.show()

for i in range(20):
    numerosTirada = []
    for j in range(1000):
        numerosTirada.append(ran.randint(0, 36))
    tirada = Tirada(numerosTirada, stat.mean(numerosTirada), stat.variance(numerosTirada), stat.stdev(numerosTirada),
                    rel_freq(numerosTirada, 8))
    if(i==1): #estamos en la primera corrida
        frecs = funcionFrecuencia(numerosTirada, 8)
        cte = constante(1 / 37,len(numerosTirada))
        graficarFrecuencia(frecs,cte)
    arrayTiradas.append(tirada)
    print("Tirada número: ", i + 1, ". Promedio: ", tirada.promedio, ". Varianza: ", tirada.varianza, ". Desvío: ",
          tirada.desvio, "Frec. Rel del 8:", tirada.frecuencia, ".")

