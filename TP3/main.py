
  # semilla recomendada: 4798373

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



if __name__ == "__main__":
    square = Square(10,1931)
    square.mid_square()







