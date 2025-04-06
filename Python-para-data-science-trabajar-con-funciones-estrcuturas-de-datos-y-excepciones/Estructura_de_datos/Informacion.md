# 2048-python-para-data-science-trabajar-con-funciones
Este repositorio corresponde al entrenamiento de Python: Trabajar con funciones, estructuras de datos y funciones de Alura Latam.

### Para saber más: trabajando con tuplas

Las tuplas son estructuras de datos inmutables en el lenguaje Python que se utilizan para almacenar conjuntos de múltiples elementos y a menudo se aplican para agrupar datos que no deben modificarse. Es decir, no es posible agregar, cambiar o eliminar sus elementos después de creadas. Vamos a explorar un poco más este tipo de estructura enfocada en la aplicación en ciencia de datos.

Las tuplas son especialmente útiles en situaciones en las que necesitamos garantizar que los datos no se modifiquen accidental o intencionalmente. Por ejemplo, en un conjunto de datos que representa el registro de estudiantes, podemos utilizar una tupla para representar a ese estudiante en particular y mantenerlo en la base de datos de una institución educativa. De esta manera, aseguramos que la información de cada estudiante no se modifique inadvertidamente.

Para crear una tupla, simplemente separamos sus elementos por comas y los envolvemos entre paréntesis. Por ejemplo, podemos crear una tupla con un registro de una estudiante de la siguiente manera:

registro = ("Julia", 23, "CDMX", "EM", "Python para DS 1")

Para acceder a los elementos de una tupla, podemos usar el índice entre corchetes. Por ejemplo:

print(registro[0])  # imprime Julia
print(registro[-1])  # imprime Python para DS 1

Además, al ser un iterable, podemos desempaquetar los datos de una tupla pasando cada valor a una variable. Por ejemplo:

nombre, edad, ciudad, estado, curso = registro

Y mostrar los datos del registro de la estudiante:

print(f'La estudiante {nombre} tiene {edad} años y vive en {ciudad}-{estado}. Ella está matriculada en el curso de {curso}.')

Salida:

La estudiante Julia tiene 23 años y vive en CDMX-EM. Ella está matriculada en el curso de Python para DS 1.

### Lo que aprendimos



Lo que aprendimos en esta aula:

    Crear listas de listas y listas de tuplas.
    Acceder y extraer listas y elementos de una lista de listas.

