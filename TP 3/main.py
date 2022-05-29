
import math
import random
import math
import matplotlib.pyplot as plt
import numpy
import numpy as np
from scipy.stats import expon


 # def random_integer(prob_distrib): FALTA IMPLEMENTAR

sim_time = None;
inv_level = None;
time_last_event = None;
total_ordering_cost = 0;
area_holding = None;
area_shortage = None;
amount = None;
prob_distrib_demmand = None;
smalls = 15;
bigs = 30;
setup_cost = 2;
incremental_cost = None;
minlag = None;
maxlag = None;

avg_holding_cost= None;
avg_holding_cost_array= [];

avg_ordering_cost= None;
avg_ordering_cost_array = []

avg_shortage_cost= None;
avg_shortage_cost_array = []

total_cost = None;
total_cost_array = []

holding_cost = 2;
shortage_cost = 2;
num_delays_required = None;
num_custs_delayed = None;
total_of_delays = None;
time_since_last_event= None;
area_num_in_q = None;
num_in_q = None;
area_server_status = None;
server_status = None;
time_last_event = None;
min_time_next_event= None;
time= None;
next_event_type= None;
min_time_next_event= None;
time_next_event= None;
num_events= None;
num_policies = None;
num_months = 20;
initial_inv_level = 20


def graficar(list1, msg1, msg2):
    plt.plot(list1)
    plt.xlabel(msg1)
    plt.ylabel(msg2)
    plt.show()




def inicialize(mean_interdemand):
    global sim_time
    global inv_level
    global time_last_event
    global total_ordering_cost
    global area_holding
    global area_shortage
    global time_next_event  #
    global num_months

    sim_time = 0

    #inicializamos las variables de estado

    inv_level = initial_inv_level


    time_last_event = 0

    #inicializamos los contadores estadisticos

    total_ordering_cost = 0
    area_holding = 0
    area_shortage = 0

    #inicializamos la lista de eventos

    time_next_event = [0,0,0,0]

    time_next_event[0] = math.inf
    time_next_event[1] = float(sim_time + numpy.random.exponential(mean_interdemand))
    time_next_event[2] = num_months
    time_next_event[3] = 1

    #Me parece que no es la forma correcta de hacerlo, ademas no esta inicializado como tupla
    #time_next_event.insert(0, math.inf) #Arribo del prox pedido
    #time_next_event.insert(1, float(sim_time + expon(mean_interdemand))) #Arribo de un cliente
    #time_next_event.insert(2, num_months) #Final de la simulacion
    #time_next_event.insert(3, 0) #Evaluaciones de inventario


def order_arrival():
    global amount #
    global inv_level

    #incrementamos el nivel de inventario por la cantidad ordenada
    inv_level += amount

    #dado que ahora no hay ningun pedido pendiente, eliminamos el evento de llegada del pedido de consideracion
    #time_next_event.insert(0, 1*10**(30))
    time_next_event[0] = math.inf



def demand_size(D):
    #generamos un valor entre 0 y 1
    n = random.uniform(0, 1)
    if(n <= D[0]):
        return 1
    elif(n <= D[0] + D[1]):
        return 2
    elif (n <= D[0] + D[1] + D[2]):
        return 3
    elif (n <= D[0] + D[1] + D[2] + D[3]):
        return 4;

def demand(D,mean_interdemand):
    global prob_distrib_demmand #
    global inv_level
    global time_next_event
    global sim_time

    prob_distrib_demmand = [26] #
    cant = demand_size(D)
    inv_level -= cant
    #disminuimos el nivel de inventario por un tama�o de demanda generado
    #inv_level -= random_integer(prob_distrib_demmand)  #FALTA IMPLEMENTAR RANDOM INTEGER
    #programamos la hora de la proxima demanda
    time_next_event[1] = float(sim_time + numpy.random.exponential(mean_interdemand))
    print("Nuevo pedido de un cliente: ", cant)

def evaluate(fixed_cost):
    global smalls  #
    global bigs  #
    global setup_cost  #
    global incremental_cost  #
    global total_ordering_cost
    global minlag  #
    global maxlag  #
    global inv_level
    global amount


    if (inv_level < smalls):
        amount = bigs - inv_level
        #total_ordering_cost += setup_cost + incremental_cost + amount esta linea no se entiende lo que quiere hacer
        total_ordering_cost += amount * setup_cost + fixed_cost
        #avg_ordering_cost_array.append(total_ordering_cost / time_next_event[3])

        time_next_event[0] = float(sim_time + 0.5 + (1-0.5)*random.uniform(0, 1)) #Formula que vimos en clase
        #time_next_event.insert(0, sim_time + random.uniform(minlag, maxlag))
        time_next_event[3] += 1
        print("Se realizara un pedido porque el nivel de inventario es: ",inv_level)

    #time_next_event.insert(3, sim_time + 1)

def report(shortage_cost,num_months):
    global avg_holding_cost
    global avg_ordering_cost
    global avg_shortage_cost
    global num_delays_required  #
    global num_custs_delayed  #
    global total_of_delays  #
    global holding_cost


    #calculamos y escribimos estimaciones de las medidas deseadas de rendimiento
    avg_ordering_cost = total_ordering_cost / time_next_event[2]
    avg_holding_cost = holding_cost * area_holding / time_next_event[2]
    avg_shortage_cost = shortage_cost * area_shortage / time_next_event[2]
    total_cost = avg_ordering_cost + avg_holding_cost + avg_shortage_cost
    #avg_ordering_cost = total_ordering_cost / num_months
    #avg_holding_cost = holding_cost * area_holding / num_months
    #avg_shortage_cost = shortage_cost * area_shortage / num_months

    print("Costo promedio de orden: ", avg_ordering_cost)
    print("Costo promedio de mantenimiento: ", avg_holding_cost)
    print("Costo promedio de faltantes: ", avg_shortage_cost)
    print("Costo total: ", total_cost)

    graficar(avg_ordering_cost_array, "Tiempo(meses)", "Costo de orden")
    graficar(avg_shortage_cost_array, "Tiempo(meses)", "Costo de faltantes")
    graficar(avg_holding_cost_array, "Tiempo(meses)", "Costo de almacenamiento")

    # A estos me parece que no los pide
    #print("Promedio de clientes en el sistema: ", total_of_delays / num_custs_delayed)

    #print("Promedio de clientes en cola: ", area_num_in_q / sim_time)

    #print("Tiempo Promedio en el sistema: ", area_server_status / num_delays_required)

    #print("N�mero de retrasos completados: ", num_custs_delayed)

    #print("Utilizacion del servidor: ", area_server_status / sim_time)


def update_time_avg_stats():
    global time_since_last_event
    global area_num_in_q  #
    global num_in_q  #
    global area_server_status  #
    global server_status  #
    global time_last_event  #
    global area_holding
    global area_shortage
    global sim_time
    global inv_level
    global time_next_event
    global holding_cost
    global shortage_cost
    global total_ordering_cost

    #calculamos el tiempo desde el ultimo evento y actualizamos el marcador de tiempo del ultimo evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    if(inv_level < 0):
        area_shortage += (inv_level * time_since_last_event)*(-1)
        #area_shortage -= inv_level * time_since_last_event me parece que se deberia sumar en vez de restar
    elif(inv_level > 0 ):
        area_holding += inv_level * time_since_last_event
    avg_shortage_cost_array.append(shortage_cost * area_shortage / time_next_event[3])
    avg_holding_cost_array.append(holding_cost * area_holding / time_next_event[3])
    avg_ordering_cost_array.append(total_ordering_cost / time_next_event[3])

def timing():
    global min_time_next_event
    global sim_time
    global next_event_type
    global min_time_next_event
    global time_next_event
    global num_events


    min_time_next_event=1*10**(29)
    next_event_type=0
    for i in range(num_events):
        if(time_next_event[i]<min_time_next_event):
            min_time_next_event=time_next_event[i]
            next_event_type=i+1
    sim_time=min_time_next_event
    if(min_time_next_event == time_next_event[3]):
        time_next_event[3] +=1;
    if(time_next_event[3] == time_next_event[2]):
        next_event_type = 3



def inputValues():
    mean_interdemand = float(input("Media entre arribos: "))
    num_months = int(input("Numero de Meses: "))
    num_delays_required = int(input("Numero de clientes total: "))


if __name__ == "__main__":
    repetir_bucle = True;
    num_policies = 1 #Supongo que debe ser el numero de simulaciones
    num_events = 4 #esto qué hace? Encima nunca se usa jaja
    D = [1/6,1/3,1/3,1/6]
    for i in range(num_policies):
        inputValues()
        inicialize(0.5)
        repetir_bucle = True
        while repetir_bucle:
            # Determinamos el siguiente evento
            timing()
            # Actualizamos acumuladores estad�sticos de promedio de tiempo.
            update_time_avg_stats()
            # Invocamos la funci�n de evento apropiada
            if (next_event_type == 1):
                print("Llegada de mercaderia")
                order_arrival() #Cuando llega la mercaderia
            elif (next_event_type == 2):
                demand(D,0.5) # Cuando nos hacen un pedido
                print("Nos hicieron un pedido")
            elif (next_event_type == 4):
                evaluate(4) #Evaluacion de inventario
                print("Evaluacion de inventario")
            elif (next_event_type == 3):
                report(2,2)
            #repetir_bucle = (next_event_type <= 3)
            repetir_bucle = time_next_event[3] < time_next_event[2]


