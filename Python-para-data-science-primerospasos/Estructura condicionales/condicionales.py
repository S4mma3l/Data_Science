# Nota de aprobacion entre 7 y 10 == nota de aprobacion >= 7
# Nota de reprobacion es menor a 7 == nota de reprobacion < 7

'''
Si la nota es mayor o igual a 7, entonces el alumno aprueba el curso.
Si no, entonces el alumno reprueba el curso.
'''

if 2 < 7:
    print("La condicion es verdadera")

if 2 > 7:
    print("La condicion es verdadera")
print("La condicion es falsa")

# ejemplo de condicion simple

if 2 < 7:
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")
print("Fin de la condicion")
# ejemplo de condicion compuesta

### Utilizando if y else

nota = float(input("Ingrese la nota del alumno: "))

if nota >= 7:
    print("El alumno aprueba el curso")
else:
    print("El alumno reprueba el curso")


### ejemplo cuando existe una posiblidad de poder aprobar el curso

nota = float(input("Ingrese la nota del alumno: "))

if nota >= 7:
    print("El alumno aprueba el curso")
if 7 > nota >= 5:
    print("El alumno tiene una oportunidad de aprobar el curso en recuperacion")
if nota < 5:
    print("El alumno reprueba el curso")

# error de logica
nota = float(input("Ingrese la nota del alumno: "))

if nota >= 7:
    print("El alumno aprueba el curso")
if 7 > nota >= 5:
    print("El alumno tiene una oportunidad de aprobar el curso en recuperacion")
else:
    print("El alumno reprueba el curso")

# uso de elif
# ejemplo cuando existe una posiblidad de poder aprobar el curso
nota = float(input("Ingrese la nota del alumno: "))

if nota >= 7:
    print("El alumno aprueba el curso")
elif 7 > nota >= 5:
    print("El alumno tiene una oportunidad de aprobar el curso en recuperacion")
else:
    print("El alumno reprueba el curso")