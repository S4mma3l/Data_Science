import os
import random
import numpy as np

# 1 - Instalar matplotlib versión 3.7.1
# Nota: La instalación de paquetes se realiza generalmente desde la terminal, no dentro de un script de Python.

# Desde la terminal:
# pip install matplotlib==3.7.1


# 2 - Importar numpy con el alias np
# Hecho al principio del script: import numpy as np


# 3 - Elegir un número al azar de una lista
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_aleatorio = random.choice(lista)
print(f"3. Número aleatorio de la lista: {numero_aleatorio}")


# 4 - Generar un número entero aleatorio menor que 100
numero_entero_aleatorio = random.randint(0, 99)
print(f"4. Número entero aleatorio (<100): {numero_entero_aleatorio}")


# 5 - Calcular la potencia de dos números enteros
while True:
    try:
        numero1 = int(input("Ingresa el primer número entero: "))
        numero2 = int(input("Ingresa el segundo número entero: "))
        potencia = numero1 ** numero2
        print(f"5. {numero1} elevado a {numero2} es: {potencia}")
        break  # Sale del bucle si la entrada es válida
    except ValueError:
        print("Error: Ingresa números enteros válidos.")

### aplicando a proyectos

import random
import math

# 6 - Sortear un seguidor de una red social
num_participantes = int(input("Ingresa el número de participantes del sorteo: "))
ganador = random.randint(1, num_participantes)
print(f"6. El ganador es el participante número: {ganador}")


# 7 - Generar token de acceso para una aplicación
nombre_usuario = input("Ingresa tu nombre de usuario: ")
token_generado = random.randrange(1000, 9999, 2)
print(f"7. Hola, {nombre_usuario}, tu token de acceso es {token_generado}. ¡Bienvenido/a!")


# 8 - Ensalada de frutas sorpresa
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
ensalada = random.sample(frutas, 3)
print(f"8. Ensalada de frutas sorpresa: {', '.join(ensalada)}")

# 9 - Raíz cuadrada de números enteros
numeros = [2, 8, 15, 23, 91, 112, 256]
raices_enteras = []

for num in numeros:
    raiz = math.sqrt(num)
    if raiz.is_integer():
        raices_enteras.append(int(raiz))

print(f"9. Raíces cuadradas enteras: {raices_enteras}")

#10 - Calcular el precio del cesped.
radio = float(input("Ingrese el radio del jardín circular en metros: "))
area = math.pi*(radio**2)
costo_metro_cuadrado = 25.00
costo_total = area * costo_metro_cuadrado

print(f"10. El área del jardín es de {area:.2f} metros cuadrados")
print(f"10. El costo total del césped es de: R${costo_total:.2f}")
