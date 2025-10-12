from vehiculos.carros import Carro
from vehiculos.motos import Moto
from vehiculos.camiones import Camion
from empleados.conductores import Conductor
from empleados.mecanicos import Mecanico, registros_placa

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
