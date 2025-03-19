# Cree un hilo el que le pasaremos so números enteros, n1, n2, y escriba la secuencia compartida
# entre ambos números si n1<n2. Desde el hilo principal, muestre un mensaje con el resultado de
# la resta.

import threading

def secuencia_compartida(n1, n2):
    secuencia = [i for i in range(n1, n2 + 1)]
    print(f"Secuencia compartida: {secuencia}")

def calcular_resta(n1, n2):
    print(f"La resta (n2 - n1) es: {n2 - n1}")

if __name__ == "__main__":
    n1 = int(input("Ingrese el primer número (n1): "))
    n2 = int(input("Ingrese el segundo número (n2): "))
    
    if n1 < n2:
        hilo_secuencia = threading.Thread(target=secuencia_compartida, args=(n1, n2))
        hilo_resta = threading.Thread(target=calcular_resta, args=(n1, n2))
        
        hilo_secuencia.start()
        hilo_resta.start()
        
        hilo_secuencia.join()
        hilo_resta.join()
    else:
        print("El primer número debe ser menor que el segundo.")
