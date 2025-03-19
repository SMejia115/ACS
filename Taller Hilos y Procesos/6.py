import threading
import random

class SumaHilo(threading.Thread):
    def __init__(self, id_hilo):
        super().__init__()
        self.id_hilo = id_hilo
        self.suma_total = 0

    def run(self):
        """Genera 100 números aleatorios y los suma."""
        numeros = [random.randint(1, 1000) for _ in range(100)]
        self.suma_total = sum(numeros)
        print(f"Hilo {self.id_hilo}: suma = {self.suma_total}")

def main():
    hilos = []
    resultados = []

    # Crear y ejecutar 10 hilos
    for i in range(1, 11):
        hilo = SumaHilo(i)
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
        resultados.append((hilo.id_hilo, hilo.suma_total))

    # Determinar el hilo ganador
    hilo_ganador = max(resultados, key=lambda x: x[1])
    print(f"\nEl hilo ganador es el {hilo_ganador[0]} con una suma de {hilo_ganador[1]}.")

if __name__ == "__main__":
    main()
