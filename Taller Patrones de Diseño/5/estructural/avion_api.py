class AvionAPI:
    def buscar_vuelos(self, fecha_ida: str, fecha_vuelta: str, origen: str, destino: str):
        print("==============================")
        print(f"Vuelos encontrados para {destino} desde {origen}")
        print(f"Fecha IDA: {fecha_ida} Fecha Vuelta: {fecha_vuelta}")
        print("==============================")