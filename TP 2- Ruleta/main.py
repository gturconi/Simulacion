import random as ran
import statistics
import matplotlib.pyplot as plt

caja = [50]
apuesta = [1]
#tipos_apuesta = {0:"Rojo",1:"Negro",2:"Par",3:"Impar",4:"Pasa",5:"Falta",6:"Docena 1",7:"Docena 2",
#                 8:"Docena 3",9:"Columna 1",10:"Columna 2",11:"Columna 3",12:"Docenas 1 y 2",13:"Docenas 2 y 3",
 #                14:"Columnas 1 y 2",15:"Columnas 2 y 3",16:"Seisena 1",17:"Seisena 2",18:"Seisena 3",
 #                19:"Seisena 4",20:"Seisena 5",21:"Seisena 6",22:"Seisena 7",23:"Seisena 8",24:"Seisena 9",
 #                25:"Seisena 10",26:"Seisena 11",}

rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]


class Tirada:
    def __init__(self, numeros):
        self.numeros = numeros

class Martingala():


for i in range(1):
    numerosTirada = []
    for j in range(1000):
        numerosTirada.append(ran.randint(0, 36))
     

def fibonacci(valor, apuesta):
    if valor:
        caja[0] += apuesta
        serie = [1, 1]
        while (True):
            serie.append(serie[0] + serie[1]) 
            serie.pop(0)
            if (serie[0] == apuesta) :
                break
    else:
        caja[0] -= apuesta
        serie = [0, 1]
    return (serie[1])

   
   
def testear():
    while (True):
        if (randint(0, 1) == 1):
            resultado = True
        else: 
            resultado = False
        apuesta[0] = fibonacci(resultado, apuesta[0])
        print("Resultado", resultado,". Apuesta:", apuesta[0], " . Caja:", caja[0])
        rta = input("Jugar de nuevo?: ")
        if (rta != "s"):
            break   
