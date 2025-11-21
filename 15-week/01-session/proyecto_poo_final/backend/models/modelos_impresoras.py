"""Modelos simples para impresoras 3D y solicitudes de impresión."""

from dataclasses import dataclass


@dataclass
class Impresora3D:
    id: int
    codigo: str
    nombre: str
    estado: str = "DISPONIBLE"  # "DISPONIBLE" o "EN_USO"

    def esta_disponible(self) -> bool:
        return self.estado == "DISPONIBLE"


@dataclass
class SolicitudImpresion:
    id: int
    codigo_estudiante: str
    nombre_estudiante: str
    facultad: int              # 1 = Mecatrónica, 2 = Renovables, 3 = Industrial
    impresora_id: int
    fecha_impresion: str       # "dd/mm/aaaa"
    duracion_minutos: int
    material_gramos: int
    estado: str                # "PENDIENTE", "EN_CURSO", "FINALIZADA", "RECHAZADA"
    motivo_rechazo: str | None = None
