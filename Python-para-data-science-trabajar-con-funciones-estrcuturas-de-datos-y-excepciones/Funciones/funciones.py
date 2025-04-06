

notas = {"1 trimestre": 8, "2 trimestre": 9, "3 trimestre": 7.5,}
suma = 0
for s in notas.values():
    suma += s
print(suma)

promedio = sum(notas.values()) / len(notas)
print(promedio)

promedio = round(promedio, 1)
print(promedio)
print(f"El promedio es: {promedio}")

'''
### Tipos de built-in functions

peso = float(input("Digita el peso, en kilogramos: "))
altura = float(input("Digita la altura, en metros: "))

imc = round(peso / pow(altura, 2), 2)

print(f"El IMC de la persona es: {imc}")


# Funciones sin parametros

def promedio():
    calculo = (10 + 9 + 7)/3
    print(f"El promedio es: {calculo}")

# Funciones con parametros


def promedio(n1, n2, n3):
    calculo = (n1 + n2 + n3)/3
    print(f"El promedio es: {calculo}")

promedio(10, 9, 7)


notas = [8.5, 9.0, 6.0, 10.0]

def promedio(lista):
    calculo = sum(lista) / len(lista)
    print(f"El promedio es: {calculo}")
promedio(notas)
media = promedio(notas)
print(media)

# Funciones con retorno de valores
examen = [8.5, 9.0, 6.0,]

def promedio(lista):
    resultado = sum(lista)/len(lista)
    if resultado >= 7:
        situacion = "Aprobado"
    else:
        situacion = "Reprobado"
    return resultado, situacion

promedio(examen)
final = promedio(notas)
print(final)

# Funciones lambda
# funciones lambda son funciones anonimas, es decir, no tienen nombre
# son funciones que se pueden usar en una sola linea de codigo
# son funciones que se pueden usar como argumentos de otras funciones

nota_ = float(input("Digita la nota: "))

def cualitativa(nota):
    return nota + 0.5
cualitativa(nota_)
print(cualitativa(nota_))

nota_2 = float(input("Digita la nota: "))

cualitativa = lambda nota: nota + 0.5
cualitativa(nota_2)
print(cualitativa(nota_2))


n_1 = float(input("Digita la nota #1: "))
n_2 = float(input("Digita la nota #2: "))
n_3 = float(input("Digita la nota #3: "))

ponderado = lambda n1, n2, n3: (n1 * 3 + n2 * 2 + n3 * 5) / (3 + 2 + 5)
ponderado(n_1, n_2, n_3)
print(ponderado(n_1, n_2, n_3))
print(f"El promedio ponderado es: {ponderado(n_1, n_2, n_3)}")

# Mapeo de valores
notas = [6.5, 7.5, 5.5, 8.0]
notas_actualizadas = list(map(lambda x: x + 0.5, notas))
print(notas_actualizadas)
print(f"las notas originales son: {notas} y tuas notas actualizadas son: {notas_actualizadas}")
'''
temp_celsius = [0, 25, 37, 78, 100]
temp_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temp_celsius))
print(temp_fahrenheit)
