from abc import ABC, abstractmethod

# Clase abstracta AlgoritmoInventario (Interfaz)
class AlgoritmoInventario(ABC):
    @abstractmethod
    def optimizar_inventario(self, datos):
        pass

# Implementación de diferentes estrategias de optimización
class FIFO(AlgoritmoInventario):
    def optimizar_inventario(self, datos):
        return f"Optimizando inventario con FIFO: {datos}"

class LIFO(AlgoritmoInventario):
    def optimizar_inventario(self, datos):
        return f"Optimizando inventario con LIFO: {datos}"

class JIT(AlgoritmoInventario):
    def optimizar_inventario(self, datos):
        return f"Optimizando inventario con JIT (Just In Time): {datos}"

# Fábrica de Algoritmos de Inventario
class FabricaAlgoritmos:
    @staticmethod
    def get_algoritmo(tipo):
        algoritmos = {
            "FIFO": FIFO(),
            "LIFO": LIFO(),
            "JIT": JIT()
        }
        return algoritmos.get(tipo, None)

# Contexto para gestionar la estrategia seleccionada
class GestionInventario:
    def __init__(self, algoritmo: AlgoritmoInventario):
        self._algoritmo = algoritmo

    def set_algoritmo(self, nuevo_algoritmo: AlgoritmoInventario):
        self._algoritmo = nuevo_algoritmo

    def ejecutar_optimizacion(self, datos):
        return self._algoritmo.optimizar_inventario(datos)

# Función principal para interactuar con el usuario
def main():
    print("Seleccione un algoritmo de inventario: FIFO, LIFO, JIT")
    opcion_usuario = input("Ingrese el tipo de algoritmo: ").strip().upper()
    
    algoritmo = FabricaAlgoritmos.get_algoritmo(opcion_usuario)
    if not algoritmo:
        print("Algoritmo no soportado.")
        return
    
    contexto = GestionInventario(algoritmo)
    datos_inventario = "Stock de productos"
    resultado = contexto.ejecutar_optimizacion(datos_inventario)
    print(resultado)

if __name__ == "__main__":
    main()