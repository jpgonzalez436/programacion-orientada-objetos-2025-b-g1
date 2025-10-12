from vehiculos import Vehiculos

class Moto(Vehiculos):
    def tipo(self):
        return "Moto"

    def costo_mantenimiento(self):
        return 400000
