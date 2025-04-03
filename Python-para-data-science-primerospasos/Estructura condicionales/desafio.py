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