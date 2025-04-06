# 2048-python-para-data-science-trabajar-con-funciones
Este repositorio corresponde al entrenamiento de Python: Trabajar con funciones, estructuras de datos y funciones de Alura Latam.

## Que son las built-in functions?

Las funciones incorporadas, o funciones integradas, proporcionan una serie de funcionalidades básicas para la aplicación de tareas e instrucciones en el lenguaje Python. Son muy útiles en Data Science por la facilidad de uso y abstracción en tareas que pueden ser complejas, como ordenaciones de lista o manipulación de cadenas.

Con esto en mente, ¿Describe qué son las funciones incorporadas en Python y otras ventajas de su uso?

Son funciones que Python proporciona automáticamente y que están listas para usar en cualquier programa de Python.
Cubren una amplia gama de funcionalidades, desde operaciones matemáticas básicas hasta manipulación de cadenas y estructuras de datos.
Ejemplos comunes incluyen print(), len(), sum(), max(), min(), type(), int(), str(), y muchos más.

Facilidad de uso:

    Están disponibles de inmediato, lo que simplifica el desarrollo y reduce la necesidad de escribir código adicional.

## Para saber más: alcance de una variable

En Python, el alcance (o "escopo") de una variable está definido por la región del código donde puede ser accedida. En el caso de una función, el alcance se puede dividir en dos categorías: alcance global y alcance local.

El alcance global es el espacio en el cual una variable puede ser accedida por cualquier función o código que se esté ejecutando en el programa. Por otro lado, el alcance local es el espacio en el cual la variable solo puede ser accedida por la función en la que fue definida.

El problema de alcance ocurre cuando una variable se define dentro del alcance de una función y luego se referencia fuera del alcance de la función. En este caso, Python genera un mensaje de error, indicando que la variable no ha sido definida (NameError).

A continuación, se presenta un ejemplo que ilustra este comportamiento. Inicialmente, crearemos una variable x fuera de la función suma(), en la cual definimos otra variable y y, finalmente, imprimimos la suma de las dos variables.

x = 7

def suma():
  y = 9
  print(x + y)

Observa que x es nuestra variable definida en el alcance global, y es la variable definida en el alcance local de la función suma(). Cuando intentamos ejecutar nuestra función, la suma se realiza normalmente:

suma()

Salida:

16

Sin embargo, Python genera un error cuando intentamos imprimir la suma de x e y fuera del alcance de la función, ya que la variable y solo existe dentro de la función suma().

print(x + y)

Salida:

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-f09a7b03ddbf> in <module>
----> 1 print(x + y)

NameError: name 'y' is not defined

Para corregir este error, podemos convertir y en una variable global o devolver su valor en la función y asignarlo a una variable externa. En el próximo vídeo, aprenderemos cómo proceder en este tipo de situaciones.

## Para saber más: documentando funciones

Es importante hacer que nuestro código o análisis de datos sea lo más accesible posible para el público. Una de las formas de lograr este propósito es documentar las funciones. Podemos ayudar a quienes leen nuestro proyecto o utilizan las funciones que hemos desarrollado a entender qué tipos de variables podemos usar, si hay o no valores predeterminados o incluso describir de manera sucinta lo que hace ese fragmento de código.

Aquí, te pedimos que sigas este paso a paso en la documentación de la función de media que construimos durante la clase. Será requerida nuevamente más adelante en nuestros estudios.

Type Hint

Type Hint es una sintaxis utilizada en Python para indicar el tipo de dato esperado de un parámetro o el retorno de una función, ayudando en la legibilidad y mantenimiento del código. Podemos decir, en pocas palabras, que es una sugerencia de tipado de datos.

Formato:

def <nombre>(<param>: <tipo_param>) -> <tipo_retorno>:
  <instrucciones>
  return resultado

Aplicando esto a nuestro ejemplo de la función media(), podemos usar Type Hint de la siguiente manera:

# nuestra función recibe una lista del tipo list y retorna una variable del tipo float
def media(lista: list) -> float:
  calculo = sum(lista) / len(lista)
  return calculo

Si escribimos la función media() en otra celda y pasamos el ratón por encima, podemos observar la sugerencia de tipo de los parámetros de entrada y salida de la función.

Default Value

En Python, Default Value es un valor predeterminado asignado a un argumento de función que se utiliza si el usuario no proporciona ningún valor.

Formato:

<nombre_variable>: <tipo_variable> = <valor_variable>

Extendiendo nuestra función media(), podemos usar el valor predeterminado de la siguiente manera:

# nuestra función recibe una lista del tipo list y retorna una variable del tipo float
# si no recibe ningún valor de parámetro, se pasará una lista con un único
# elemento, siendo este cero
def media(lista: list=[0]) -> float:
  calculo = sum(lista) / len(lista)
  return calculo

De la misma manera que hicimos con Type Hint, si escribimos la función media() en otra celda y pasamos el ratón por encima, podemos observar la sugerencia de tipo de los parámetros de entrada y salida de la función, así como el valor predeterminado para nuestra lista si el usuario no proporciona ningún valor durante la ejecución.

Si ejecutamos la función media, esta será la salida:

0.0

Docstring

Finalmente, tenemos el Docstring, que es una cadena literal utilizada para documentar módulos, funciones, clases o métodos en Python. Se coloca como el primer elemento de la definición y se puede acceder utilizando la función help().

El Docstring debe describir el propósito, los parámetros, el tipo de retorno y las excepciones que puede generar la función. Es una buena práctica de programación utilizar Docstrings en tu código para facilitar la lectura, el mantenimiento y el intercambio de código con otros desarrolladores.

Formato:

def <nombre>(<param_1>, <param_2>, ..., <param_n>):
    '''Texto documentando su función...
    '''
  <instrucciones>
  return resultado

Concluyendo la implementación de nuestra función media(), podemos usar el Docstring de la siguiente manera:

def media(lista: list=[0]) -> float:
  '''Función para calcular la media de notas pasadas por una lista

  lista: list, default [0]
    Lista con las notas para calcular la media
  return = calculo: float
    Media calculada
  '''
  calculo = sum(lista) / len(lista)
  return calculo

Si ejecutamos el código help(media) en otra celda, obtenemos la siguiente salida:

Help on function media in module __main__:

media(lista: list = [0]) -> float
    Función para calcular la media de notas pasadas por una lista

    lista: list, default [0]
      Lista con las notas para calcular la media
    return = calculo: float
      Media calculada

Te dejamos el enlace a un artículo, en inglés, que explica algunos conceptos sobre la documentación de código en Python. https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49


### Lo que aprendimos



Lo que aprendimos en esta aula:

    Comprender qué son las funciones integradas (built-in functions) y cómo usarlas.
    Crear funciones con y sin parámetros de entrada.
    Crear funciones con y sin retorno de valores.
    Documentar las funciones utilizando Type hint, valor predeterminado (default value) y docstring.
    Comprender y crear funciones anónimas (Lambda Functions).

