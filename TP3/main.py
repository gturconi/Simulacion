

  # semilla recomendada: 4798373
  #Otras semillas: 1257787

from PIL import Image
import numpy as np
import pylab as plt
from statsmodels.sandbox.stats.runs import runstest_1samp







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
        runTest(u)
        #bitmap(np.reshape(u, (1000, 1000)))

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

def uniformTest():
    z = []
    for i in range(65025):
        z.append(np.random.uniform((1000, 1000))[0])
    bitmap(np.reshape(z, (1000, 1000)))

def bitmap(values):
    plt.imshow(values, cmap='gray', interpolation='nearest')
    plt.show()

#Perform Runs test
def runTest(data):
    print(runstest_1samp(data, correction=False))


if __name__ == "__main__":
    #uniformTest()
    rand = Randu(255*255,1257787)
    rand.randu()











