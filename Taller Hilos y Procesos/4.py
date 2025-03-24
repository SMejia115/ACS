from datetime import datetime
import time
import uuid
import random
import threading
import logging
import queue

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s')

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

condition = threading.Condition()

class HiloProductor(threading.Thread):
    def __init__(self, name=None):
        super(HiloProductor, self).__init__()
        self.name = name

    def run(self):
        while True:
            item = random.randint(1, 10)
            with condition:  # Protección de la región crítica
                while q.full():  
                    condition.wait()  # Esperar si la cola está llena
                q.put(item)
                logging.debug(f'Insertando "{item}" : {q.qsize()} elementos en la cola')
                condition.notify()  # Despertar consumidores
            
            time.sleep(random.random())

class HiloConsumidor(threading.Thread):
    def __init__(self, name=None):
        super(HiloConsumidor, self).__init__()
        self.name = name

    def run(self):
        while True:
            with condition:  # Protección de la región crítica
                while q.empty():  
                    condition.wait()  # Esperar si la cola está vacía
                item = q.get()
                logging.debug(f'Sacando "{item}" : {q.qsize()} elementos en la cola')
                condition.notify()  # Despertar productores
            
            time.sleep(random.random())

# Creación y ejecución de hilos
p = HiloProductor(name='productor')
p2 = HiloProductor(name='productor2')
c = HiloConsumidor(name='consumidor')

p.start()
p2.start()
c.start()