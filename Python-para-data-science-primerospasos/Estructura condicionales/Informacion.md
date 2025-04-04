# Para saber más: operadores relacionales

Una condición no es más que una comparación entre datos a partir de la cual podemos obtener el resultado verdadero o falso de una condición. La comparación puede realizarse mediante operadores relacionales cuya misión es comparar valores y determinar si una expresión es verdadera o falsa. A continuación, conoceremos los operadores lógicos y cómo utilizarlos.

Mayor que (>)

Devuelve verdadero si el valor a la izquierda del símbolo es mayor que el de la derecha. Su sintaxis, valor_1 > valor_2, representa una comparación que solo será verdadera si valor_1 es mayor que valor_2. Con este operador relacional, podemos verificar si una persona es mayor que otra al comparar sus edades, como se muestra en el siguiente ejemplo:

edad_maria = int(input('Ingrese la edad de María: '))
edad_beatriz = int(input('Ingrese la edad de Beatriz: '))

if edad_maria > edad_beatriz:
  print('María es mayor que Beatriz.')

El operador mayor que (>) devuelve un valor falso si los valores comparados son iguales o si el valor a la izquierda del símbolo es inferior al de la derecha.

Menor que (<)

Devuelve verdadero si el valor a la izquierda del símbolo es menor que el de la derecha. Su sintaxis es valor_1 < valor_2. Esta comparación solo será verdadera si valor_1 es menor que valor_2. Con este operador relacional, también podemos verificar si una persona es menor que otra al comparar sus edades, como se muestra a continuación:

edad_maria = int(input('Ingrese la edad de María: '))
edad_beatriz = int(input('Ingrese la edad de Beatriz: '))

if edad_maria < edad_beatriz:
  print('María es menor que Beatriz.')

Este operador también devuelve un valor falso si los valores comparados son iguales o si el valor a la izquierda del símbolo es superior al de la derecha.

Mayor o igual a (>=)

Devuelve verdadero si el valor a la izquierda del símbolo es mayor o igual al valor a la derecha. Su sintaxis es valor_1 >= valor_2. Esta comparación solo será verdadera si valor_1 es mayor o igual a valor_2. Con este operador relacional, podemos verificar, por ejemplo, si una empresa tiene una cantidad mayor o igual a la de otra, como se muestra a continuación:

empleados_empresa_1 = int(input('Ingrese la cantidad de empleados de la empresa 1: '))
empleados_empresa_2 = int(input('Ingrese la cantidad de empleados de la empresa 2: '))

if empleados_empresa_1 >= empleados_empresa_2:
  print('La empresa 1 tiene una cantidad de empleados mayor o igual a la empresa 2.')

Menor o igual a (<=)

Devuelve verdadero si el valor a la izquierda del símbolo es menor o igual al valor de la derecha. Su sintaxis es valor_1 <= valor_2. Esta comparación solo será verdadera si valor_1 es menor o igual a valor_2. Con este operador relacional, podemos verificar si una empresa tiene una cantidad menor o igual a otra, como se muestra a continuación:

empleados_empresa_1 = int(input('Ingrese la cantidad de empleados de la empresa 1: '))
empleados_empresa_2 = int(input('Ingrese la cantidad de empleados de la empresa 2: '))

if empleados_empresa_1 <= empleados_empresa_2:
  print('La empresa 1 tiene una cantidad de empleados menor o igual a la empresa 2.')

Igual a (==)

Devuelve verdadero si el valor a la izquierda del símbolo es igual al valor de la derecha. Su sintaxis, valor_1 == valor_2, representa una comparación que solo será verdadera si valor_1 es igual a valor_2. Con este operador relacional, podemos verificar si dos libros tienen el mismo título mediante una comparación de cadenas, como se muestra en el siguiente ejemplo:

libro_1 = input('Ingrese el título del 1° libro: ')
libro_2 = input('Ingrese el título del 2° libro: ')

if libro_1 == libro_2:
  print('Los libros tienen el mismo título.')

También es posible realizar esta comparación con valores numéricos.

Diferente de (!=)

Devuelve verdadero si el valor a la izquierda del símbolo es diferente del valor a la derecha. Su sintaxis, valor_1 != valor_2, representa una comparación que solo será verdadera si valor_1 es diferente de valor_2. Este operador es el inverso de ==. Con él, podemos verificar si dos libros tienen títulos diferentes mediante una comparación de cadenas, como se muestra a continuación:

libro_1 = input('Ingrese el título del 1° libro: ')
libro_2 = input('Ingrese el título del 2° libro: ')

if libro_1 != libro_2:
  print('Los libros tienen títulos diferentes.')

También es posible realizar esta comparación con valores numéricos.

### Para saber más: tabla de la verdad

Cuando deseamos crear una expresión lógica con operadores lógicos, es necesario comprender cómo funciona la tabla de verdad de cada uno de ellos para poder construir un código que produzca el resultado deseado. Estas tablas ayudan a comprender y analizar expresiones lógicas, como las que se encuentran en algoritmos de programación y a verificar la validez de una expresión lógica dada. La tabla de verdad ayuda a verificar los resultados para todas las posibles combinaciones de valores lógicos de una expresión lógica dada.

Vamos a conocer la tabla de verdad de los operadores lógicos and, or y not.

Operador and

La tabla de verdad del operador and muestra que la salida solo es Verdadero (True) si ambos operandos son Verdaderos. De lo contrario, devuelve Falso (False), como se muestra en la siguiente tabla:
operando_1	operando_2	operando_1 and operando_2
False	        False	False
False	        True	False
True	       False	False
True	        True	True

Operador or

La tabla de verdad del operador or muestra que la salida solo es Falso (False) si ambos operandos son Falsos; de lo contrario, devuelve Verdadero (True). Es decir, se devuelve True si al menos uno de los operandos es True, como se muestra a continuación:
operando_1	operando_2	operando_1 or operando_2
False	       False	False
False	        True	True
True	       False	True
True	        True	True

Operador not

El operador not tiene una tabla de verdad más simple, ya que simplemente invierte el valor del operando. Si el operando es Verdadero, devuelve Falso; si es Falso, devuelve Verdadero.
operando	not operando
True	      False
False	      True

### Lo que Aprendimos


Lo que aprendimos en esta aula:

    Construir estructuras condicionales con if, else y elif.
    Diferenciar las estructuras condicionales.
    Seleccionar la estructura condicional que mejor se adapte al problema.
    Utilizar diferentes operadores para crear expresiones condicionales.

