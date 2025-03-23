import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

lock = threading.Lock()  # Lock para protección adicional

class HiloProductor(threading.Thread):
    def __init__(self, name=None):
        super(HiloProductor, self).__init__()
        self.name = name

    def run(self):
        while True:
            item = random.randint(1, 10)
            q.put(item)  # Operación bloqueante, no requiere verificar si está llena
            logging.debug(f'Insertando "{item}" : {q.qsize()} elementos en la cola')
            time.sleep(random.random())

class HiloConsumidor(threading.Thread):
    def __init__(self, name=None):
        super(HiloConsumidor, self).__init__()
        self.name = name

    def run(self):
        while True:
            item = q.get()  # Operación bloqueante, no requiere verificar si está vacía
            logging.debug(f'Sacando "{item}" : {q.qsize()} elementos en la cola')
            time.sleep(random.random())

p = HiloProductor(name='productor')
p2 = HiloProductor(name='productor2')
c = HiloConsumidor(name='consumidor')

p.start()
p2.start()
c.start()