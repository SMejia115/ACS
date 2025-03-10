from check_facade import CheckFacade

if __name__ == "__main__":
    cliente1 = CheckFacade()
    cliente1.buscar("02/07/2018", "08/07/2018", "Lima", "Cancún")

    cliente2 = CheckFacade()
    cliente2.buscar("02/07/2018", "08/07/2018", "Lima", "Quito")
