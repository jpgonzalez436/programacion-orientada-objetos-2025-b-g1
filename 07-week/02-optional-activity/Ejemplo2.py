## Datos del globales
estudiante = input("Digite el nombre del estudiante: ") 
materia = input("Digite el nombre de la materia: ")

## Datos de la nota

### Taller, Quiz y Foro 25%
taller = float(input("Digite la nota del taller: "))
quiz = float(input("Digite la nota del quiz: "))
foro = float(input("Digite la nota del foro: "))

### Parcial 70%
parcial1 = float(input("Digite la nota del parcial parte 1: "))
parcial2 = float(input("Digite la nota del parcial parte 2: "))

### Auto - Coe 5%
auto = float(input("Digite la nota de la autoevaluación: "))
coe = float(input("Digite la nota de la coevaluación: "))

## Sumar notas en diccionarios
nota1 = {"taller": taller, "foro": foro, "quiz": quiz}
nota2 = {"p1": parcial1, "p2": parcial2}
nota3 = {"auto":auto,"coe":coe}
print(f"Las notas del taller, quiz y foro son: {nota1}")
print("La nota del parcial 2 es :" , nota2["p2"])
print(f"Las notas de la autoevaluación y coevaluación son: {nota3}")
#Sacar porcentajes
def porcentajes(notas, porcentaje):
    promedio = 0
    total = 0
    for i in notas:
        promedio += notas[i]
        total += 1
    promedio /= total
    return promedio * porcentaje

nota1f = porcentajes(nota1, 0.25)
nota2f = porcentajes(nota2, 0.7)
nota3f = porcentajes(nota3, 0.05)
corte= nota1f + nota2f + nota3f

print(f"El estudiante {estudiante} de la materia {materia} sacó una nota de {corte:.2f}")

