from .persona import Persona

class Docente(Persona):
    def __init__(self, nombre: str, documento: str, categoria: str):
        super().__init__(nombre, documento)
        self.categoria = categoria

def presentarse(self) -> str:
    return f"Prof. {self.nombre} ({self.categoria})"
