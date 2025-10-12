from abc import ABC, abstractmethod

class Empleados(ABC):
    def __init__(self, ID, nombre):
        self.__ID = ID
        self.__nombre = nombre
        self.__activo = True

    def get_ID(self):
        return self.__ID

    def get_nombre(self):
        return self.__nombre

    def estado(self):
        return self.__activo

    def activar(self):
        self.__activo = True

    def desactivar(self):
        self.__activo = False

    def presentarse(self):
        return f"Empleado: {self.__nombre}, Cargo: {self.rol()}"

    @abstractmethod
    def rol(self) -> str:
        pass
