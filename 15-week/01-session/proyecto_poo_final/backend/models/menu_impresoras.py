"""Menú de consola para el sistema de impresoras 3D."""

from models import FACULTADES

CONTRASENA_ADMIN = "1234"


def _pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print("Ingrese un número entre", minimo, "y", maximo)
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")


def _mostrar_impresoras(sistema):
    print("\n=== IMPRESORAS 3D ===")
    for impresora in sistema.impresoras:
        estado = sistema.obtener_estado_impresora(impresora.id)
        print(f"{impresora.id}. {impresora.codigo} - {impresora.nombre} [{estado}]")


def _menu_impresora(sistema):
    _mostrar_impresoras(sistema)
    impresora_id = _pedir_entero(
        "Seleccione una impresora (0 para volver): ", 0, len(sistema.impresoras)
    )
    if impresora_id == 0:
        return

    while True:
        print(f"\n=== IMPRESORA SELECCIONADA: {impresora_id} ===")
        print("1. Ver historial de uso")
        print("2. Ver estado actual")
        print("0. Volver")
        opcion = _pedir_entero("Seleccione una opción: ", 0, 2)

        if opcion == 0:
            break
        if opcion == 1:
            _mostrar_historial_impresora(sistema, impresora_id)
        elif opcion == 2:
            estado = sistema.obtener_estado_impresora(impresora_id)
            print("\nEstado actual:", estado)


def _mostrar_historial_impresora(sistema, impresora_id):
    historial = sistema.obtener_historial_impresora(impresora_id)
    if not historial:
        print("\nNo hay registros de uso para esta impresora.")
        return

    print("\n=== HISTORIAL DE USO ===")
    for s in historial:
        facultad_nombre = FACULTADES.get(s.facultad, "Desconocida")
        print(
            f"- Solicitud #{s.id} | Fecha: {s.fecha_impresion} | "
            f"Duración: {s.duracion_minutos} min | "
            f"Material: {s.material_gramos} g PLA | Estado: {s.estado}"
        )
        print(
            f"  Estudiante: {s.nombre_estudiante} "
            f"({s.codigo_estudiante}) | Facultad: {facultad_nombre}"
        )
        if s.estado == "RECHAZADA" and s.motivo_rechazo:
            print(f"  Motivo de rechazo: {s.motivo_rechazo}")
        print()


def _crear_solicitud_interactiva(sistema):
    print("\n=== SOLICITAR USO DE IMPRESORA 3D ===")
    print("1. Diligencias los datos.")
    print("2. Se envía la solicitud.")
    print("3. El administrador aprueba o rechaza.")
    print("4. Si aprueba, la impresora queda EN USO hasta finalizar.\n")

    _mostrar_impresoras(sistema)
    impresora_id = _pedir_entero(
        "Seleccione la impresora que desea usar: ", 1, len(sistema.impresoras)
    )

    codigo = input("Código del estudiante: ").strip()
    nombre = input("Nombre completo del estudiante: ").strip()

    print("\nFacultad:")
    print("1. Ingeniería Mecatrónica")
    print("2. Ingeniería de Energías Renovables")
    print("3. Ingeniería Industrial")
    facultad = _pedir_entero("Seleccione la facultad [1-3]: ", 1, 3)

    fecha = input("Fecha de impresión (dd/mm/aaaa): ").strip()
    duracion = _pedir_entero("Duración estimada (minutos): ", 10, 600)
    material = _pedir_entero("Cantidad de material (gramos PLA): ", 10, 2000)

    solicitud = sistema.crear_solicitud(
        codigo_estudiante=codigo,
        nombre_estudiante=nombre,
        facultad=facultad,
        impresora_id=impresora_id,
        fecha_impresion=fecha,
        duracion_minutos=duracion,
        material_gramos=material,
    )

    print("\nSolicitud registrada.")
    print("Número de solicitud:", solicitud.id)
    print("Estado inicial: PENDIENTE.\n")


def _menu_admin(sistema):
    print("\n=== ACCESO ADMINISTRADOR ===")
    contrasena = input("Contraseña (1234) o ENTER para cancelar: ").strip()
    if contrasena != CONTRASENA_ADMIN:
        print("Contraseña incorrecta.")
        return

    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Ver solicitudes pendientes")
        print("2. Aprobar / rechazar solicitud")
        print("3. Finalizar impresión")
        print("0. Volver")
        opcion = _pedir_entero("Seleccione una opción: ", 0, 3)

        if opcion == 0:
            break
        if opcion == 1:
            _mostrar_solicitudes_pendientes(sistema)
        elif opcion == 2:
            _aprobar_o_rechazar_solicitud(sistema)
        elif opcion == 3:
            _finalizar_impresion_admin(sistema)


def _mostrar_solicitudes_pendientes(sistema):
    pendientes = sistema.obtener_solicitudes_pendientes()
    if not pendientes:
        print("\nNo hay solicitudes pendientes.")
        return

    print("\n=== SOLICITUDES PENDIENTES ===")
    for s in pendientes:
        facultad_nombre = FACULTADES.get(s.facultad, "Desconocida")
        print(
            f"- Solicitud #{s.id} | Impresora {s.impresora_id} | "
            f"Fecha {s.fecha_impresion} | {s.duracion_minutos} min, "
            f"{s.material_gramos} g PLA"
        )
        print(
            f"  Estudiante: {s.nombre_estudiante} "
            f"({s.codigo_estudiante}) | Facultad: {facultad_nombre}"
        )
        print()


def _aprobar_o_rechazar_solicitud(sistema):
    pendientes = sistema.obtener_solicitudes_pendientes()
    if not pendientes:
        print("\nNo hay solicitudes pendientes.")
        return

    solicitud_id = _pedir_entero(
        "Número de solicitud a gestionar: ", 1, 10000
    )

    print("\n1. Aprobar (inicia impresión)")
    print("2. Rechazar")
    accion = _pedir_entero("Seleccione una acción: ", 1, 2)

    if accion == 1:
        mensaje = sistema.aprobar_solicitud(solicitud_id)
        print("\n" + mensaje)
    else:
        motivo = input("Motivo de rechazo: ").strip()
        mensaje = sistema.rechazar_solicitud(solicitud_id, motivo)
        print("\n" + mensaje)


def _finalizar_impresion_admin(sistema):
    solicitud_id = _pedir_entero(
        "Número de solicitud a finalizar: ", 1, 10000
    )
    mensaje = sistema.finalizar_impresion(solicitud_id)
    print("\n" + mensaje)


def ejecutar_sistema(sistema):
    while True:
        print("\n=== SISTEMA DE IMPRESORAS 3D (FABLAB) ===")
        print("1. Ver impresoras y estado / historial")
        print("2. Solicitar uso de una impresora")
        print("3. Menú administrador")
        print("0. Salir")

        opcion = _pedir_entero("Seleccione una opción: ", 0, 3)

        if opcion == 0:
            print("Saliendo del sistema...")
            break
        if opcion == 1:
            _menu_impresora(sistema)
        elif opcion == 2:
            _crear_solicitud_interactiva(sistema)
        elif opcion == 3:
            _menu_admin(sistema)
