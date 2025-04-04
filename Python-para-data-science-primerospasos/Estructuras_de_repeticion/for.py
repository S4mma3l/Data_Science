# range solo trabaj con numeros enteros

for n in range(1, 11):
    print(n)

for e in range(1, 4):
    nota_1 = float(input(f"Ingrese la primera nota del estudiante #{e}: "))
    nota_2 = float(input(f"Ingrese la segunda nota del estudiante #{e}: "))
    print(f"El promedio del estudiante #{e} es: {(nota_1 + nota_2) / 2}")