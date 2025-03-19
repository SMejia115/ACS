# 1. Plantee un algoritmo que calcule el área de la siguiente figura geométrica 
# descomponiendo en hilos para optimizar su ejecución.

import threading

# b = base, h = altura
# t = triangulo, r = rectangulo

t1_b = 10
t1_h = 12

t2_b = 2
t2_h = 5

r1_b = 8
r1_h = 12

r2_b = 6
r2_h = 5


areas = []
lock = threading.Lock()


def area_triangulo(base, altura):
    area = (base * altura) / 2
    with lock:
        areas.append(area)


def area_rectangulo(base, altura):
    area = base * altura
    with lock:
        areas.append(area)

def total_areas_hilos():
    t1 = threading.Thread(target=area_triangulo, args=(t1_b, t1_h))
    t2 = threading.Thread(target=area_triangulo, args=(t2_b, t2_h))
    r1 = threading.Thread(target=area_rectangulo, args=(r1_b, r1_h))
    r2 = threading.Thread(target=area_rectangulo, args=(r2_b, r2_h))
    
    # Iniciar los hilos
    t1.start()
    t2.start()
    r1.start()
    r2.start()
    
    # Esperar a que terminen los hilos
    t1.join()
    t2.join()
    r1.join()
    r2.join()
    
    # Sumar las áreas obtenidas
    total = sum(areas)
    print(f"El área total de la figura es {total}")


if __name__ == "__main__":
  total_areas_hilos()