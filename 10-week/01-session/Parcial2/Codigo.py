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

class Conductor(Empleados):
    def rol(self):
        return "Conductor"

    def conducir(self, vehiculo, km):
        vehiculo.add_km(km)
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

class Camion(Vehiculos):
    def tipo(self):
        return "Camion"

    def costo_mantenimiento(self):
        return 3000000

class Carro(Vehiculos):
    def tipo(self):
        return "Carro"

    def costo_mantenimiento(self):
        return 1500000

class Moto(Vehiculos):
    def tipo(self):
        return "Moto"

    def costo_mantenimiento(self):
        return 400000

def main():
    # EMPLEADOS

    conductores = [
        Conductor("42001", "Jesus Ariel González"),
        Conductor("42002", "Juan Diego Trujillo"),
        Conductor("42003", "Brayan Esteban Rojas"),
        Conductor("42004", "Nicolas Santiago"),
        Conductor("42005", "Marianita Lopez")
    ]

    mecanicos = [
        Mecanico("41001", "Johan Cardenas"),
        Mecanico("41002", "Juan Gonzalez"),
        Mecanico("41003", "Jhon Erick Puentes")
    ]

    print("\n LISTA DE EMPLEADOS ")
    for e in conductores + mecanicos:
        print(e.presentarse())

    # VEHÍCULOS

    carros = [
        Carro("OMG650", 23500),
        Carro("AAA120", 20041),
        Carro("UAQ629", 8930)
    ]

    motos = [
        Moto("PMU79S", 4420),
        Moto("RVK62E", 35022),
        Moto("REW001", 40539)
    ]

    camiones = [
        Camion("ABG435", 90021),
        Camion("AVB234", 85067),
        Camion("AWH430", 75656)
    ]

    # ASIGNACIÓN DE VEHÍCULOS
    carros[0].asignar_conductor(conductores[0])
    carros[1].asignar_conductor(conductores[1])
    motos[0].asignar_conductor(conductores[2])
    motos[1].asignar_conductor(conductores[0])
    camiones[0].asignar_conductor(conductores[3])
    camiones[2].asignar_conductor(conductores[4])

    # 3) INFORMACIÓN GENERAL 

    print("\n LISTA DE VEHÍCULOS ")
    for v in carros + motos + camiones:
        print(v.descripcion())

    print("\n COSTOS DE MANTENIMIENTO ")
    for v in carros + motos + camiones:
        print(v.tipo(), "->", v.costo_mantenimiento())

    # 4) REVISIÓN DE ESTADO DE EMPLEADOS

    print("\n ESTADO DE EMPLEADOS ")
    #ACTIVAR EMPLEADO
    print(conductores[1].get_nombre(), "activo?", conductores[1].estado())
    print(mecanicos[2].get_nombre(), "activo?", mecanicos[2].estado())

    # DESACTIVAR EMPLEADO
    conductores[1].desactivar()
    mecanicos[2].desactivar()
    print(conductores[1].get_nombre(), "activo?", conductores[1].estado())
    print(mecanicos[2].get_nombre(), "activo?", mecanicos[2].estado())

    # REACTIVAR 
    conductores[1].activar()
    mecanicos[2].activar()
    print(conductores[1].get_nombre(), "activo?", conductores[1].estado())
    print(mecanicos[2].get_nombre(), "activo?", mecanicos[2].estado())

if __name__ == "__main__":
    main()
