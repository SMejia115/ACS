# Modifique el código Eventos.py para permitir que, cuando la función genera_eventos() y haya
# completado todas sus iteraciones, se termine de forma genérica el programa. Intente a través del
# envío de señales mediante la clase Event.

import threading
import time

def genera_eventos():
    for _ in range(5):
        time.sleep(2)
        ev.set()
    fin.set()  # Señal para indicar que debe finalizar el otro hilo

def escribe_algo():
    while not fin.is_set():  # Verifica si se ha indicado finalizar
        ev.wait()
        if fin.is_set():  # Si se activa la señal de finalización, salir
            break
        print("hola")
        ev.clear()

# Creación de eventos
ev = threading.Event()
fin = threading.Event()

# Creación de hilos
T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

# Inicio de hilos
T1.start()
T2.start()

# Esperar a que terminen
T1.join()
T2.join()

print("El programa ha finalizado.")

