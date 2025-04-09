# 2048-python-para-data-science-trabajar-con-funciones
Este repositorio corresponde al entrenamiento de Python: Trabajar con funciones, estructuras de datos y funciones de Alura Latam.

### Para saber más: función zip()

La función zip() es una función incorporada de Python que toma uno o más iterables (lista, cadena, diccionario, etc.) y los devuelve como un iterador de tuplas donde cada elemento de los iterables está emparejado. Es útil para realizar iteraciones simultáneas en varias listas.

La función zip() se puede utilizar junto con otras funciones de Python, como map() y filter(), para crear soluciones elegantes y concisas para ciertos problemas. Realicemos una prueba simple para verificar este comportamiento:

objeto_zip = zip([1, 2, 3])
objeto_zip

Salida:

<zip at 0x7f28fc5c0040>

Notamos que zip() creó un objeto zip en la memoria, que sería nuestro iterable. Coloquemos el resultado en una lista para verificar la salida:

list(objeto_zip)

Salida:

[(1,), (2,), (3,)]

Observa que, con solo un iterable, se generó una lista de tuplas, donde cada tupla tiene, como uno de los pares, los elementos provenientes de la lista [1, 2, 3] y la otra parte de los pares está vacía. Como solo usamos un iterable, cada tupla está vacía en el segundo elemento, ya que zip() actúa para crear pares de iterables.

Pero lo más interesante es trabajar con dos o más iterables en los que podemos emparejarlos. Por ejemplo, si queremos crear una lista de tuplas con la asignación de las regiones de Brasil con sus respectivos identificadores:

id = [1, 2, 3, 4, 5]
region = ["Norte", "Oriente", "Sudeste", "Centro", "Sur"]

mapa = list(zip(id, region))
mapa

Salida:

[(1, 'Norte'), (2, Oriente), (3, 'Sudeste'), (4, 'Centro'), (5, 'Sur')]

Para un científico de datos, esta función puede ayudar a emparejar dos listas diferentes en un único objeto zip, que se puede transformar en una lista de tuplas (formato ideal para generar un índice de más de un nivel que se explorará en algunos de los cursos de la formación) o en un diccionario pasando el objeto zip a la función dict().

Ahora, si las listas de entrada tienen longitudes diferentes, la salida contendrá el mismo número de tuplas que la lista de menor longitud y los elementos restantes de los otros iterables se ignorarán. Por ejemplo:

codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["manzana", "uva", "banana", "naranja"]

mercancia = list(zip(codigos, frutas))
mercancia

Salida:

[('1000', 'manzana'), ('1001', 'uva'), ('1002', 'banana'), ('1003', 'naranja')]

Para realizar el proceso contrario, de transformar una tupla iterable en listas, basta con colocar el operador asterisco (*) al lado izquierdo del nombre de la tupla iterable que se desea extraer los datos, transmitiendo cada tupla a una variable.

tupla_iterable = [('J392', 'Juan'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claudia'), ('A49', 'Ana')]
ids, nombres = zip(*tupla_iterable)

ids = list(ids)
nombres = list(nombres)

print("IDs = ", ids)
print("Nombres = ", nombres)

Salida:

IDs = ['J392', 'M890', 'J681', 'C325', 'A49']
Nombres = ['Juan', 'Maria', 'José', 'Claudia', 'Ana']

La idea de realizar un "desempaquetado inverso" es útil cuando queremos extraer claves o valores por separado o generar una lista de tuplas separadas, con el conjunto de claves y valores, cada uno representado en una tupla.

### Lo que aprendimos



Lo que aprendimos en esta aula:

    Crear listas de diversas formas mediante la comprensión de listas (list comprehension).
    Crear diccionarios mediante la comprensión de diccionarios (dict comprehension).
    Trabajar con listas de listas en diccionarios.
    Generar un nuevo registro clave/valor en un diccionario.
