from datetime import datetime, timedelta
import time
import uuid
import random
from concurrent.futures import ThreadPoolExecutor


class OrdersManager:
    def __init__(self, quantity=1_000, max_workers=10):
        self.__orders = [(uuid.uuid4(), x) for x in range(quantity)]
        self.__orders_processed = 0
        self.__last_printed_log = datetime.now()
        self.__max_workers = max_workers
        self.__log(f"{len(self.__orders)} orders generated...")

    def __log(self, message):
        print(f"{datetime.now()} > {message}")

    def __fake_save_on_db(self, order):
        id, number = order
        time.sleep(random.uniform(0, 1))  # Simula el tiempo de guardado en DB
        self.__orders_processed += 1
        
        if datetime.now() > self.__last_printed_log:
            self.__last_printed_log = datetime.now() + timedelta(seconds=5)
            self.__log(
                f"Total orders executed: {self.__orders_processed}/{len(self.__orders)}"
            )
        return f"Order [{id}] {number} was successfully processed."

    def process_orders(self):
        with ThreadPoolExecutor(max_workers=self.__max_workers) as executor:
            list(executor.map(self.__fake_save_on_db, self.__orders))


# ---
orders_manager = OrdersManager(quantity=1_000, max_workers=1000)

start_time = time.time()
orders_manager.process_orders()
delay = time.time() - start_time

print(f"{datetime.now()} > Tiempo de ejecucion: {delay:.2f} segundos...")