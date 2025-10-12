from empleados import Empleados

class Conductor(Empleados):
    def rol(self):
        return "Conductor"

    def conducir(self, vehiculo, km):
        vehiculo.add_km(km)
