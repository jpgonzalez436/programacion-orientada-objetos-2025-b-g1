from empleados import Empleados

_REGISTROS = []

class Mecanico(Empleados):
    def rol(self):
        return "Mecánico"

    def registrar_mantenimiento(self, vehiculo, detalles, costo):
        _REGISTROS.append({
            "placa": vehiculo.get_placa(),
            "mecanico": self.get_nombre(),
            "detalles": detalles,
            "costo": float(costo),
        })
        return f"OK:{vehiculo.get_placa()}:{len(_REGISTROS)}"

def registros_placa(placa):
    lista = []
    for r in _REGISTROS:
        if r["placa"] == placa:
            lista.append(r)
    return lista
