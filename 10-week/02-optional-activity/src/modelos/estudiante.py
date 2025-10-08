from .persona import Persona

class Estudiante(Persona):

    def __init__(self, nombre: str, documento: str, codigo: str):
        super().__init__(nombre, documento) # llama al constructor de Persona
        self.codigo = codigo

    def presentarse(self) -> str: # Sobrescritura opcional
        base = super().presentarse()
        return base + f" Mi código es {self.codigo}."
