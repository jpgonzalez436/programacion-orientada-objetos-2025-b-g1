from modelos.estudiante import Estudiante
from modelos.persona import Persona
from modelos.docente import Docente

e = Estudiante("Ana", "CC 1001", "2025-001")
print(e.presentarse())

class Asistente:
    def permisos(self):
        return {"puede_tomar_asistencia": True}
    
class Monitor:
    def permisos(self):
        return {"puede_moderar_foro": True}
    
class EstudianteMonitor(Estudiante, Monitor, Asistente):
    pass

em = EstudianteMonitor("Luis", "CC 1002", "2025-002")
print(EstudianteMonitor.__mro__) # tupla con el orden de búsqueda
# Resolución de métodos:
print(em.permisos()) # Python usa el primer método encontrado según MRO


class HistorialAcademico:
    def __init__(self):
        self.notas = []

    def registrar(self, curso: str, nota: float):
        self.notas.append((curso, nota))

class EstudianteComposicion(Persona):
    def __init__(self, nombre: str, documento: str, codigo: str):
        super().__init__(nombre, documento)
        self.codigo = codigo
        self.historial = HistorialAcademico() # Composición: tiene-un historial