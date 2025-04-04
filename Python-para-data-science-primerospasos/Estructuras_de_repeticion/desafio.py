'''
# 1 - Escribe un programa que solicite dos números enteros e imprima todos los números enteros entre ellos.
nuevo_numero_1 = int(input("Ingrese el primer número entero: "))
nuevo_numero_2 = int(input("Ingrese el segundo número entero: "))

for numero in range(nuevo_numero_1, nuevo_numero_2 + 1):
    print(numero)



# 2 - Escribe un programa para calcular cuántos días tomará que la colonia de una bacteria A supere o iguale a la colonia de una bacteria B, basado en tasas de crecimiento del 3% y 1.5%, respectivamente. Supón que la colonia A comienza con 4 elementos y B con 10.
colonia_a = 4
colonia_b = 10
dias = 0

while colonia_a < colonia_b:
    colonia_a = colonia_a + colonia_a * 0.03
    colonia_b = colonia_b + colonia_b * 0.015
    dias = dias + 1

print(f"Tomará {dias} días para que la colonia A supere o iguale a la colonia B.")

# 3 - Para procesar una cantidad de 15 datos de evaluaciones de usuarios de un servicio de la empresa, necesitamos verificar si las calificaciones son válidas. Por lo tanto, escribe un programa que recibirá calificaciones del 0 al 5 y verificará si son valores válidos. Si se ingresa una calificación superior a 5 o inferior a 0, se repetirá hasta que el usuario ingrese un valor válido.

calificaciones = []
contador = 1
for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del usuario #{contador}: "))
    while calificacion < 0 or calificacion > 5:
        print("Calificación inválida. Debe estar entre 0 y 5.")
        calificacion = float(input(f"Ingrese la calificación del usuario #{contador}: "))
    calificaciones.append(calificacion)
    contador += 1
print(f"Las calificaciones válidas son: {int(calificaciones)}")
'

# 4 - Desarrolla un programa que lea un conjunto indefinido de temperaturas en grados Celsius y calcule su promedio. La lectura debe detenerse al ingresar el valor -273°C.

temperaturas = []
temperatura = float(input("Ingrese una temperatura en grados Celsius (-273 para finalizar): "))

while temperatura != -273:
    temperaturas.append(temperatura)
    temperatura = float(input("Ingrese otra temperatura en grados Celsius (-273 para finalizar): "))

if temperaturas:  # Verifica si la lista no está vacía
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"El promedio de las temperaturas ingresadas es: {promedio} °C")
else:
    print("No se ingresaron temperaturas.")

# 5 - Escribe un programa que calcule el factorial de un número entero proporcionado por el usuario. Recuerda que el factorial de un número entero es el producto de ese número por todos sus antecesores hasta llegar al número 1. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.

numero = int(input("Ingrese un número entero: "))
factorial = 1

if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")

# 6 - Escribe un programa que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 2, la tabla de multiplicar debe mostrarse en el siguiente formato:
numero = int(input("Ingrese un número entero: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7 - Los números primos tienen diversas aplicaciones en Ciencia de Datos, como en criptografía y seguridad. Un número primo es aquel que es divisible solo por sí mismo y por 1. Por lo tanto, crea un programa que solicite un número entero y determine si es un número primo o no.
numero = int(input("Ingrese un número entero: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

#  8 - Vamos a comprender la distribución de edades de los pensionistas de una empresa de seguros. Escribe un programa que lea las edades de una cantidad no informada de clientes y muestre la distribución en los intervalos [0-25], [26-50], [51-75] y [76-100]. La entrada de datos se detendrá al ingresar un número negativo.

edades = []
edad = 0

while edad >= 0:
    edad = int(input("Ingrese la edad de un cliente (número negativo para finalizar): "))
    if edad >= 0:
        edades.append(edad)

intervalos = [0, 0, 0, 0]  # [0-25], [26-50], [51-75], [76-100]

for edad in edades:
    if 0 <= edad <= 25:
        intervalos[0] += 1
    elif 26 <= edad <= 50:
        intervalos[1] += 1
    elif 51 <= edad <= 75:
        intervalos[2] += 1
    elif 76 <= edad <= 100:
        intervalos[3] += 1

print("Distribución de edades:")
print(f"[0-25]: {intervalos[0]} clientes")
print(f"[26-50]: {intervalos[1]} clientes")
print(f"[51-75]: {intervalos[2]} clientes")
print(f"[76-100]: {intervalos[3]} clientes")'
'''
# 9 - En una elección para la gerencia de una empresa con 20 empleados, hay cuatro candidatos. Escribe un programa que calcule al ganador de la elección. La votación se realizó de la siguiente manera:

# Cada empleado votó por uno de los cuatro candidatos (representados por los números 1, 2, 3 y 4).

# También se contaron los votos nulos (representados por el número 5) y los votos en blanco (representados por el número 6).

# Al final de la votación, el programa debe mostrar el número total de votos para cada candidato, los votos nulos y los votos en blanco. Además, debe calcular y mostrar el porcentaje de votos nulos con respecto al total de votos y el porcentaje de votos en blanco con respecto al total de votos.

votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0
votos_candidato4 = 0
votos_nulos = 0
votos_blanco = 0

for i in range(20):
    voto = int(input(f"Ingrese el voto del empleado {i+1} (1-4 candidatos, 5 nulo, 6 blanco): "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    elif voto == 4:
        votos_candidato4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_blanco += 1
    else:
        print("Voto inválido. Se contará como nulo.")
        votos_nulos += 1

total_votos = votos_candidato1 + votos_candidato2 + votos_candidato3 + votos_candidato4 + votos_nulos + votos_blanco

porcentaje_nulos = (votos_nulos / total_votos) * 100
porcentaje_blanco = (votos_blanco / total_votos) * 100

print("\nResultados de la elección:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")
print(f"Candidato 4: {votos_candidato4} votos")
print(f"Votos nulos: {votos_nulos} ({porcentaje_nulos:.2f}%)")
print(f"Votos en blanco: {votos_blanco} ({porcentaje_blanco:.2f}%)")