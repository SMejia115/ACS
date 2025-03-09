from memento import Memento

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento: Memento):
        self._mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self._mementos[index]