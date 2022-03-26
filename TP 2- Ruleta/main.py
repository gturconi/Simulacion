import random as ran
import statistics
import matplotlib.pyplot as plt

# tipos_apuesta = {0:"Rojo",1:"Negro",2:"Par",3:"Impar",4:"Pasa",5:"Falta",6:"Docena 1",7:"Docena 2",
#                 8:"Docena 3",9:"Columna 1",10:"Columna 2",11:"Columna 3",12:"Docenas 1 y 2",13:"Docenas 2 y 3",
#                14:"Columnas 1 y 2",15:"Columnas 2 y 3",16:"Seisena 1",17:"Seisena 2",18:"Seisena 3",
#                19:"Seisena 4",20:"Seisena 5",21:"Seisena 6",22:"Seisena 7",23:"Seisena 8",24:"Seisena 9",
#                25:"Seisena 10",26:"Seisena 11",}


if __name__ == "__main__":
    rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    variables = (500,1,0)


    def constante(n, len):
        numeros = []
        for i in range(len):
            numeros.append(n)
        return numeros


    def graficar(list1, list2, msg1, msg2):
        plt.plot(list1)
        plt.plot(list2)
        plt.xlabel(msg1)
        plt.ylabel(msg2)
        plt.show()

    def martingala(valor, caja, apuesta,aciertos):
        if (valor in negros):
            caja = caja + apuesta
            aciertos = aciertos + 1
        else:
            caja = caja - apuesta
            apuesta *= 2;
        return caja, apuesta, aciertos


    cte_caja = constante(500, 20)
    frecs_corridas = []

    for i in range(1):
        numerosTirada = []
        flujoCaja = []
        for j in range(20):
            tirada = ran.randint(0, 36)
            flujoCaja.append(variables[0])
            numerosTirada.append(tirada)
            variables = martingala(tirada, variables[0], variables[1],variables[2])
            print("Tirada número: ", i + 1, "Valor: ", tirada, "Caja: ", variables[0],"Apuesta:", variables[1] ,"Aciertos: ",variables[2])
            frecs_corridas.append(variables[2]/(j+1))
        graficar(flujoCaja, cte_caja, "n(numero de tiradas)", "cc(cantidad de capital)")