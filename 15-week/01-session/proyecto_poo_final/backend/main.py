"""Punto de entrada del sistema de impresoras 3D del FABLAB."""

from models import Impresora3D, SolicitudImpresion, SistemaImpresoras3D
from models.menu_impresoras import ejecutar_sistema


def crear_datos_iniciales():
    """Impresoras y solicitudes de ejemplo para probar el sistema."""
    impresoras = [
        Impresora3D(1, "4020", "CR-10 #1"),
        Impresora3D(2, "4021", "CR-10 #2"),
        Impresora3D(3, "4022", "CR-10 #3"),
        Impresora3D(4, "4023", "CR-10 #4"),
        
    ]

    solicitudes = [
        SolicitudImpresion(
            id=1,
            codigo_estudiante="1905001001",
            nombre_estudiante="Alex Ramírez",
            facultad=1,
            impresora_id=1,
            fecha_impresion="10/06/2025",
            duracion_minutos=120,
            material_gramos=80,
            estado="FINALIZADA",
        ),
        SolicitudImpresion(
            id=2,
            codigo_estudiante="1905001002",
            nombre_estudiante="Camila López",
            facultad=1,
            impresora_id=2,
            fecha_impresion="15/06/2025",
            duracion_minutos=90,
            material_gramos=60,
            estado="FINALIZADA",
        ),
        SolicitudImpresion(
            id=3,
            codigo_estudiante="1905001003",
            nombre_estudiante="Diego Martínez",
            facultad=2,
            impresora_id=3,
            fecha_impresion="20/06/2025",
            duracion_minutos=180,
            material_gramos=120,
            estado="EN_CURSO",
        ),
        SolicitudImpresion(
            id=4,
            codigo_estudiante="1905001004",
            nombre_estudiante="Valentina Pérez",
            facultad=3,
            impresora_id=4,
            fecha_impresion="21/06/2025",
            duracion_minutos=60,
            material_gramos=50,
            estado="EN_CURSO",
        ),
        SolicitudImpresion(
            id=5,
            codigo_estudiante="1905001005",
            nombre_estudiante="Luis Herrera",
            facultad=1,
            impresora_id=1,
            fecha_impresion="25/06/2025",
            duracion_minutos=120,
            material_gramos=90,
            estado="PENDIENTE",
        ),

        SolicitudImpresion(
            id=6,
            codigo_estudiante="1905001001",
            nombre_estudiante="Jose ramirez",
            facultad=1,
            impresora_id=1,
            fecha_impresion="10/06/2025",
            duracion_minutos=120,
            material_gramos=80,
            estado="EN_CURSO",
        ),
    ]

    return impresoras, solicitudes


def main():
    impresoras, solicitudes = crear_datos_iniciales()
    sistema = SistemaImpresoras3D(impresoras=impresoras, solicitudes=solicitudes)
    ejecutar_sistema(sistema)


if __name__ == "__main__":
    main()
