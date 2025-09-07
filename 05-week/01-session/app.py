#Código desarrollado por Juan Pablo Gonzalez Trujillo

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, titulo, stock):
        self.titulo = titulo
        self.stock = stock

    @abstractmethod
    def prestamo(self):
        pass

    @abstractmethod
    def multa(self):
        pass

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, cantidad):
        if cantidad >= 0:
            self._stock = cantidad
        else:
            raise ValueError("El stock no puede ser negativo")

class Libro(Item):
    def prestamo(self):
        return 14

    def multa(self):
        return 300

class Revista(Item):
    def prestamo(self):
        return 7

    def multa(self):
        return 200

class Usuario:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self._documento = documento

    @property
    def documento(self):
        return self._documento

class Prestamo:
    def __init__(self, usuario, material, fecha_inicio):
        self.usuario = usuario
        self.material = material
        self.fecha_inicio = fecha_inicio

    def dias_prestados(self, fecha_devolucion):
        dia_inicio = int(self.fecha_inicio.split("/")[0])
        dia_devolucion = int(fecha_devolucion.split("/")[0])
        return dia_devolucion - dia_inicio

    def multa_total(self, fecha_devolucion):
        dias = self.dias_prestados(fecha_devolucion)
        dias_retraso = dias - self.material.prestamo()
        if dias_retraso > 0:
            return dias_retraso * self.material.multa()
        return 0

class Biblioteca:
    def __init__(self):
        self.materiales = []
        self.usuarios = []
        self.prestamos = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def agregar_usuario(self, usuario):
        for u in self.usuarios:
            if u.documento == usuario.documento:
                print("Documento ya registrado.")
                return
        self.usuarios.append(usuario)

    def crear_prestamo(self, usuario, material, fecha_inicio):
        for p in self.prestamos:
            if p.usuario == usuario and p.material == material:
                print("Ese usuario ya tiene ese material prestado.")
                return

        if material.stock <= 0:
            print("No hay stock disponible.")
            return

        nuevo = Prestamo(usuario, material, fecha_inicio)
        self.prestamos.append(nuevo)
        material.stock -= 1
        print("Préstamo creado con éxito.")

    def devolver_material(self, usuario, material, fecha_devolucion):
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.material == material:
                multa = prestamo.multa_total(fecha_devolucion)
                print(f"Multa a pagar: ${multa}")
                self.prestamos.remove(prestamo)
                material.stock += 1
                print("Material devuelto correctamente.")
                return
        print("No se encontró ese préstamo.")

biblio = Biblioteca()

def buscar_usuario(documento):
    return next((u for u in biblio.usuarios if u.documento == documento), None)

def buscar_material(titulo):
    return next((m for m in biblio.materiales if m.titulo == titulo), None)

#---------------------------------------------------------------------------#
juan = Usuario("Juan Esteban", "15611")
erick = Usuario("Erick", "21832")
camila = Usuario("Camila", "33803")
mateo = Usuario("Mateo", "445534")

biblio.agregar_usuario(juan)
biblio.agregar_usuario(erick)
biblio.agregar_usuario(camila)
biblio.agregar_usuario(mateo)

metamorfosis = Libro("La Metamorfosis", 1)
ford = Revista("Ford", 2)
hobbit = Libro("Hobbit", 1)

biblio.agregar_material(metamorfosis)
biblio.agregar_material(ford)
biblio.agregar_material(hobbit)

# Préstamo con retraso (Juan) hace 1 mes
biblio.crear_prestamo(juan, metamorfosis, "06/08/2025")

# Préstamo sin retraso (Camila) hace 5 dias
biblio.crear_prestamo(camila, ford, "01/09/2025")

# Erick hizo un préstamo sin retraso hace 2 dia
biblio.crear_prestamo(erick, hobbit, "04/09/2025")


while True:
    print("\n--- MENÚ BIBLIOTECA ---")
    print("1. Agregar usuario")
    print("2. Agregar material")
    print("3. Crear préstamo")
    print("4. Devolver material")
    print("5. Ver préstamos con multa estimada")
    print("6. Listar usuarios y materiales")
    print("7. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del usuario: ")
        documento = input("Documento (único): ")
        nuevo = Usuario(nombre, documento)
        biblio.agregar_usuario(nuevo)

    elif opcion == "2":
        tipo = input("¿Tipo de material? (libro/revista): ").lower()
        titulo = input("Título: ")
        stock = int(input("Stock disponible: "))
        if tipo == "libro":
            biblio.agregar_material(Libro(titulo, stock))
        elif tipo == "revista":
            biblio.agregar_material(Revista(titulo, stock))
        else:
            print("Tipo no válido.")

    elif opcion == "3":
        doc = input("Documento del usuario: ")
        titulo = input("Título del material: ")
        fecha = input("Fecha de inicio (dd/mm/aaaa): ")
        usuario = buscar_usuario(doc)
        material = buscar_material(titulo)
        if usuario and material:
            biblio.crear_prestamo(usuario, material, fecha)
        else:
            print("Usuario o material no encontrado.")

    elif opcion == "4":
        doc = input("Documento del usuario: ")
        titulo = input("Título del material: ")
        fecha = input("Fecha de devolución (dd/mm/aaaa): ")
        usuario = buscar_usuario(doc)
        material = buscar_material(titulo)
        if usuario and material:
            biblio.devolver_material(usuario, material, fecha)
        else:
            print("Usuario o material no encontrado.")

    elif opcion == "5":
        for p in biblio.prestamos:
            print(f"\nUsuario: {p.usuario.nombre}")
            print(f"Material: {p.material.titulo}")
            print(f"Fecha de inicio: {p.fecha_inicio}")
            print(f"Días permitidos: {p.material.prestamo()}")
            dias_transcurridos = int(input("¿Cuántos días han pasado desde el préstamo?: "))
            dias_retraso = dias_transcurridos - p.material.prestamo()
            multa = dias_retraso * p.material.multa() if dias_retraso > 0 else 0
            print(f"¿Retrasado?: {'Sí' if dias_retraso > 0 else 'No'}")
            print(f"Multa estimada: ${multa}")

    elif opcion == "6":
        print("\nUsuarios:")
        for u in biblio.usuarios:
            print(f"{u.nombre} - Documento: {u.documento}")
        print("\nMateriales:")
        for m in biblio.materiales:
            print(f"{m.__class__.__name__}: {m.titulo} - Stock: {m.stock}")

    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida.")