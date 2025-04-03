edad = 5
type(edad)
print(type(edad))
# type(edad) devuelve el tipo de dato de la variable edad

promedio = 5.5
type(promedio) 
print(type(promedio))
# type(promedio) devuelve el tipo de dato de la variable promedio

nombre = "Juan"
type(nombre)
print(type(nombre))
# type(nombre) devuelve el tipo de dato de la variable nombre

v = True
type(v)
print(type(v))
# type(v) devuelve el tipo de dato de la variable v

nombre_estudiante = "Juan Pérez"
edad_estudiante = 20
promedio_estudiante = 8.5
situacion_estudiante = True

print(nombre_estudiante, edad_estudiante, promedio_estudiante, situacion_estudiante)
print(type(nombre_estudiante), type(edad_estudiante), type(promedio_estudiante), type(situacion_estudiante))
# type() devuelve el tipo de dato de cada variable

### Variables int, float, str, bool
# int: enteros, float: decimales, str: cadenas de texto, bool: booleanos (True o False)
'''
cargo    Cantidad     Salario
Vigilante    5          300
Docente      16         500
Coordinador  2          600
'''

cant_vigilante = 5
salario_vigilante = 300

cant_docente = 16
salario_docente = 500

cant_Coordinador = 2
salario_Coordinador = 600   

total_empleados = cant_vigilante + cant_docente + cant_Coordinador
print("Total de empleados:", total_empleados)
# total_empleados almacena la suma de los empleados de cada cargo

diferencia_salario = salario_docente - salario_vigilante
print("Diferencia de salario entre docente y vigilante:", diferencia_salario)
# diferencia_salario almacena la diferencia entre el salario de los docentes y el de los vigilantes

promedio_salarios = (cant_vigilante * salario_vigilante + cant_docente * salario_docente + cant_Coordinador * salario_Coordinador) / total_empleados
print("Promedio de salarios:", promedio_salarios)
# promedio_salarios almacena el promedio de los salarios de todos los empleados
# Se puede hacer de la siguiente manera.

### variables str

t = "Alura"
print(type(t))
# type(t) devuelve el tipo de dato de la variable t

# practica con las variables str
texto = "  Micaela de los Sanyos " # cadena de texto con espacios al principio y al final, apellido mas escrito, debo de pasarlo a mayuscula y corregir el apellido.
print(id(texto))  # id(texto) devuelve la direccion de memoria de la variable texto
print(texto.upper()) # upper() convierte la cadena de texto a mayusculas.
print(texto.lower()) # lower() convierte la cadena de texto a minusculas.
print(texto.strip()) # strip() elimina los espacios al principio y al final de la cadena de texto.
print(texto.replace("Sanyos", "Santos")) # replace() reemplaza una cadena de texto por otra.

nuevo_texto = texto.strip().replace("Sanyos", "Santos").upper()
print(nuevo_texto) # imprime el nuevo texto con los cambios realizados.
print(id(nuevo_texto)) # id(nuevo_texto) devuelve la direccion de memoria de la variable nuevo_texto

### Ingreso de datos por teclado
# input() permite ingresar datos por teclado, devuelve una cadena de texto.

year_admision = input("Ingrese el año de admision: ")


# puedo definir el tipo de variable a los input() de la siguiente manera:
score_admision = float(input("Ingrese la nota de admision: "))
print(year_admision)
print(type(score_admision)) # type(year_admision) devuelve el tipo de dato de la variable year_admision

# como dar formato

print(f"\tEl año de admision es: {year_admision} \n\tLa nota de admision fue: {score_admision}") # f-string permite dar formato a la cadena de texto, se coloca una f antes de la cadena de texto y se pueden usar llaves para insertar variables dentro de la cadena.