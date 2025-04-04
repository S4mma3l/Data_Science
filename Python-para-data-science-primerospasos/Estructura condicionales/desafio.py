'''
# 1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.

num1 = float(input("Escribe el primer número: "))
num2 = float(input("Escribe el segundo número: "))
if num1 > num2:
    print(f"El número más grande es {num1}.")
else:
    print(f"El número más grande es {num2}.")

# 2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

porcentaje = float(input("Ingrese el porcentaje de crecimiento de producción: "))
if porcentaje > 50:
    print("Hubo un crecimiento en la producción.")
else:
    print("Hubo una disminución en la producción.")

# 3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.

letra = input("Ingrese una letra: ").lower()
if letra in "aeiou":
    print(f"La {letra} es una vocal.")
else:
    print(f"La {letra} es una consonante.")

# 4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.

precio_2022 = [20000, 18000, 22000]
precio_2023 = [17000, 19000, 21000]
precio_2024 = [15000, 16000, 18000]

if precio_2022 > precio_2023:
    print(f"El precio más alto es {precio_2022} que fue en 2022.")
elif precio_2023 > precio_2024:
    print(f"El precio más alto es {precio_2023} que fue en 2023.")
else:
    print(f"El precio más alto es {precio_2024} que fue en 2024.")

# 5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.

precio_producto1 = float(input("Ingrese el precio del producto 1: "))
precio_producto2 = float(input("Ingrese el precio del producto 2: "))
precio_producto3 = float(input("Ingrese el precio del producto 3: "))
if precio_producto1 < precio_producto2 and precio_producto1 < precio_producto3:
    print(f"El producto más barato es el producto 1 con un precio de {precio_producto1}.")
elif precio_producto2 < precio_producto1 and precio_producto2 < precio_producto3:
    print(f"El producto más barato es el producto 2 con un precio de {precio_producto2}.")
else:
    print(f"El producto más barato es el producto 3 con un precio de {precio_producto3}.")


# 6 - Escribe un programa que lea tres números y los muestre en orden descendente.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 >= num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1
else:
    mayor = num3
    if num1 >= num2:
        medio = num1
        menor = num2
    else:
        medio = num2
        menor = num1
print(f"Los números en orden descendente son: {mayor}, {medio}, {menor}.")


# 7 -Escribe un programa que pregunte en qué turno estudia la persona usuaria ("mañana", "tarde" o "noche") y muestre el mensaje "¡Buenos Días!", "¡Buenas Tardes!", "¡Buenas Noches!" o "Valor Inválido!", según el caso.
turno = input("¿En qué turno estudias? (mañana, tarde, noche): ").lower()
if turno == "mañana":
    print("¡Buenos Días!")
elif turno == "tarde":
    print("¡Buenas Tardes!")
elif turno == "noche":
    print("¡Buenas Noches!")
else:
    print("Valor Inválido!")


# 8 - Escribe un programa que solicite un número entero a la persona usuaria y determine si es par o impar. Pista: Puedes usar el operador módulo (%).

numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")



# 9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.
numero = input("Ingrese un número: ")

number = float(numero)
if number == int(number):
    print(f"{numero} es un número entero.")
else:
    print(f"{numero} es un número decimal.")'
    


# 10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.
numero1_str = input("Ingrese el primer número: ")
numero2_str = input("Ingrese el segundo número: ")

#intentamos hacer la conversion, y si falla, devolvemos un mensaje y detenemos el programa
if '.' in numero1_str:
  numero1_float = float(numero1_str)
else:
  numero1_float = int(numero1_str)

if '.' in numero2_str:
  numero2_float = float(numero2_str)
else:
  numero2_float = int(numero2_str)

operacion = input("¿Qué operación desea realizar? (+, -, *, /): ")

if operacion == "+":
    resultado = numero1_float + numero2_float
elif operacion == "-":
    resultado = numero1_float - numero2_float
elif operacion == "*":
    resultado = numero1_float * numero2_float
elif operacion == "/":
    resultado = numero1_float / numero2_float
else:
    print("Operación no válida.")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)
    if resultado == int(resultado):
        print("El resultado es entero.")
    else:
        print("El resultado es decimal.")

    if resultado >= 0:
        print("El resultado es positivo.")
    else:
        print("El resultado es negativo.")

    if resultado == int(resultado): #solo verificamos paridad si es entero.
      if int(resultado) % 2 == 0:
          print("El resultado es par.")
      else:
          print("El resultado es impar.")

    #Informacion numero1:

    if numero1_float >= 0:
        print("El numero 1 es positivo.")
    else:
        print("El numero 1 es negativo.")
    if numero1_float == int(numero1_float):
      print("El numero 1 es entero")
    else:
      print("El numero 1 es decimal")

    if numero1_float == int(numero1_float):
      if int(numero1_float) %2 == 0:
        print("El numero 1 es par.")
      else:
        print("El numero 1 es impar.")

    #informacion numero 2

    if numero2_float >= 0:
        print("El numero 2 es positivo.")
    else:
        print("El numero 2 es negativo.")
    if numero2_float == int(numero2_float):
      print("El numero 2 es entero")
    else:
      print("El numero 2 es decimal")
    if numero2_float == int(numero2_float):
      if int(numero2_float) %2 == 0:
        print("El numero 2 es par.")
      else:
        print("El numero 2 es impar.")



# 11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:

    # Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
    # Triángulo Equilátero: tres lados iguales;
    # Triángulo Isósceles: dos lados iguales;
    # Triángulo Escaleno: tres lados diferentes.

lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print(f"El triángulo es equilátero. {int(lado1)}, {int(lado2)}, {int(lado3)}")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(f"El triángulo es isósceles. {int(lado1)}, {int(lado2)}, {int(lado3)}")
    else:
        print(f"El triángulo es escaleno. {int(lado1)}, {int(lado2)}, {int(lado3)}")'
        


# 12 - Un establecimiento está vendiendo combustibles con descuentos variables. Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros, el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

    # El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
    # El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros menos el valor del descuento resultante del cálculo.

litros = float(input("Ingrese la cantidad de litros vendidos: "))
tipo_combustible = input("Ingrese el tipo de combustible (E para etanol, D para diésel): ").upper()

if tipo_combustible == "E":
    precio_litro = 1.70
    if litros <= 15:
        descuento = 0.02
    else:
        descuento = 0.04
elif tipo_combustible == "D":
    precio_litro = 2.00
    if litros <= 15:
        descuento = 0.03
    else:
        descuento = 0.05
else:
    print("Tipo de combustible no válido.")
    exit()

valor_descuento = precio_litro * litros * descuento
valor_total = precio_litro * litros - valor_descuento

print(f"Valor a pagar: R$ {int(valor_total)} tu descuento es de R$ {int(valor_descuento)}.")

'''

# 13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales para ayudar a la dirección en la toma de decisiones. El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual. A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

    # Para una variación superior al 20%: bonificación para el equipo de ventas.
    # Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
    # Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
    # Para bonificaciones inferiores al -10%: recorte de gastos.

ventas_2022 = int(input("Ingrese la cantidad de ventas en 2022: "))
ventas_2023 = int(input("Ingrese la cantidad de ventas en 2023: "))

variacion_porcentual = ((ventas_2023 - ventas_2022) / ventas_2022) * 100

print(f"Variación porcentual: {int(variacion_porcentual)}%")

if variacion_porcentual > 20:
    print("Bonificación para el equipo de ventas.")
elif 2 <= variacion_porcentual <= 20:
    print("Pequeña bonificación para el equipo de ventas.")
elif -10 <= variacion_porcentual < 2:
    print("Planificación de políticas de incentivo a las ventas.")
else:
    print("Recorte de gastos.")