# 1 - Crea un código para imprimir la suma de los elementos de cada una de las listas contenidas en la siguiente lista:
lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]

for lista in lista_de_listas:
    suma = sum(lista)  # La función sum() calcula la suma de los elementos de una lista.
    print(f"La suma de los elementos de {lista} es: {suma}")

# 2 - Crea un código para generar una lista que almacene el tercer elemento de cada tupla contenida en la siguiente lista de tuplas:
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

tercer_elemento = [tupla[2] for tupla in lista_de_tuplas]
# Comprensión de lista: itera sobre cada tupla y extrae el elemento en el índice 2 (el tercero).
print(f"Lista con el tercer elemento de cada tupla: {tercer_elemento}")

# 3 - A partir de la lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crea un código para generar una lista de tuplas
#     en la que cada tupla tenga el primer elemento como la posición del nombre en la lista original y el segundo elemento siendo el propio nombre.
lista_nombres = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']

lista_de_tuplas_con_indice = [(indice, nombre) for indice, nombre in enumerate(lista_nombres)]
# Comprensión de lista:
# enumerate() genera pares de índice y elemento para cada elemento en la lista.
# Para cada par (indice, nombre), crea una tupla (indice, nombre).
print(f"Lista de tuplas con índice y nombre: {lista_de_tuplas_con_indice}")

# 4 - Crea una lista usando la comprensión de listas (list comprehension) que almacene solo el valor numérico de cada tupla
#     en caso de que el primer elemento sea 'Apartamento', a partir de la siguiente lista de tuplas:
alquiler = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

precios_apartamentos = [precio for tipo, precio in alquiler if tipo == 'Apartamento']
# Comprensión de lista:
# Itera sobre cada tupla (tipo, precio) en la lista 'alquiler'.
# Si el 'tipo' es igual a 'Apartamento', agrega el 'precio' a la nueva lista.
print(f"Lista de precios de apartamentos: {precios_apartamentos}")

# 5 - Crea un diccionario usando la comprensión de diccionarios (dict comprehension) en el que las claves estén en la lista
#     meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
#     y los valores estén en gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
gasto = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

gastos_por_mes = {mes: valor for mes, valor in zip(meses, gasto)}
# Comprensión de diccionario:
# zip(meses, gasto) crea un iterador de tuplas donde el primer elemento de cada tupla proviene de 'meses'
# y el segundo de 'gasto'.
# Para cada par (mes, valor), crea una entrada en el diccionario con 'mes' como clave y 'valor' como valor.
print(f"Diccionario de gastos por mes: {gastos_por_mes}")

# 6 - Una tienda tiene una base de datos con la información de venta de cada representante y de cada año y necesita
#     filtrar solo los datos del año 2022 con ventas mayores a 6000. La tienda proporcionó una muestra con solo las
#     columnas de los años y los valores de venta para que puedas ayudar a realizar la filtración de los datos a través de un código:
ventas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141),
          ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471),
          ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

ventas_2022_mayores_6000 = [venta for ano, venta in ventas if ano == '2022' and venta > 6000]
# Comprensión de lista:
# Itera sobre cada tupla (ano, venta) en la lista 'ventas'.
# Si el 'ano' es '2022' y la 'venta' es mayor que 6000, agrega la tupla a la nueva lista.
print(f"Ventas de 2022 mayores a 6000: {ventas_2022_mayores_6000}")

# 7 - Una clínica analiza datos de pacientes y almacena el valor numérico de la glucosa en una base de datos y le gustaría
#     etiquetar los datos de la siguiente manera:
#
#     Glucosa igual o inferior a 70: 'Hipoglicemia'
#     Glucosa entre 70 y 99: 'Normal'
#     Glucosa entre 100 y 125: 'Alterada'
#     Glucosa superior a 125: 'Diabetes'
#
# La clínica proporcionó parte de los valores y tu tarea es crear una lista de tuplas usando la comprensión de listas
#     que contenga la etiqueta y el valor de la glucemia en cada tupla.
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

etiquetas_glucemia = [(
    'Hipoglicemia' if valor <= 70 else
    'Normal' if 70 < valor <= 99 else
    'Alterada' if 100 <= valor <= 125 else
    'Diabetes',
    valor
) for valor in glicemia]
# Comprensión de lista con expresiones condicionales anidadas:
# Itera sobre cada 'valor' en la lista 'glicemia'.
# Evalúa una serie de condiciones para asignar la etiqueta correcta y crea una tupla (etiqueta, valor).
print(f"Etiquetas de glucemia: {etiquetas_glucemia}")

# 8 - Un comercio electrónico tiene información de id de venta, cantidad vendida y precio del producto divididos en las
#     siguientes listas:
id_venta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cantidad = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
precio = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

encabezado = ('id', 'cantidad', 'precio', 'total')
datos_venta = [(i, cant, prec, cant * prec) for i, cant, prec in zip(id_venta, cantidad, precio)]
# Comprensión de lista:
# zip(id_venta, cantidad, precio) crea un iterador de tuplas con los elementos correspondientes de cada lista.
# Para cada tupla (i, cant, prec), calcula el 'total' y crea una nueva tupla (i, cant, prec, total).
tabla_venta = [encabezado] + datos_venta  # Combina el encabezado con los datos.
print("Tabla de ventas:")
for fila in tabla_venta:
    print(fila)

# 9 - Una empresa tiene sucursales distribuidas en los estados de la región Sudeste de Brasil. En una de las tablas de
#     registro de las sucursales, hay una columna que contiene la información de a qué estado pertenece:
estados = ['CMX', 'OAX', 'PUE', 'PUE', 'CMX', 'PUE', 'OAX', 'OAX', 'OAX', 'CMX', 'CMX', 'PUE', 'OAX', 'CMX', 'VER',
           'PUE', 'VER', 'CMX', 'PUE', 'CMX', 'OAX', 'CMX', 'PUE']

# Opción 1: Sin paso intermedio (más conciso)
conteo_estados = {estado: estados.count(estado) for estado in set(estados)}
# Comprensión de diccionario:
# set(estados) crea un conjunto de los estados únicos, eliminando duplicados.
# Para cada 'estado' único, cuenta cuántas veces aparece en la lista original 'estados' usando estados.count(estado).

# Opción 2: Con paso intermedio (como se sugiere en la pista)
lista_de_listas_estados = [[estado] * estados.count(estado) for estado in set(estados)]
# Comprensión de lista:
# Para cada 'estado' único en set(estados), crea una sublista que contiene ese 'estado' repetido
# la misma cantidad de veces que aparece en la lista original.
# print(f"Lista de listas de estados: {lista_de_listas_estados}") # Para ver el paso intermedio

conteo_estados_v2 = {lista[0]: len(lista) for lista in lista_de_listas_estados}
# Comprensión de diccionario:
# Itera sobre cada sublista en 'lista_de_listas_estados'.
# La clave del diccionario es el primer (y único) elemento de la sublista (el nombre del estado).
# El valor es la longitud de la sublista (la cantidad de veces que aparece el estado).

print(f"Conteo de sucursales por estado: {conteo_estados}")
print(f"Conteo de sucursales por estado (v2): {conteo_estados_v2}") # Mismo resultado que la opción 1

# 10 - En esa misma tabla de registro de sucursales, hay una columna con la información de la cantidad de personas empleadas
#      y el gerente quisiera tener un agrupamiento de la suma de esas personas para cada estado. Las informaciones
#      contenidas en la tabla son:
empleados = [('CMX', 16), ('OAX', 8), ('PUE', 9), ('PUE', 6), ('CMX', 10), ('PUE', 4), ('OAX', 9), ('OAX', 7),
             ('OAX', 12), ('CMX', 7), ('CMX', 11), ('PUE', 8), ('OAX', 8), ('CMX', 9), ('VER', 13), ('PUE', 5),
             ('VER', 9), ('CMX', 12), ('PUE', 10), ('CMX', 7), ('OAX', 14), ('CMX', 10), ('PUE', 12)]

# Diccionario con listas de empleados por estado
empleados_por_estado_lista = {}
for estado, cantidad in empleados:
    if estado not in empleados_por_estado_lista:
        empleados_por_estado_lista[estado] = []
    empleados_por_estado_lista[estado].append(cantidad)
print(f"Lista de empleados por estado: {empleados_por_estado_lista}")

# Diccionario con la suma de empleados por estado
suma_empleados_por_estado = {}
for estado, cantidad in empleados:
    if estado not in suma_empleados_por_estado:
        suma_empleados_por_estado[estado] = 0
    suma_empleados_por_estado[estado] += cantidad
print(f"Suma de empleados por estado: {suma_empleados_por_estado}")