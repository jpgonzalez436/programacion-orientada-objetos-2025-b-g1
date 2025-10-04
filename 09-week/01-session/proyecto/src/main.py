# Registrar personas
# Asignar usuarios a personas
# Registrar estudiantes y profesores

# Nota: Cargar y mostar los datos del profesor, estudiante.
#  Se conoce que el estudiante tiene materias asociadas {subject_academic}.
#  Y Un profesor orienta materias {subject_academic}. 
from security.person import Person
from security.user import User
Persona1 = Person("CC", 1002580816,"juan","gonzalez", "date: 19-11-2002" , "gonzalez@gmail")
User1= User("juangonza", 1234, Persona1 )
print (User1)