'''
1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre]."
'''
nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}.")

'''
2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima "Hola, [nombre], tienes [edad] años."
'''
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
print(f"Hola, {nombre}, tienes {edad} años.")

'''
3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."'
'''
nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
altura = input("Escribe tu altura en metros: ")
print(f"Hola, {nombre}, tienes {edad} años y mides {altura} metros.")

''''
4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.'
'''
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}.")

''''
5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.'
'''
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
num3 = float(input("Escribe el tercer número: "))
suma = num1 + num2 + num3
print(f"La suma de {num1}, {num2} y {num3} es {suma}.")

'''''
6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.'
'''
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
resta = num1 - num2
print(f"La resta de {num1} menos {num2} es {resta}.")

'''
7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.'
'''
num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
multiplicacion = num1 * num2
print(f"La multiplicación de {num1} y {num2} es {multiplicacion}.")

''''
8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.'
'''
num1 = float(input("Escribe el numerador: "))
num2 = float(input("Escribe el denominador: "))
if num2 != 0:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es {division}.")

'''
9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.
'''
num1 = float(input("Escribe la base: "))
num2 = float(input("Escribe el exponente: "))
exponente = num1 ** num2
print(f"{num1} elevado a la {num2} es {exponente}.")

''''
10 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y realice la división entera entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.'
'''
num1 = float(input("Escribe el numerador: "))
num2 = float(input("Escribe el denominador: "))
if num2 != 0:
    division_entera = num1 // num2
    print(f"La división entera de {num1} entre {num2} es {division_entera}.")

'''
11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.
'''
num1 = float(input("Escribe el numerador: "))
num2 = float(input("Escribe el denominador: "))
if num2 != 0:
    resto = num1 % num2
    print(f"El resto de la división de {num1} entre {num2} es {resto}.")

'''
12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.
'''
nota1 = float(input("Escribe la primera nota: "))
nota2 = float(input("Escribe la segunda nota: "))
nota3 = float(input("Escribe la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de las notas es {promedio}.")

''''
13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.'
'''
numeros = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]
suma_numeros = sum(n * p for n, p in zip(numeros, pesos))
suma_pesos = sum(pesos)
promedio_ponderado = suma_numeros / suma_pesos
print(f"El promedio ponderado es {promedio_ponderado}.")

'''''
14 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.'
'''
frase = "Hola, soy un programa de Python."
print(frase)

'''''
15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.'
'''
frase = input("Escribe una frase: ")
print(frase)

'''''
16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.'
'''
frase = input("Escribe una frase: ")
print(frase.upper())

'''''
17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.'
'''
frase = input("Escribe una frase: ")
print(frase.lower())

'''
18 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase sin espacios en blanco al principio y al final.
'''
frase = "   Hola, soy un programa de Python.   "
print(frase.strip())

''''
19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada sin espacios en blanco al principio y al final.'
'''
frase = input("Escribe una frase: ")
print(frase.strip())

''''
20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final, además de convertirla a minúsculas.'
'''
frase = input("Escribe una frase: ")
print(frase.strip().lower())

''''
21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".'
'''
frase = input("Escribe una frase: ")
frase_modificada = frase.replace("e", "f")
print(frase_modificada)

''''
22 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "a" reemplazadas por el carácter "@".'
'''
frase = input("Escribe una frase: ")
frase_modificada = frase.replace("a", "@")
print(frase_modificada)

''''
23 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".'
'''
frase = input("Escribe una frase: ")
frase_modificada = frase.replace("s", "$")
print(frase_modificada)
