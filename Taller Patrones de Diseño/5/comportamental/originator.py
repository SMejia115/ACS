from juego import Juego
from memento import Memento

class Originator:
    def __init__(self):
        self._estado = None

    def set_estado(self, estado: Juego):
        self._estado = estado

    def get_estado(self) -> Juego:
        return self._estado

    def guardar(self) -> Memento:
        return Memento(self._estado)

    def restaurar(self, memento: Memento):
        self._estado = memento.get_estado()
