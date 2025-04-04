'''
nota_1 = float(input("Ingrese la primera nota del estudiante #1: "))
nota_2 = float(input("Ingrese la segunda nota del estudiante #1: "))
print(f"El promedio del estudiante #1 es: {(nota_1 + nota_2) / 2}")

nota_1 = float(input("Ingrese la primera nota del estudiante #2: "))
nota_2 = float(input("Ingrese la segunda nota del estudiante #2: "))
print(f"El promedio del estudiante #2 es: {(nota_1 + nota_2) / 2}")

nota_1 = float(input("Ingrese la primera nota del estudiante #3: "))
nota_2 = float(input("Ingrese la segunda nota del estudiante #3: "))
print(f"El promedio del estudiante #3 es: {(nota_1 + nota_2) / 2}")
'''

### uso de While

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

contador = 1
while contador <= 3:
    nota_1 = float(input(f"Ingrese la primera nota del estudiante #{contador}: "))
    nota_2 = float(input(f"Ingrese la segunda nota del estudiante #{contador}: "))
    print(f"El promedio del estudiante #{contador} es: {(nota_1 + nota_2) / 2}")
    contador += 1