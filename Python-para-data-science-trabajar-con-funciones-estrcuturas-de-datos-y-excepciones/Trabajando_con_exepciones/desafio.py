# 1 - Haz un programa que solicite a la persona usuaria ingresar dos
# números decimales y calcular la división entre estos números. El código
# debe incluir un manejo de error, indicando el tipo de error que se
# generó si la división no es posible.
# Prueba el programa con el segundo valor numérico de la entrada igual a
# 0. También prueba usando caracteres textuales en la entrada para
# verificar los tipos de errores que ocurren.

try:
    num1_str = input("Ingrese el primer número decimal: ")
    num2_str = input("Ingrese el segundo número decimal: ")
    num1 = float(num1_str)  # Intenta convertir la primera entrada a float
    num2 = float(num2_str)  # Intenta convertir la segunda entrada a float
    resultado = num1 / num2  # Realiza la división
    print(f"El resultado de la división es: {resultado}")
except ValueError:
    print("Error: La entrada no es un número decimal válido.")  # Se genera si la conversión a float falla
except ZeroDivisionError:
    print("Error: No es posible dividir por cero.")  # Se genera si el segundo número es 0

# Anotaciones:
# - El bloque 'try' contiene el código que podría generar errores (ValueError si la entrada no es un número,
#   ZeroDivisionError si el segundo número es cero).
# - El bloque 'except ValueError' captura el error que ocurre al intentar convertir una cadena no numérica a float.
# - El bloque 'except ZeroDivisionError' captura el error que ocurre al intentar dividir por cero.
# - Si no ocurre ningún error en el bloque 'try', se ejecuta el 'else' (implícito aquí, ya que solo hay un 'print').

# 2 - Haz un programa que solicite a la persona usuaria ingresar un
# texto que será una clave a buscar en el siguiente diccionario: edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17},
# almacenando el resultado del valor en una variable. El código debe
# incluir un manejo de error KeyError, imprimiendo la información 'Nombre
# no encontrado' en caso de error, e imprimir el valor si no ocurre
# ninguno.
# Prueba el programa con un nombre presente en una de las claves del
# diccionario y con uno que no esté en el diccionario para verificar el
# mensaje de error.

edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nombre_buscado = input("Ingrese el nombre a buscar en el diccionario: ")
    edad_encontrada = edades[nombre_buscado]  # Intenta acceder al valor usando la clave ingresada
    print(f"La edad de {nombre_buscado} es: {edad_encontrada}")
except KeyError:
    print("Nombre no encontrado")  # Se genera si la clave ingresada no existe en el diccionario

# Anotaciones:
# - El bloque 'try' intenta acceder a un elemento del diccionario utilizando la clave proporcionada por el usuario.
# - El bloque 'except KeyError' captura el error que ocurre cuando la clave ingresada no se encuentra en el diccionario 'edades'.
# - Si la clave se encuentra, la edad correspondiente se almacena en 'edad_encontrada' y se imprime.

# 3 - Crea una función que reciba una lista como parámetro y convierta
# todos los valores de la lista a flotantes. La función debe incluir un
# manejo de error indicando el tipo de error generado y devolver la lista
# si no ha ocurrido ningún error. Por último, debe tener la cláusula finally para imprimir el texto: 'Fin de la ejecución de la función'.

def convertir_a_flotante(lista_entrada):
    """Convierte todos los valores de una lista a flotantes.

    Args:
        lista_entrada: La lista de valores a convertir.

    Returns:
        Una nueva lista con los valores convertidos a flotantes,
        o la lista original si no hubo errores.
    """
    try:
        lista_flotante = [float(elemento) for elemento in lista_entrada]  # Intenta convertir cada elemento a float
        return lista_flotante
    except ValueError:
        print("Error: Uno o más elementos de la lista no pueden ser convertidos a flotante.")  # Se genera si un elemento no es convertible
        return lista_entrada  # Devuelve la lista original en caso de error
    finally:
        print("Fin de la ejecución de la función")  # Se ejecuta siempre

# Anotaciones:
# - El bloque 'try' utiliza una comprensión de lista para intentar convertir cada elemento de la 'lista_entrada' a float.
# - El bloque 'except ValueError' captura el error que ocurre si algún elemento de la lista no puede ser convertido a un número flotante.
# - El bloque 'finally' se ejecuta siempre, tanto si ocurre un error como si no, imprimiendo el mensaje indicado.

# 4 - Crea una función que reciba dos listas como parámetros y agrupe
# los elementos uno a uno de las listas, formando una lista de tuplas de 3
# elementos. El primer y segundo elemento de la tupla son los valores en
# la posición i de las listas y el tercer elemento es la suma de los valores en la posición i de las listas.
# La función debe incluir un manejo de error indicando el tipo de error
# generado y devolver como resultado la lista de tuplas. Si las listas
# enviadas como parámetro tienen tamaños diferentes, la función debe
# devolver un IndexError con la frase: 'La cantidad de elementos en cada
# lista es diferente.'.
# Datos para probar la función:
# Valores sin error:
lista1_sin_error = [4, 6, 7, 9, 10]
lista2_sin_error = [-4, 6, 8, 7, 9]
# Listas con tamaños diferentes:
lista1_diff_size = [4, 6, 7, 9, 10, 4]
lista2_diff_size = [-4, 6, 8, 7, 9]
# Listas con valores incoherentes:
lista1_incoherente = [4, 6, 7, 9, 'A']
lista2_incoherente = [-4, 'E', 8, 7, 9]

def agrupar_y_sumar_listas(lista_a, lista_b):
    """Agrupa elementos de dos listas en tuplas de 3 elementos (a, b, a+b).

    Args:
        lista_a: La primera lista.
        lista_b: La segunda lista.

    Returns:
        Una lista de tuplas, o lanza un IndexError si las listas tienen
        tamaños diferentes, o un TypeError si los elementos no son sumables.
    """
    try:
        if len(lista_a) != len(lista_b):
            raise IndexError("La cantidad de elementos en cada lista es diferente.")
        lista_de_tuplas = []
        for i in range(len(lista_a)):
            suma = lista_a[i] + lista_b[i]  # Intenta sumar los elementos en la misma posición
            lista_de_tuplas.append((lista_a[i], lista_b[i], suma))
        return lista_de_tuplas
    except IndexError as e:
        return e  # Devuelve la excepción IndexError con el mensaje específico
    except TypeError:
        return "Error: Los elementos de las listas deben ser numéricos para poder sumarlos."

# Anotaciones:
# - El bloque 'try' primero verifica si las longitudes de las listas son diferentes. Si lo son, lanza un IndexError.
# - Luego, itera a través de los índices de las listas (asumiendo que tienen la misma longitud) y crea tuplas con el elemento
#   de cada lista en la posición actual y su suma.
# - El bloque 'except IndexError as e' captura el error de índice y devuelve la excepción con el mensaje.
# - El bloque 'except TypeError' captura el error que ocurre si los elementos de las listas no se pueden sumar (por ejemplo, intentar sumar un número y una cadena).

# 5 - Como desafío, se te ha asignado la tarea de desarrollar un código
# que contabiliza las puntuaciones de estudiantes de una institución
# educativa de acuerdo con sus respuestas en una prueba. Este código debe
# ser probado para un ejemplo de 3 estudiantes con una lista de listas en
# la que cada lista tiene las respuestas de 5 preguntas objetivas de cada
# estudiante. Cada pregunta vale un punto y las alternativas posibles son
# A, B, C o D.
# Si alguna alternativa en una de las pruebas no está entre las
# alternativas posibles, debes lanzar un ValueError con el mensaje "La
# alternativa [alternativa] no es una opción de alternativa válida". El
# cálculo de las 3 notas solo se realizará mediante las entradas con las
# alternativas A, B, C o D en todas las pruebas. Si no se lanza la
# excepción, se mostrará una lista con las notas en cada prueba.
# Datos para la prueba del código:
respuestas = ['D', 'A', 'B', 'C', 'A']
# A continuación, hay 2 listas de listas que puedes usar como prueba:
tests_sin_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
tests_con_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calcular_notas(tests, respuestas_correctas):
    """Calcula las puntuaciones de los estudiantes en una prueba.

    Args:
        tests: Una lista de listas, donde cada lista representa las
               respuestas de un estudiante.
        respuestas_correctas: Una lista con las respuestas correctas.

    Returns:
        Una lista con las puntuaciones de cada estudiante, o lanza un
        ValueError si se encuentra una alternativa inválida.
    """
    notas = []
    alternativas_validas = ['A', 'B', 'C', 'D']
    for estudiante_respuestas in tests:
        nota = 0
        for i, respuesta_estudiante in enumerate(estudiante_respuestas):
            if respuesta_estudiante not in alternativas_validas:
                raise ValueError(f"La alternativa '{respuesta_estudiante}' no es una opción de alternativa válida.")
            if respuesta_estudiante == respuestas_correctas[i]:
                nota += 1
        notas.append(nota)
    return notas

try:
    notas_sin_error = calcular_notas(tests_sin_ex, respuestas)
    print("Notas sin excepción:", notas_sin_error)
except ValueError as e:
    print("Error al calcular notas:", e)

try:
    notas_con_error = calcular_notas(tests_con_ex, respuestas)
    print("Notas con excepción:", notas_con_error)
except ValueError as e:
    print("Error al calcular notas:", e)

# Anotaciones:
# - La función 'calcular_notas' itera a través de las respuestas de cada estudiante.
# - Para cada respuesta, verifica si es una alternativa válida ('A', 'B', 'C', 'D'). Si no lo es, lanza un ValueError con un mensaje específico.
# - Si la alternativa es válida y coincide con la respuesta correcta en la misma posición, se incrementa la nota del estudiante.
# - Si todas las alternativas en todas las pruebas son válidas, la función devuelve una lista con las notas de cada estudiante.
# - Los bloques 'try-except' se utilizan para probar la función con datos que no generan excepción y con datos que sí la generan.

# 6 - Estás trabajando con procesamiento de lenguaje
# natural (NLP) y, en esta ocasión, tu líder te pidió que crees un
# fragmento de código que reciba una lista con las palabras separadas de
# una frase generada por ChatGPT.
# Necesitas crear una función que evalúe cada palabra de este texto y
# verifique si el tratamiento para quitar los símbolos de puntuación (',',
# '.', '!' y '?') se realizó. De lo contrario, se lanzará una excepción
# del tipo ValueError señalando el primer caso en que se detectó el uso de
# una puntuación a través de la frase "El texto presenta puntuaciones en
# la palabra "[palabra]"". Esta solicitud se centra en el análisis del
# patrón de frases generadas por la inteligencia artificial.
# Datos para probar el código:
lista_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso', 'versátil',
                  'y', 'fácil', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial']
lista_no_tratada = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación', 'poderoso,', 'versátil',
                  'y', 'fácil,', 'de', 'aprender', 'utilizado', 'en', 'diversos', 'campos,', 'desde',
                  'análisis', 'de', 'datos', 'hasta', 'inteligencia', 'artificial!']

def verificar_puntuacion(lista_palabras):
    """Verifica si hay símbolos de puntuación en una lista de palabras.

    Args:
        lista_palabras: Una lista de cadenas (palabras).

    Raises:
        ValueError: Si se encuentra un símbolo de puntuación en alguna palabra,
                    con un mensaje indicando la primera palabra con puntuación.
    """
    puntuaciones = [',', '.', '!', '?']
    for palabra in lista_palabras:
        for simbolo in puntuaciones:
            if simbolo in palabra:
                raise ValueError(f"El texto presenta puntuaciones en la palabra '{palabra}'")

try:
    verificar_puntuacion(lista_tratada)
    print("La lista tratada no presenta símbolos de puntuación.")
except ValueError as e:
    print("Error en la lista tratada:", e)

try:
    verificar_puntuacion(lista_no_tratada)
    print("La lista no tratada no presenta símbolos de puntuación.")
except ValueError as e:
    print("Error en la lista no tratada:", e)

# Anotaciones:
# - La función 'verificar_puntuacion' itera a través de cada palabra de la lista.
# - Para cada palabra, verifica si contiene alguno de los símbolos de puntuación definidos en la lista 'puntuaciones'.
# - Si se encuentra un símbolo de puntuación en una palabra, se lanza inmediatamente un ValueError con un mensaje específico que incluye la palabra infractora.
# - Los bloques 'try-except' se utilizan para probar la función con ambas listas, la tratada (que no debería generar error) y la no tratada (que sí debería generarlo).