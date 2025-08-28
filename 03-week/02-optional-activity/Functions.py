#hallar la media de notas de 4 alumnos
def notas(n1,n2,n3,n4):
    suma = n1 + n2 + n3 + n4
    return suma/4
#Con def le decimos a python que vamos a crear una función
#Con n1... le decimos a python que vamos a recibir 4 parámetros y los inicializamos
#Con return le decimos a python que nos devuelva un valor
print("La media de las notas es: ", notas(5,7,8,9))