"""Servicio para gestionar reservas de laboratorios."""

from typing import List

from models.laboratorio import Laboratorio
from models.grupo import Grupo
from models.docente import Docente
from models.reserva import Reserva


class ReservationService:
    """Encapsula la lógica de creación y consulta de reservas."""

    def __init__(self) -> None:
        self.reservas: List[Reserva] = []

    @staticmethod
    def _hora_a_minutos(hora_str: str) -> int:
        """Convierte 'HH:MM' a minutos enteros."""
        horas_str, minutos_str = hora_str.split(":")
        horas = int(horas_str)
        minutos = int(minutos_str)
        return horas * 60 + minutos

    def _rangos_se_solapan(
        self,
        hora_inicio1: str,
        hora_fin1: str,
        hora_inicio2: str,
        hora_fin2: str,
    ) -> bool:
        """
        Determina si dos rangos horarios se solapan.

        Se considera que [ini1, fin1) se solapa con [ini2, fin2) si:
        ini1 < fin2 y ini2 < fin1
        """
        ini1 = self._hora_a_minutos(hora_inicio1)
        fin1 = self._hora_a_minutos(hora_fin1)
        ini2 = self._hora_a_minutos(hora_inicio2)
        fin2 = self._hora_a_minutos(hora_fin2)
        return ini1 < fin2 and ini2 < fin1

    def laboratorio_esta_libre(
        self,
        laboratorio: Laboratorio,
        fecha: str,
        hora_inicio: str,
        hora_fin: str,
    ) -> bool:
        """Indica si el laboratorio está libre en esa fecha y rango horario."""
        for reserva in self.reservas:
            if reserva.laboratorio.id == laboratorio.id and reserva.fecha == fecha:
                if self._rangos_se_solapan(
                    reserva.hora_inicio,
                    reserva.hora_fin,
                    hora_inicio,
                    hora_fin,
                ):
                    return False
        return True

    def crear_reserva_regular(
        self,
        id_: int,
        laboratorio: Laboratorio,
        grupo: Grupo,
        docente: Docente,
        fecha: str,
        hora_inicio: str,
        hora_fin: str,
    ) -> Reserva | None:
        """Crea una reserva REGULAR si el laboratorio está libre."""
        if not self.laboratorio_esta_libre(
            laboratorio,
            fecha,
            hora_inicio,
            hora_fin,
        ):
            print(
                f"[ERROR] {laboratorio.codigo} ocupado en "
                f"{fecha} {hora_inicio}-{hora_fin}.",
            )
            return None

        reserva = Reserva(
            id_=id_,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            tipo="REGULAR",
            laboratorio=laboratorio,
            grupo=grupo,
            docente=docente,
        )
        self.reservas.append(reserva)
        print(f"[OK] Reserva REGULAR creada: {reserva}")
        return reserva

    def crear_reserva_extracurricular(
        self,
        id_: int,
        laboratorio: Laboratorio,
        grupo: Grupo,
        docente: Docente | None,
        fecha: str,
        hora_inicio: str,
        hora_fin: str,
    ) -> Reserva | None:
        """
        Crea una reserva EXTRACURRICULAR validando:

        - laboratorio libre
        - duración entre 1 y 3 horas
        - grupo con entre 6 y capacidad_max estudiantes
        - docente obligatorio
        """
        if docente is None:
            print(
                "[ERROR] Una reserva EXTRACURRICULAR debe "
                "tener un docente asignado.",
            )
            return None

        if grupo.numero_estudiantes < 6:
            print(
                "[ERROR] El grupo tiene menos de 6 estudiantes, "
                "no se permite reserva extracurricular.",
            )
            return None

        if grupo.numero_estudiantes > laboratorio.capacidad_max:
            print(
                "[ERROR] El grupo supera la capacidad del laboratorio.",
            )
            return None

        ini = self._hora_a_minutos(hora_inicio)
        fin = self._hora_a_minutos(hora_fin)
        duracion = fin - ini

        if duracion < 60:
            print(
                "[ERROR] Una reserva extracurricular debe "
                "durar al menos 1 hora.",
            )
            return None

        if duracion > 180:
            print(
                "[ERROR] Una reserva extracurricular no puede "
                "durar más de 3 horas.",
            )
            return None

        if not self.laboratorio_esta_libre(
            laboratorio,
            fecha,
            hora_inicio,
            hora_fin,
        ):
            print(
                f"[ERROR] {laboratorio.codigo} ocupado en "
                f"{fecha} {hora_inicio}-{hora_fin}.",
            )
            return None

        reserva = Reserva(
            id_=id_,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            tipo="EXTRACURRICULAR",
            laboratorio=laboratorio,
            grupo=grupo,
            docente=docente,
        )
        self.reservas.append(reserva)
        print(f"[OK] Reserva EXTRACURRICULAR creada: {reserva}")
        return reserva

    def obtener_reservas_por_laboratorio_y_fecha(
        self,
        laboratorio: Laboratorio,
        fecha: str,
    ) -> list[Reserva]:
        """Devuelve la lista de reservas de un laboratorio en una fecha dada."""
        return [
            r
            for r in self.reservas
            if r.laboratorio.id == laboratorio.id and r.fecha == fecha
        ]
