from abc import ABC, abstractmethod

# Clase abstracta EstrategiaOrdenacion
class EstrategiaOrdenacion(ABC):
    @abstractmethod
    def ordenar(self, lista, ascendente: bool):
        pass

# Clase Burbuja que extiende EstrategiaOrdenacion
class Burbuja(EstrategiaOrdenacion):
    def ordenar(self, lista, ascendente: bool):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if (lista[j] > lista[j+1]) != ascendente:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

# Clase QuickSort que extiende EstrategiaOrdenacion
class QuickSort(EstrategiaOrdenacion):
    def ordenar(self, lista, ascendente: bool):
        if len(lista) <= 1:
            return lista
        pivot = lista[len(lista) // 2]
        izquierda = [x for x in lista if (x < pivot) != ascendente]
        medio = [x for x in lista if x == pivot]
        derecha = [x for x in lista if (x > pivot) != ascendente]
        return self.ordenar(izquierda, ascendente) + medio + self.ordenar(derecha, ascendente)

# Clase InsertSort que extiende EstrategiaOrdenacion
class InsertSort(EstrategiaOrdenacion):
    def ordenar(self, lista, ascendente: bool):
        for i in range(1, len(lista)):
            clave = lista[i]
            j = i - 1
            while j >= 0 and (lista[j] > clave) != ascendente:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = clave
        return lista

# Clase ContextoOrdenacion
class ContextoOrdenacion:
    def __init__(self, estrategia: EstrategiaOrdenacion):
        self._estrategia = estrategia

    def setEstrategia(self, estrategia: EstrategiaOrdenacion):
        self._estrategia = estrategia

    def ejecutarOrdenacion(self, lista, ascendente: bool):
        return self._estrategia.ordenar(lista, ascendente)

# Función principal para interactuar con el usuario
def main():
    algoritmos = {
        '1': Burbuja(),
        '2': QuickSort(),
        '3': InsertSort()
    }

    print("Seleccione el algoritmo de ordenación:")
    print("1: Bubble Sort")
    print("2: Quick Sort")
    print("3: Insertion Sort")
    choice = input("Ingrese el número correspondiente: ")

    order = input("Orden ascendente (si/no)? ").strip().lower() == "si"
    
    data = list(map(int, input("Ingrese los números a ordenar separados por espacio: ").split()))

    if choice in algoritmos:
        contexto = ContextoOrdenacion(algoritmos[choice])
        sorted_data = contexto.ejecutarOrdenacion(data, order)
        print("Lista ordenada:", sorted_data)
    else:
        print("Selección no válida.")

if __name__ == "__main__":
    main()
