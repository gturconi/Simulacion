

# semilla recomendada: 4798373
#Otras semillas: 1257787
from random import random


import numpy as np
import pylab as plt
import scipy
from statsmodels.sandbox.stats.runs import runstest_1samp
import math







class Randu:
    def __init__(self, n, seed):
        self.n=n
        self.seed=seed

    def randu(self):
        x = [0 for _ in range(self.n)]
        u = [0 for _ in range(self.n)]
        x[0] = self.seed  # semilla
        u[0] = x[0] / (2 ** 31 - 1)  # transformamos al (0, 1)


        for i in range(1, self.n):
            x[i] = ((2 ** 16 + 3) * x[i - 1]) % (2 ** 31)
            u[i] = x[i] / (2 ** 31)

        for i in range(1, self.n):
            print("Valor", x[i])
            print("Normalizacion", u[i])
        #testPoker(u)
        #chisq_test(u)
        #testArribaAbajo(u)
        #testCorridas(u)
        #runTest(u)
        bitmap(np.reshape(u, (500, 500)))


class Rand:
    def __init__(self, n, seed):
        self.n=n
        self.seed=seed

    def rand(self):
        x = [0 for _ in range(self.n)]
        u = [0 for _ in range(self.n)]
        x[0] = self.seed  # semilla
        u[0] = x[0] / (2 ** 31 - 1)  # transformamos al (0, 1)

        for i in range(1, self.n):
            x[i] = (7 ** 5 * x[i - 1]) % (2 ** 31 - 1)
            u[i] = x[i] / (2 ** 31 - 1)

        for i in range(1, self.n):
            print("Valor", x[i])
            print("Normalizacion", u[i])
        bitmap(np.reshape(u, (1000, 1000)))

class Square:
    def __init__(self, n, seed):
        self.n=n
        self.seed=seed

    def mid_square(self):
        seeds = [0 for _ in range(self.n)]
        x = [0 for _ in range(self.n)]
        numbers = [0 for _ in range(self.n)]

        value = self.seed
        for i in range(0, self.n):
            x[i] = value ** 2
            string = str(x[i])
            l = len(string)
            if l < 8:
                for j in range(0, 8-l):
                    string = '0' + string
            seeds[i] = string[2:6]
            value = int(seeds[i])
            numbers[i] = '0.' + seeds[i]
            print("Valor" , x[i])
            print("Semilla", int(seeds[i]))
            print("Numero", float(numbers[i]))
        numbers = np.array(numbers, dtype=np.float32)
        bitmap(np.reshape(numbers.astype(np.float64), (1000, 1000)))

def randomTest():
    z = np.random.random((1000, 1000))  # Test data
    bitmap(z)

def bitmap(values):
    plt.imshow(values, cmap='gray', interpolation='nearest')
    plt.show()

#Perform Runs test
def runTest(data):
    print(runstest_1samp(data, correction=False))

def chisq_test(data):
    hi2, p, dof, expected = scipy.stats.chi2_contingency(data)
    print(hi2,p,dof)


def testArribaAbajo(p):
      print("Test arriba y abajo : ")
      x = []
      corridas = 1
      contmas = 0
      contmenos = 0
      u = []

      for i in range(len(p) - 1):
          u.append(float(p[i]))
      med = np.mean(u)

      for i in range(len(u)):
          if u[i] >= med:
              x.append("+")
          elif (u[i] < med):
              x.append("-")

      for i in range(1, len(x)):
          if (x[i] != x[i - 1]):
              corridas += 1

      if (x[0] == "+"):
          contmas += 1
      else:
          contmenos += 1
      for i in range(1, len(x)):
          if (x[i] == "+"):
              contmas += 1
          else:
              contmenos += 1

      n = contmas + contmenos
      media = ((2 * contmenos * contmas) / (contmas + contmenos)) + 1
      desviacion = math.sqrt(((2 * contmenos * contmas * (2 * contmas * contmenos - n)) / ((n ** 2) * (n - 1))))
      z = (corridas - media) / desviacion
      print("Z <=" + str(z))

def pokerSuma(observado, esperado):
  return (((observado - esperado) ** 2) / esperado)

def pokerCaracteres(u):
	distintos = 0
	dosIguales = 0
	tresIguales = 0
	for i in range(len(u)):
		c = str(u[i])
		if(c[2] != c[3] and c[2] != c[4] and c[3] != c[4]):
			distintos += 1
		elif(c[2] == c[3] and c[2] == c[4] and c[3] == c[4]):
			tresIguales += 1
		else:
			dosIguales += 1
	return distintos,dosIguales,tresIguales

def pokerSuma(observado,esperado):
	return(((observado-esperado)**2)/esperado)


def testPoker(u):
    print("Test de Poker")
    x = []
    y = []
    z = []
    distintosEsperado = 0.72
    dosIgualesEsperado = 0.09
    tresIgualesEsperado = 0.01

    distintos, dosIguales, tresIguales = pokerCaracteres(u)

    totalDistintos = pokerSuma(distintos/(255*255), distintosEsperado)
    totalDosIguales = pokerSuma(dosIguales/(255*255), dosIgualesEsperado)
    totalTresIguales = pokerSuma(tresIguales/(255*255), tresIgualesEsperado)
    x2 = totalDistintos + totalDosIguales + totalTresIguales
    print("X2 = " + str(x2))

def testCorridas(u):
	print("Test de Corridas: ")
	x = []
	a = 1
	for i in range(len(u)-1):
		if u[i+1] >= u[i]:
			x.append("+")
		elif(u[i+1] < u[i]):
			x.append("-")

	for i in range(1, len(x)):
		if (x[i] != x[i-1]):
			a += 1
	n = len(x)
	media = (2*n-1)/3
	desviacion = math.sqrt((16*n-29)/90)
	z = (a-media)/desviacion
	print("Z <= "+ str(z))





if __name__ == "__main__":
    rand = Randu(500*500,1257787)
    rand.randu()
    #sq = Square(1000*1000,5678)
    #sq.mid_square()
    decimalFractions = " "
    #print(array.split())


