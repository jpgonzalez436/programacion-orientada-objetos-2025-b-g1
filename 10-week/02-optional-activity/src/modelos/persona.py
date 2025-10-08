class Persona:
    def __init__(self, nombre: str, documento: str):
        self.nombre = nombre
        self.documento = documento

    def presentarse(self) -> str:
        return f"Soy {self.nombre} ({self.documento})."

