import random as ran
import statistics
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    variables = (50, 1, 0)


    def constante(n, len):
        numeros = []
        for i in range(len):
            numeros.append(n)
        return numeros


    def graficar(list1, list2, msg1, msg2,msg3):
        plt.plot(list1)
        plt.plot(list2)
        plt.xlabel(msg1)
        plt.ylabel(msg2)
        plt.title(msg3)
        plt.show()


    def graficar2(list, msg1, msg2):
        length = len(list)
        y_pos = np.arange(length)
        plt.bar(y_pos, list, color="b", width=0.25)

        list2 = []
        for i in range(length):
            list2.append(i + 1)
        plt.xticks(y_pos, list2)
        plt.ylabel(msg1)
        plt.title(msg2)
        plt.show()


    def martingala(valor, caja, apuesta, aciertos):
        if (valor in negros):
            caja = caja + apuesta
            aciertos = aciertos + 1
            apuesta = 1
        else:
            caja = caja - apuesta
            apuesta *= 2;
        return caja, apuesta, aciertos


    def fibonacci(valor, caja, apuesta, aciertos):
        if valor in negros:
            caja = caja + apuesta
            aciertos = aciertos + 1
            serie = [1, 1]
            while (True):
                serie.append(serie[0] + serie[1])
                serie.pop(0)
                if (serie[0] == apuesta):
                    break
        else:
            caja = caja - apuesta
            serie = [0, 1]
        return caja, serie[1], aciertos


    def dalembert(valor, caja, apuesta, aciertos):
        if valor in negros:
            caja = caja + apuesta
            aciertos = aciertos + 1
            if (apuesta > 1):
                apuesta = apuesta - 1
        else:
            caja = caja - apuesta
            apuesta = apuesta + 1
        return caja, apuesta, aciertos


    frecs_total_fibo = []
    flujoCaja_fibo = []
    frecs_total_martin = []
    flujoCaja_martin = []
    frecs_total_dalem = []
    flujoCaja_dalem = []

    funciones = [fibonacci, martingala, dalembert]
for i in range(5):
    for funcion in funciones:
        variables = (50, 1, 0)
        numerosTirada = []
        flujoCaja = []
        frecs_corridas = []
        flujoCaja.append(variables[0])
        j = 0
        while ((flujoCaja[j] > 0) and (j < 20)):
            tirada = ran.randint(0, 36)
            numerosTirada.append(tirada)
            variables = funcion(tirada, variables[0], variables[1], variables[2])
            flujoCaja.append(variables[0])
            print("Tirada número: ", funcion, "Valor: ", tirada, "Caja: ", variables[0], "Apuesta:", variables[1],
                  "Aciertos: ", variables[2], "Apuesta número", j + 1)
            frecs_corridas.append(variables[2] / (j + 1))
            j = j + 1
        if (i == 1):
            cte_caja = constante(50, len(flujoCaja))
            if (funcion == fibonacci):
                graficar(flujoCaja, cte_caja, "n(numero de tiradas)", "cc(cantidad de capital)","Flujo de caja Fibonacci")
                graficar2(frecs_corridas, "fr(frecuencia relativa)", "Frecuencia relativa de aciertos Fibonacci")
            elif (funcion == martingala):
                graficar(flujoCaja, cte_caja, "n(numero de tiradas)", "cc(cantidad de capital)", "Flujo de caja Martingala")
                graficar2(frecs_corridas, "fr(frecuencia relativa)", "Frecuencia relativa de aciertos Martingala")
            else:
                graficar(flujoCaja, cte_caja, "n(numero de tiradas)", "cc(cantidad de capital)","Flujo de caja Dalembert")
                graficar2(frecs_corridas, "fr(frecuencia relativa)", "Frecuencia relativa de aciertos Dalembert")
        if (funcion == fibonacci):
            flujoCaja_fibo.append(flujoCaja[j - 1])
            frecs_total_fibo.append(frecs_corridas[j - 1])
        elif(funcion == martingala):
            flujoCaja_martin.append(flujoCaja[j - 1])
            frecs_total_martin.append(frecs_corridas[j - 1])
        else:
            flujoCaja_dalem.append(flujoCaja[j - 1])
            frecs_total_dalem.append(frecs_corridas[j - 1])

graficar(flujoCaja_fibo, constante(50, 5), "n(numero de tiradas)", "cc(cantidad de capital)","Flujo de caja Fibonacci de cada corrida")
graficar2(frecs_total_fibo, "fr(frecuencia relativa)", "Frecuencia relativa de aciertos Fibonacci de cada corrida")
graficar(flujoCaja_martin, constante(50,5), "n(numero de tiradas)", "cc(cantidad de capital)","Flujo de caja Martingala de cada corrida")
graficar2(frecs_total_martin,"fr(frecuencia relativa)" ,"Frecuencia relativa de aciertos Martingala de cada corrida")
graficar(flujoCaja_dalem, constante(50,5), "n(numero de tiradas)", "cc(cantidad de capital)","Flujo de caja Dalembert de cada corrida")
graficar2(frecs_total_dalem,"fr(frecuencia relativa)" ,"Frecuencia relativa de aciertos Dalembert de cada corrida")

