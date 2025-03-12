class Conexion:
    _instancia = None  # Variable de clase para almacenar la única instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Conexion, cls).__new__(cls)
        return cls._instancia

    def conectar(self):
        print("Me conecté a la BD")

    def desconectar(self):
        print("Me desconecté de la BD")


# Uso del Singleton
if __name__ == "__main__":
    c = Conexion()
    c.conectar()
    c.desconectar()

    c1 = Conexion()
    
    c2 = Conexion()
    print(c1 is c2)

    # Verificar si sigue siendo la misma instancia
    print(isinstance(c, Conexion)) 