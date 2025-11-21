"""Lógica del sistema de gestión de impresoras 3D."""

from .modelos_impresoras import Impresora3D, SolicitudImpresion

# 1 = Mecatrónica, 2 = Renovables, 3 = Industrial
FACULTADES = {
    1: "Ingeniería Mecatrónica",
    2: "Ingeniería de Energías Renovables",
    3: "Ingeniería Industrial",
}


class SistemaImpresoras3D:
    """Gestiona impresoras, solicitudes y estados."""

    def __init__(self, impresoras=None, solicitudes=None):
        self.impresoras = impresoras or []
        self.solicitudes = solicitudes or []
        self._siguiente_id = len(self.solicitudes) + 1
        self._actualizar_estados_impresoras()

    def _actualizar_estados_impresoras(self):
        """Sincroniza estados EN_CURSO -> impresora EN_USO."""
        for impresora in self.impresoras:
            impresora.estado = "DISPONIBLE"

        for solicitud in self.solicitudes:
            if solicitud.estado == "EN_CURSO":
                for impresora in self.impresoras:
                    if impresora.id == solicitud.impresora_id:
                        impresora.estado = "EN_USO"

    def _buscar_impresora(self, impresora_id):
        for impresora in self.impresoras:
            if impresora.id == impresora_id:
                return impresora
        return None

    def _buscar_solicitud(self, solicitud_id):
        for solicitud in self.solicitudes:
            if solicitud.id == solicitud_id:
                return solicitud
        return None

    # Operaciones públicas

    def crear_solicitud(
        self,
        codigo_estudiante,
        nombre_estudiante,
        facultad,
        impresora_id,
        fecha_impresion,
        duracion_minutos,
        material_gramos,
    ):
        nueva = SolicitudImpresion(
            id=self._siguiente_id,  
            codigo_estudiante=codigo_estudiante,
            nombre_estudiante=nombre_estudiante,
            facultad=facultad,
            impresora_id=impresora_id,
            fecha_impresion=fecha_impresion,
            duracion_minutos=duracion_minutos,
            material_gramos=material_gramos,
            estado="PENDIENTE",
        )
        self.solicitudes.append(nueva)
        self._siguiente_id += 1
        return nueva

    def obtener_historial_impresora(self, impresora_id):
        """Devuelve solicitudes de una impresora."""
        historial = []
        for solicitud in self.solicitudes:
            if (
                solicitud.impresora_id == impresora_id
                and solicitud.estado != "PENDIENTE"
            ):
                historial.append(solicitud)
        return historial

    def obtener_solicitudes_pendientes(self):
        pendientes = []
        for solicitud in self.solicitudes:
            if solicitud.estado == "PENDIENTE":
                pendientes.append(solicitud)
        return pendientes

    def aprobar_solicitud(self, solicitud_id):
        """Aprueba y deja la impresión en curso si se puede."""
        solicitud = self._buscar_solicitud(solicitud_id)
        if solicitud is None:
            return "Solicitud no encontrada."

        if solicitud.estado != "PENDIENTE":
            return "Solo se pueden aprobar solicitudes pendientes."

        impresora = self._buscar_impresora(solicitud.impresora_id)
        if impresora is None:
            return "Impresora no encontrada."

        if not impresora.esta_disponible():
            return "No se puede aprobar: la impresora está en uso."

        # Solo una impresión por día y por impresora
        for s in self.solicitudes:
            if (
                s.id != solicitud.id
                and s.impresora_id == solicitud.impresora_id
                and s.fecha_impresion == solicitud.fecha_impresion
                and s.estado in ("EN_CURSO", "FINALIZADA")
            ):
                return (
                    "No se puede aprobar: ya existe una impresión para esa "
                    "impresora en esa fecha."
                )

        solicitud.estado = "EN_CURSO"
        impresora.estado = "EN_USO"
        return "Solicitud aprobada e impresión iniciada. La impresora queda EN USO."

    def rechazar_solicitud(self, solicitud_id, motivo):
        solicitud = self._buscar_solicitud(solicitud_id)
        if solicitud is None:
            return "Solicitud no encontrada."

        if solicitud.estado != "PENDIENTE":
            return "Solo se pueden rechazar solicitudes pendientes."

        solicitud.estado = "RECHAZADA"
        solicitud.motivo_rechazo = motivo
        return "Solicitud rechazada."

    def finalizar_impresion(self, solicitud_id):
        solicitud = self._buscar_solicitud(solicitud_id)
        if solicitud is None:
            return "Solicitud no encontrada."

        if solicitud.estado != "EN_CURSO":
            return "Solo se pueden finalizar impresiones en curso."

        impresora = self._buscar_impresora(solicitud.impresora_id)
        if impresora is None:
            return "Impresora no encontrada."

        impresora.estado = "DISPONIBLE"
        solicitud.estado = "FINALIZADA"
        return "Impresión finalizada."

    def obtener_estado_impresora(self, impresora_id):
        impresora = self._buscar_impresora(impresora_id)
        if impresora is None:
            return "Impresora no encontrada."

        if impresora.esta_disponible():
            return "DISPONIBLE"

        for solicitud in self.solicitudes:
            if solicitud.impresora_id == impresora.id and solicitud.estado == "EN_CURSO":
                return (
                    "EN USO por "
                    + solicitud.nombre_estudiante
                    + " ("
                    + solicitud.codigo_estudiante
                    + ") el "
                    + solicitud.fecha_impresion
                )

        return "EN USO"
