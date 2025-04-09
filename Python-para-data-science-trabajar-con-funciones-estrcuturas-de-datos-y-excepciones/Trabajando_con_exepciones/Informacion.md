# 2048-python-para-data-science-trabajar-con-funciones
Este repositorio corresponde al entrenamiento de Python: Trabajar con funciones, estructuras de datos y funciones de Alura Latam.

### Para saber más: tipos de excepciones

En Python, básicamente existen dos formas distintas de errores: los de sintaxis y las excepciones. Las excepciones son una manera de manejar errores y situaciones inesperadas en el código, asegurando un flujo de ejecución más controlado.

Como científico de datos, deberás prestar atención a situaciones como estas para evitar errores o problemas en tus códigos y análisis que puedan afectar tanto la experiencia del usuario como la eficiencia de tu análisis.

Tipos de Excepciones

SyntaxError

Ocurre cuando el analizador detecta un error en la descripción del código. Normalmente, una flecha señala la parte del código que generó el error, como una especie de pista sobre dónde puede haber ocurrido el error.

print(10 / 2

Salida:

  File "<ipython-input-16-2db3afa07d68>", line 1
    print(10/2
              ^
SyntaxError: unexpected EOF while parsing

Observa que olvidamos cerrar el paréntesis y, por lo tanto, se presentó un error de sintaxis, es decir, de escritura de código.

NameError

Excepción lanzada cuando intentamos utilizar un nombre de algún elemento que no está presente en nuestro código.

raiz = sqrt(100)

Salida:

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-17-2e14e900fb9f> in <module>
----> 1 raiz = sqrt(100)

NameError: name 'sqrt' is not defined

En este caso, el intérprete no puede aplicar el método de la raíz cuadrada porque no se ha importado junto con la biblioteca math.

IndexError

Excepción lanzada cuando intentamos indexar alguna estructura de datos como lista, tupla o incluso una cadena más allá de sus límites.

lista = [1, 2, 3]
lista[4]

Salida:

---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-18-f5fe6d922eea> in <module>
      1 lista = [1, 2, 3]
----> 2 lista[4]

IndexError: list index out of range

Para esta situación, solo tenemos 3 elementos en la lista y tratamos de leer el elemento en la posición 4, que no existe. Recibimos el mensaje de que el índice está fuera de rango.

TypeError

Excepción lanzada cuando un operador o función se aplican a un objeto cuyo tipo es inapropiado.

"1" + 1

Salida:

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-20-ec358fc6499a> in <module>
----> 1 "1" + 1

TypeError: can only concatenate str (not "int") to str

Observa que intentamos "sumar" una cadena con un número entero y esto generó una excepción en nuestro código. Esto ocurrió por 2 razones: el operador de suma se consideró como concatenación porque comenzamos usando una cadena (en este caso, el signo de suma se utiliza para concatenar cadenas), y un valor de tipo entero no se puede concatenar en este tipo de operación.

KeyError

Excepción lanzada cuando intentamos acceder a una clave que no está en el diccionario presente en nuestro código.

estados = {'EM': 1, 'JC': 2, 'OA': 3}
estados["MI"]

Salida:

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-22-45729db26889> in <module>
      1 estados =  {'EM': 1, 'JC': 2, 'OA': 3}
----> 2 estados["MI"]

KeyError: 'MI'

Intentamos acceder a los datos del Estado MI (Michoacán), que no está presente en el diccionario, lanzando así la excepción.

Warning

Excepción lanzada en situaciones en las que necesitamos alertar al usuario sobre algunas condiciones del código. Estas condiciones no necesariamente interrumpen la ejecución del programa, pero pueden lanzar advertencias sobre el uso de módulos obsoletos, o que pueden ser obsoletos en futuras actualizaciones, o también para cambios que pueden repercutir en alguna parte del código.

Es importante recordar que, en el caso de los Warnings, pueden ser ignorados o tratados como excepciones.

import numpy as np

a = np.arange(5)
a / a  # presenta una advertencia

Salida:

<ipython-input-23-93a37b275923>:4: RuntimeWarning: invalid value encountered in true_divide
  a / a  # presenta una advertencia
array([nan,  1.,  1.,  1.,  1.])

Intentamos dividir cero por cero. En un array Numpy, que es esta estructura en la salida de la consola, este resultado genera un valor nan (Not a Number). Es decir, puedes seguir con la ejecución del programa, pero es probable que necesites procesar los datos para poder utilizar este array en alguna operación más adelante.

### Ventajas de las exepciones



Los errores en Python pueden ocurrir por diferentes motivos, desde errores de sintaxis hasta problemas de lógica en el código. Es importante saber identificar el tipo de error y su causa para que puedan corregirse de manera eficiente.

Podemos utilizar herramientas para identificar el origen de los errores y entender mejor el flujo de ejecución del programa. Además, las excepciones son una forma importante de manejar errores en Python.

Dicho esto, ¿cuál es la principal ventaja de utilizar excepciones en un proyecto de ciencia de datos en Python?

La principal ventaja de utilizar excepciones en un proyecto de ciencia de datos en Python radica en su capacidad para robustecer el código y hacerlo más tolerante a errores inesperados, permitiendo que el programa continúe su ejecución de manera controlada en lugar de detenerse abruptamente.

### Lo que aprendimos



Lo que aprendimos en esta aula:

    Identificar los tipos de errores y excepciones.
    Manejar las excepciones mediante las cláusulas try, except, else y finally.
    Generar nuestras propias excepciones para comportamientos indeseados en el código.



    Funciones nativas de Python: Imagina que Python es como una cocina muy bien equipada. Las funciones nativas son como los utensilios y electrodomésticos que ya vienen con la cocina, como cuchillos, ollas y una licuadora. No necesitas comprar nada extra para usarlos; simplemente los tomas y comienzas a cocinar. Así, puedes realizar tareas comunes sin complicaciones.

    Funciones definidas por el usuario: Ahora, piensa en que decides crear tu propia receta especial. Esta receta es como una función que tú defines. Puedes decidir qué ingredientes (parámetros) usar y qué resultado (valor de retorno) quieres obtener. Las funciones lambda son como recetas rápidas que puedes hacer en un instante, sin necesidad de seguir un proceso largo. Son ideales para esos momentos en que solo necesitas algo simple y rápido.

    Estructuras de datos: Imagina que tienes una caja de herramientas. Las listas son como un estante donde puedes colocar herramientas de diferentes tamaños y formas, las tuplas son como un conjunto de herramientas que siempre usas juntas y no quieres que se separen, y los diccionarios son como una caja de herramientas con etiquetas, donde cada herramienta tiene su lugar específico y puedes encontrarla fácilmente.

    Excepciones: Finalmente, piensa en un viaje en coche. A veces, puedes encontrar obstáculos en el camino, como un bache o un desvío. Las excepciones son como esos obstáculos; si no estás preparado para ellos, tu viaje puede verse interrumpido. Aprender a manejar excepciones es como tener un GPS que te avisa sobre los obstáculos y te sugiere rutas alternativas para que puedas continuar tu viaje sin problemas.
