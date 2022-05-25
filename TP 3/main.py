
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon


 # def random_integer(prob_distrib): FALTA IMPLEMENTAR



def inicialize():
    # inicializamos el reloj de simulacion
    global  sim_time

    #inicializamos las variables de estado
    global  inv_level
    global initial_inv_level
    global time_last_event

    #inicializamos los contadores estaditicos

    global total_ordering_cost
    global area_holding
    global area_shortage

    #inicializamos la lista de eventos
    global time_next_event #
    global mean_interdemand #
    global num_months #

    sim_time = 0

    inv_level = initial_inv_level
    time_last_event = 0

    total_ordering_cost = 0
    area_holding = 0
    area_shortage = 0

    time_next_event.insert(0, 1*10**(30))
    time_next_event.insert(1, float(sim_time + expon(mean_interdemand)))
    time_next_event.insert(2, num_months)
    time_next_event.insert(3, 0)

mean_interdemand = float( input("Media entre arribos: "))
num_months = int (input("Numero de Meses: "))
num_delays_required = int (input("Numero de clientes total: "))

def order_arrival():
    global amount #

    #incrementamos el nivel de inventario por la cantidad ordenada
    inv_level += amount

    #dado que ahora no hay ningun pedido pendiente, eliminamos el evento de llegada del pedido de consideracion
    time_next_event.insert(0, 1*10**(30))

def demand():
    global prob_distrib_demmand #
    prob_distrib_demmand = [26] #


    #disminuimos el nivel de inventario por un tamaño de demanda generado
    #inv_level -= random_integer(prob_distrib_demmand)  #FALTA IMPLEMENTAR RANDOM INTEGER

    #programamos la hora de la proxima demanda
    time_next_event.insert(1, sim_time + expon(mean_interdemand))

def evaluate():
    global smalls #
    global bigs #
    global setup_cost #
    global incremental_cost #
    global minlag #
    global maxlag #

    if (inv_level < smalls):
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + incremental_cost + amount
        time_next_event.insert(0, sim_time + random.uniform(minlag, maxlag))
    time_next_event.insert(3, sim_time + 1)

def report():
    #calculamos y escribimos estimaciones de las medidas deseadas de rendimiento
    global avg_holding_cost
    global avg_ordering_cost
    global avg_shortage_cost
    global holding_cost #
    global shortage_cost #
    global num_delays_required #
    global num_custs_delayed #
    global total_of_delays #

    avg_ordering_cost = total_ordering_cost / num_months
    avg_holding_cost = holding_cost * area_holding / num_months
    avg_shortage_cost = shortage_cost * area_shortage / num_months

    print("Promedio de clientes en el sistema: ", total_of_delays / num_custs_delayed)

    print("Promedio de clientes en cola: ", area_num_in_q / sim_time)

    print("Tiempo Promedio en el sistema: ", area_server_status / num_delays_required)

    print("Número de retrasos completados: ", num_custs_delayed)

    print("Utilizacion del servidor: ", area_server_status / sim_time)


def update_time_avg_stats():
    global time_since_last_event
    global area_num_in_q #
    global num_in_q #
    global area_server_status #
    global server_status #
    global time_last_event #

    #calculamos el tiempo desde el ultimo evento y actualizamos el marcador de tiempo del ultimo evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    if(inv_level < 0):
        area_shortage -= inv_level * time_since_last_event
    elif(inv_level > 0 ):
        area_holding += inv_level * time_since_last_event

def timing():

    global min_time_next_event
    global time
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
    time=min_time_next_event

def main():
    global num_events
    global num_policies
    global repetir_bucle

    num_events = 4
    for i in range(num_policies):
        inicialize()
        repetir_bucle = True
        while repetir_bucle:
            #Determinamos el siguiente evento
            timing()
            #Actualizamos acumuladores estadísticos de promedio de tiempo.
            update_time_avg_stats()
            #Invocamos la función de evento apropiada
            if (next_event_type == 1):
                order_arrival()
            elif (next_event_type == 2):
                demand()
            elif (next_event_type == 3):
                evaluate()
            elif (next_event_type == 4):
                report()
            repetir_bucle = (next_event_type != 3)

