# Para saber más: String - Una secuencia de caracteres
Como se ha visto en clases anteriores, una cadena es un tipo de dato que corresponde a datos de texto. Cuando creamos una cadena, estamos agrupando varios caracteres (números, letras e incluso símbolos), y cada uno de ellos tiene sus índices. Como ejemplo, creemos una cadena con el nombre "Python":

lenguaje = 'Python'

Cada carácter de la cadena "lenguaje" se puede acceder mediante su índice, que comienza en 0 y va hasta la cantidad de caracteres de la cadena menos 1, incluyendo índices negativos. Podemos acceder a ellos de la misma manera que lo hacemos con las listas:

print(lenguaje[0], lenguaje[1], lenguaje[2], lenguaje[-3], lenguaje[-2], lenguaje[-1])

Salida: P y t h o n

Sin embargo, los índices solo se utilizan para acceder a los datos y no se puede cambiar el carácter presente en un índice específico mediante una simple asignación, como se hace con las listas. Por ejemplo, el código lenguaje[0] = 'p' generará un error en la compilación.

Con esto en mente, podríamos pensar que una cadena es una estructura de datos similar a una lista, ¿verdad? En realidad, no lo es. Una cadena es una secuencia de caracteres (letras, números, símbolos, etc.) representada por una sola variable. Por otro lado, una estructura de datos almacena una colección de elementos (que pueden ser de diferentes tipos) en una sola variable.

Sin embargo, es posible convertir una cadena en una lista mediante el método split(). Este método divide la cadena en una lista de cadenas, utilizando un delimitador especificado entre paréntesis. Este delimitador debe ser una cadena. Como ejemplo, convirtamos la cadena en una lista dividiéndola cada vez que aparezca el signo de interrogación "?":

pregunta = '¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?'
lista_palabras = pregunta.split('?')
print(lista_palabras)

Salida: ['¿Quién vino primero', ' ¿El huevo', ' ¿O fue la serpiente', '']

El delimitador no aparece en la separación. Si no se define un delimitador, la cadena se separará por todos los espacios en blanco en el texto.

pregunta = '¿Quién vino primero? ¿El huevo? ¿O fue la serpiente?'
lista_palabras = pregunta.split()
print(lista_palabras)

Salida: ['¿Quién', 'vino', 'primero?', '¿El', 'huevo?', '¿O', 'fue', 'la', 'serpiente?']

Lo contrario también es posible, ya que podemos convertir una lista en una cadena mediante el método join(). Para usar esta función, debemos definir el carácter que se utilizará para unir los elementos de la lista y formar la cadena. Luego, usamos el método { join() pasando la lista como argumento. Veamos un ejemplo con una lista que contiene el resultado de algunas mezclas de colores primarios en pintura:

mezclas = ['Pinturas: rojo, azul y amarillo',
            'Verde: mezcla de azul y amarillo',
            'Naranja: mezcla de rojo y amarillo',
            'Morado: mezcla de rojo y azul']
unificador = '. '
cadena_mezclas = unificador.join(mezclas)
print(cadena_mezclas)

Salida: 'Pinturas: rojo, azul y amarillo. Verde: mezcla de azul y amarillo. Naranja: mezcla de rojo y amarillo. Morado: mezcla de rojo y azul'


### Para saber más: otras manipulaciones para las listas

Hemos estudiado algunos métodos en clase, y además de esos, podemos utilizar otros para manipular listas en Python. Vamos a conocerlos y ver ejemplos de cómo se utilizan. En todos los casos, utilizaremos la siguiente lista llamada "razas_de_perros":

razas_de_perros = ['Labrador Retriever',
                   'Bulldog Francés',
                   'Pastor Alemán',
                   'Poodle']

El primer método es insert(), que permite insertar un elemento en una posición específica de la lista. La sintaxis es lista.insert(indice, elemento), donde "lista" es la lista que recibirá el nuevo elemento, "indice" es la posición donde se insertará el nuevo elemento y "elemento" es el nuevo elemento que se insertará.

razas_de_perros.insert(1, 'Golden Retriever')
razas_de_perros

Salida: ['Labrador Retriever', 'Golden Retriever', 'Bulldog Francés', 'Pastor Alemán', 'Poodle']

Siguiendo este enfoque, la estructura lista.insert(len(lista), elemento) es equivalente al uso del método append(), como vimos en el video anterior titulado "Manipulación de listas".

El método pop() elimina el elemento en una posición específica de la lista y lo devuelve como salida al ejecutar el método. Solo necesitamos especificar, entre paréntesis, el índice del elemento que deseamos eliminar, y se eliminará de la lista. Por lo tanto, eliminemos la raza "Golden Retriever" que agregamos en el método anterior.

razas_de_perros.pop(1)

Salida: 'Golden Retriever'

El método index() devuelve el índice de un elemento específico en la lista. Para hacerlo, especificamos el elemento entre paréntesis. Para encontrar el índice de la raza "Pastor Alemán" en la lista, hacemos lo siguiente:

razas_de_perros.index('Pastor Alemán')

Salida: 2

El método sort() ordena los elementos de la lista en orden ascendente o descendente. Si son palabras, el orden se basa en el orden alfabético o en el orden inverso. Para ordenar los valores, simplemente llamamos al método sort(), y la lista se organizará en orden. Para ordenar alfabéticamente la lista de razas de perros, podemos usar el siguiente código:

razas_de_perros.sort()
razas_de_perros

Salida: ['Bulldog Francés', 'Labrador Retriever', 'Pastor Alemán', 'Poodle']

Para obtener más opciones y descripciones de métodos, consulta la documentación de Python. https://docs.python.org/3/tutorial/datastructures.html#more-on-lists


### Para saber más: listas en diccionarios

Podemos asociar estructuras de datos a otras estructuras de datos, como ocurre cuando tenemos listas dentro de diccionarios. En este caso, las listas pueden ser almacenadas en los valores de un diccionario de tal manera que cada clave puede tener una lista asociada a ella. Esto es útil cuando necesitamos almacenar varios valores relacionados con una sola clave. Por ejemplo, podemos construir un conjunto de datos de una tienda que contenga una clave con los nombres de cada producto y otra clave con los precios correspondientes, como se muestra en el código a continuación:

tienda = {'nombres': ['televisión', 'celular', 'notebook', 'geladeira', 'estufa'],
          'precios': [2000, 1500, 3500, 4000, 1500]}

Para acceder a los valores, podemos utilizar una estructura de bucles for:

for clave, elementos in tienda.items():
  print(f'Clave: {clave}\nElementos:')
  for dato in elementos:
    print(dato)

El primer bucle, el más externo, recorre los elementos dentro del diccionario (claves y elementos). Sabiendo que los elementos son listas, podemos acceder a los datos de las listas con otro bucle anidado que se encuentra dentro del primer bucle. El bucle más interno recorre los elementos de cada lista uno a uno e imprime los valores dentro de ellas.

Además, podemos realizar operaciones comunes en las listas, como agregar, eliminar o contar elementos en la lista asociada a una clave del diccionario. Puedes copiar los códigos anteriores y ejecutarlos en Colab para verificar la salida.

### Para saber más: funciones incorporadas
Durante las clases, trabajamos directamente con varias funciones incorporadas que son predefinidas y están disponibles por defecto en Python. Estas funciones trabajan como herramientas útiles para llevar a cabo tareas comunes, como conversiones de tipos, operaciones matemáticas, manipulación de cadenas y más, sin necesidad de escribir código adicional.

Algunas de las funciones incorporadas que ya conocemos son: print(), input(), len(), int(), str(), float(), range(), chr(), etc. Pero hay otras además de estas que también son muy útiles, como: sum(), help() y dir(). ¿Las conocemos?

sum()

La función sum() permite sumar los elementos de una secuencia o estructura de datos. En el siguiente ejemplo, vamos a sumar los precios de productos:

precios = [100.0, 400.0, 200.0]
suma = sum(precios)
suma

Salida: 700.0

help()

La función help() se utiliza para acceder a la documentación de funciones, métodos y otros elementos de Python. Muestra información en inglés sobre la funcionalidad, sintaxis y uso de un objeto específico. Para usar esta función, simplemente pasa el elemento deseado entre paréntesis. Por ejemplo, vamos a verificar la documentación de la función print():

help(print)

Salida:

Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

dir()

Por último, la función dir() se utiliza para mostrar una lista de atributos y métodos asociados a un elemento. Por ejemplo, vamos a descubrir todos los atributos y métodos de una lista:

lista = [1,2,3]
dir(lista)

Salida:

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

Es útil conocer varias funciones incorporadas y cómo funcionan, ya que ayudan mucho en la creación de código. Para obtener más información sobre las funciones, puedes consultar la documentación de Python.

# Lo que aprendimos



Lo que aprendimos en esta aula:

    Construir estructuras de datos.
    Crear listas y diccionarios.
    Llenar y manipular listas y diccionarios.

