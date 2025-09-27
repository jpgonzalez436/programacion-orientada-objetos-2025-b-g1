class Persona:
    def __init__(self, nombre, edad, ID, correo):
         self.nombre= nombre
         self.edad= edad
         self.ID= ID
         self.correo= correo

    def saludar(self):
         return f"Hola, {self.nombre}"
         
    def mayor_edad(self):
         if self.edad >= 18:
              return f"{self.nombre} es mayor de edad"
         else:
              return f"{self.nombre} no es mayor de edad"
         
    def mostrar_info(self):
         return f"nombre: {self.nombre} edad: {self.edad} años, identificación: {self.ID} y correo: {self.correo}"
              
    def actualizar_correo(self, nuevo_correo):
         self.correo= nuevo_correo

class Estudiante(Persona):
    def __init__(self, nombre, edad, id, correo, carrera, semestre, promedio):
        super().__init__(nombre, edad, id, correo)
        self.carrera = carrera
        self.semestre = semestre
        self.promedio= promedio

    def estudiar(self):
         if self.carrera:
            return f"El estudiante {self.nombre} está cursando la carrera de: {self.carrera}"
         else:
            return f"Actualmente {self.nombre} no está cursando ninguna carrera"

    def calcular_beca(self):
        if self.promedio >= 4.0:
            return f"El estudiante {self.nombre} está becado"
        
    def mostrar_info(self):
        new_info = super().mostrar_info()  
        return f"{new_info}, carrera: {self.carrera}, semestre: {self.semestre}, promedio: {self.promedio}"
    
class Profesor(Persona):
    def __init__(self, nombre, edad, id, correo, asignatura, salario, experiencia):
        super().__init__(nombre, edad, id, correo)
        self.asignatura = asignatura
        self.salario = salario
        self.experiencia= experiencia

    def dictar_clase(self):
        if self.asignatura:
            return f"El docente {self.nombre} está dictando la asignatura de {self.asignatura}"
        else:
            return f"El docente {self.nombre} no está dictando ninguna asignatura"
        
    def calcular_prima(self):
        prima = self.salario * 0.10 * (self.experiencia // 5)
        return f"Actualmente la prima de {self.nombre} es de ${prima} COP"
    
    def mostrar_info(self):
        new_info = super().mostrar_info()  
        return f"{new_info}, asignatura: {self.asignatura}, salario: ${self.salario} COP, años de experiencia: {self.experiencia} años"
        
#PROGRAMA PRINCIPAL
    
Persona1 = Persona("Carlos Enrique Cuellar", 40, 10423802, "Cuellar.e@gmail.com")
Estudiante1= Estudiante ("Juan Pablo Gonzalez", 22, 1002580215, "jpgonzales-2024b@corhuila.edu.co", "Ingeniería Mecatrónica", 3, 4.67)
Profesor1= Profesor("Jesús Ariel González", 33, 1728231, "jesus.gonzalez@corhuila.edu.co", "Programación Orientada a Objetos", 4800000, 9)

print(Persona1.saludar())
print(Persona1.mayor_edad())
print(Persona1.mostrar_info())

print(Estudiante1.saludar())
print(Estudiante1.mayor_edad())
print(Estudiante1.estudiar())
print(Estudiante1.calcular_beca())
print(Estudiante1.mostrar_info())

print(Profesor1.saludar())
print(Profesor1.mayor_edad())
print(Profesor1.dictar_clase())
print(Profesor1.calcular_prima())
print(Profesor1.mostrar_info())

