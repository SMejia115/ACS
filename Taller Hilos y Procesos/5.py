# Cree un hilo que genere números aleatorios entre 1 y 100 y los inserte en una lista, y otro que
# recorra circularmente esa lista y sustituya los números terminados en 0 por el valor -1. Un tercer hilo abortará
# los otros dos en el momento en que la suma de los elementos de la lista supere el valor de 20000.

import threading
import random
import time

lista = []
lock = threading.Lock()
stop_event = threading.Event()

def generar_numeros():
    while not stop_event.is_set():
        with lock:
            lista.append(random.randint(1, 100))
        time.sleep(0.1)

def reemplazar_terminados_en_cero():
    while not stop_event.is_set():
        with lock:
            for i in range(len(lista)):
                if lista[i] % 10 == 0:
                    lista[i] = -1
        time.sleep(0.1)

def monitor_lista():
    while not stop_event.is_set():
        with lock:
            if sum(lista) > 20000:
                stop_event.set()
        time.sleep(0.1)

hilo_generador = threading.Thread(target=generar_numeros)
hilo_reemplazo = threading.Thread(target=reemplazar_terminados_en_cero)
hilo_monitor = threading.Thread(target=monitor_lista)

hilo_generador.start()
hilo_reemplazo.start()
hilo_monitor.start()

hilo_generador.join()
hilo_reemplazo.join()
hilo_monitor.join()

print("Proceso finalizado. Suma de la lista excedió 20000.")
