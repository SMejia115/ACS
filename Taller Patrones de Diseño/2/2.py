from abc import ABC, abstractmethod
from datetime import datetime

# Clase Producto
class Producto:
    def __init__(self, nombre: str, precio_contado: float):
        self.nombre = nombre
        self.precio_contado = precio_contado

# Interfaz/Clase abstracta TarjetaCredito
class TarjetaCredito(ABC):
    @abstractmethod
    def calcular_intereses(self, precio: float, cuotas: int, banco: str) -> float:
        pass

# Clase TarjetaVisa
class TarjetaVisa(TarjetaCredito):
    def calcular_intereses(self, precio: float, cuotas: int, banco: str) -> float:
        dia_semana = datetime.today().strftime("%A")  # Obtener el día de la semana
        if dia_semana == "Lunes":  # Lunes
            interes = precio * 0.05
        else:
            interes = precio * 0.07
        return interes

# Clase TarjetaMastercard
class TarjetaMastercard(TarjetaCredito):
    def calcular_intereses(self, precio: float, cuotas: int, banco: str) -> float:
        if banco == "BancoX":
            interes = precio * 0.06
        else:
            interes = precio * 0.08
        return interes

# Clase TarjetaAmericanExpress
class TarjetaAmericanExpress(TarjetaCredito):
    def calcular_intereses(self, precio: float, cuotas: int, banco: str) -> float:
        interes_base = precio * 0.09
        if cuotas > 6:
            interes = interes_base + (precio * 0.02)
        else:
            interes = interes_base
        return interes

# Clase ProcesadorPago (Contexto)
class ProcesadorPago:
    def __init__(self, tarjeta: TarjetaCredito):
        self._tarjeta = tarjeta

    def establecer_tarjeta(self, nueva_tarjeta: TarjetaCredito):
        self._tarjeta = nueva_tarjeta

    def calcular_precio_final(self, producto: Producto, cuotas: int, banco: str):
        interes = self._tarjeta.calcular_intereses(producto.precio_contado, cuotas, banco)
        precio_total = producto.precio_contado + interes
        monto_cuota = precio_total / cuotas
        return precio_total, monto_cuota

# Simulación de interacción con el usuario
def main():
    # Lista de productos de ejemplo
    productos = {
        "1": Producto("Laptop", 2000),
        "2": Producto("Smartphone", 1000),
        "3": Producto("Tablet", 800)
    }

    tarjetas = {
        "1": TarjetaVisa(),
        "2": TarjetaMastercard(),
        "3": TarjetaAmericanExpress()
    }

    print("Seleccione un producto:")
    for key, prod in productos.items():
        print(f"{key}: {prod.nombre} - ${prod.precio_contado}")
    producto_seleccionado = input("Ingrese el número del producto: ")

    print("\nSeleccione una tarjeta:")
    print("1: Visa")
    print("2: Mastercard")
    print("3: American Express")
    tarjeta_seleccionada = input("Ingrese el número de la tarjeta: ")

    cuotas = int(input("\nIngrese la cantidad de cuotas: "))
    banco = input("Ingrese el banco emisor de la tarjeta: ")

    if producto_seleccionado in productos and tarjeta_seleccionada in tarjetas:
        procesador = ProcesadorPago(tarjetas[tarjeta_seleccionada])
        precio_total, monto_cuota = procesador.calcular_precio_final(productos[producto_seleccionado], cuotas, banco)
        
        print("\nResumen del pago:")
        print(f"Precio al contado: ${productos[producto_seleccionado].precio_contado:.2f}")
        print(f"Precio total en cuotas: ${precio_total:.2f}")
        print(f"Monto por cuota: ${monto_cuota:.2f}")
    else:
        print("Selección inválida.")

if __name__ == "__main__":
    main()
