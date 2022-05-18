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


def graficar(list1, list2, msg1, msg2):
    plt.plot(list1)
    plt.plot(list2)
    plt.xlabel(msg1)
    plt.ylabel(msg2)
    plt.show()


def funcionPromedio(l):
    promedios = []
    for i in range(len(l)):
        promedios.append(stat.mean(l[:i + 1]))
    return promedios

def funcionDesvio(l):
    desvios = []
    for i in range(len(l)):
        desvios.append(stat.stdev(l[:i + 2]))
    return desvios

def funcionVariancia(l):
    variancias = []
    for i in range(len(l)):
        variancias.append(stat.variance(l[:i + 2]))
    return variancias

def graficarCorridas(list1, list2,msg1,msg2):
  plt.plot(list2)
  plt.xlabel(msg1)
  plt.ylabel(msg2)
  for i in range(len(list1)):
      plt.plot(list1[i])
  plt.show()


#Con estos arrays vamos guardando los estadisticos de cada corrida

frecs_corridas = []
proms_corridas = []
desvios_corridas = []
variancias_corridas = []


cte_frec = constante(1 / 37,3000)
cte_prom = constante(18,3000)
cte_desvios = constante(10.68, 3000)
cte_variancias = constante(112, 3000)

for i in range(5):
    numerosTirada = []
    for j in range(3000):
        numerosTirada.append(ran.randint(0, 36))

    frecs = funcionFrecuencia(numerosTirada, 8)
    frecs_corridas.append(frecs)

    proms = funcionPromedio(numerosTirada)
    proms_corridas.append(proms)

    desvios = funcionDesvio(numerosTirada)
    desvios_corridas.append(desvios)

    variancias = funcionVariancia(numerosTirada)
    variancias_corridas.append(variancias)

    if(i==1): #estamos en la primera corrida
        # Frecuencia relativa
        graficar(frecs,cte_frec,"n(numero de tiradas)","fr(frecuencia relativa)")

        # Promedio
        graficar(proms,cte_prom,"n(numero de tiradas)","vp(valor promedio de las tiradas)")

        # Desvio
        graficar(desvios,cte_desvios,"n(numero de tiradas)","vd(valor del desvio)")

        # Variancia
        graficar(variancias, cte_variancias, "n(numero de tiradas)", "vd(valor de la variancia)")

    tirada = Tirada(numerosTirada, stat.mean(numerosTirada), stat.variance(numerosTirada), stat.stdev(numerosTirada),
                    rel_freq(numerosTirada, 8))
    arrayTiradas.append(tirada)
    print("Tirada número: ", i + 1, ". Promedio: ", tirada.promedio, ". Varianza: ", tirada.varianza, ". Desvío: ",
          tirada.desvio, "Frec. Rel del 8:", tirada.frecuencia, ".")

graficarCorridas(frecs_corridas,cte_frec,"n(numero de tiradas)","fr(frecuencia relativa)")
graficarCorridas(proms_corridas,cte_prom,"n(numero de tiradas)","vp(valor promedio de las tiradas)")
graficarCorridas(desvios_corridas,cte_desvios,"n(numero de tiradas)","vd(valor del desvio)")
graficarCorridas(variancias_corridas,cte_variancias,"n(numero de tiradas)","vd(valor de la variancia)")
