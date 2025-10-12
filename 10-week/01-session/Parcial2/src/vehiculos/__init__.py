from abc import ABC, abstractmethod

class Vehiculos(ABC):
    def __init__(self, placa, kilometraje_inicial=0):
        self.__placa = placa
        self.__kilometraje = kilometraje_inicial
        self.__asignado_a = None  

    def get_placa(self):
        return self.__placa

    def get_kilometraje(self):
        return self.__kilometraje

    def get_asignado_a(self):
        return self.__asignado_a

    def asignar_conductor(self, conductor):
        self.__asignado_a = conductor

    def add_km(self, km):
        self.__kilometraje = self.__kilometraje + km

    def descripcion(self):
        if self.__asignado_a:
            persona = self.__asignado_a.get_nombre()
        else:
            persona = "Sin asignar"
        return f"{self.tipo()} {self.__placa},  km: {self.__kilometraje} Conductor: {persona}"

    @abstractmethod
    def tipo(self) -> str:
        pass

    @abstractmethod
    def costo_mantenimiento(self) -> float:
        pass
