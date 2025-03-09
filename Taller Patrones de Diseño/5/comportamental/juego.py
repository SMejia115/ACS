class Juego:
    def __init__(self):
        self._nombre = ""
        self._checkpoint = 0

    def get_checkpoint(self) -> int:
        return self._checkpoint

    def set_checkpoint(self, checkpoint: int):
        self._checkpoint = checkpoint

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def __str__(self) -> str:
        return f"Juego [nombre={self._nombre}, checkpoint={self._checkpoint}]"
