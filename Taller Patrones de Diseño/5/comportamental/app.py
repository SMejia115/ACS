from caretaker import Caretaker
from juego import Juego
from originator import Originator

if __name__ == "__main__":
    nombre_juego = "Crash Bandicoot"

    juego = Juego()
    juego.set_nombre(nombre_juego)
    juego.set_checkpoint(1)

    caretaker = Caretaker()
    originator = Originator()

    juego = Juego()
    juego.set_nombre(nombre_juego)
    juego.set_checkpoint(2)
    originator.set_estado(juego)

    juego = Juego()
    juego.set_nombre(nombre_juego)
    juego.set_checkpoint(3)
    originator.set_estado(juego)

    caretaker.add_memento(originator.guardar())  # ESTADO POSICIÓN 0

    juego = Juego()
    juego.set_nombre(nombre_juego)
    juego.set_checkpoint(4)

    originator.set_estado(juego)
    caretaker.add_memento(originator.guardar())  # ESTADO POSICIÓN 1

    juego = Juego()
    juego.set_nombre(nombre_juego)
    juego.set_checkpoint(5)
    originator.set_estado(juego)
    caretaker.add_memento(originator.guardar())  # ESTADO POSICIÓN 2

    originator.set_estado(juego)
    originator.restaurar(caretaker.get_memento(2))

    juego = originator.get_estado()
    print(juego)
