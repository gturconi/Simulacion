

  # semilla recomendada: 4798373

from PIL import Image
import numpy as np
import pylab as plt






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
        bitmap(u)

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
        bitmap(np.reshape(u, (255, 255)))

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
        bitmap(numbers)

def bitmap(values):
    plt.imshow(values, cmap='gray', interpolation='nearest')
    plt.show()



if __name__ == "__main__":
    rand = Rand(65025,4798373)
    rand.rand()











