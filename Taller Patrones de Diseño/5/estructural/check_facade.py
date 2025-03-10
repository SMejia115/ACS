from avion_api import AvionAPI
from hotel_api import HotelAPI

class CheckFacade:
    def __init__(self):
        self.avion_api = AvionAPI()
        self.hotel_api = HotelAPI()

    def buscar(self, fecha_ida: str, fecha_vuelta: str, origen: str, destino: str):
        self.avion_api.buscar_vuelos(fecha_ida, fecha_vuelta, origen, destino)
        self.hotel_api.buscar_hoteles(fecha_ida, fecha_vuelta, origen, destino)
