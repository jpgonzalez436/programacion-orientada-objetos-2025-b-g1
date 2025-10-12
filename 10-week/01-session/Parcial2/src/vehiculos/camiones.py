from vehiculos import Vehiculos

class Camion(Vehiculos):
    def tipo(self):
        return "Camion"

    def costo_mantenimiento(self):
        return 3000000
