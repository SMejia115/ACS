from juego import Juego

class Memento:
    def __init__(self, estado: Juego):
        self._estado = estado

    def get_estado(self) -> Juego:
        return self._estado
