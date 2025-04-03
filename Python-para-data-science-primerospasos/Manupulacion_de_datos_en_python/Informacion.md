A veces, cuando estamos programando, necesitamos describir alguna etapa, función o estructura dentro del propio código. Esta descripción debe darse como una anotación y, por lo tanto, no se considera código que se interprete en el entorno. Para estas situaciones, existen los comentarios.

Los comentarios son líneas de texto que se pueden colocar dentro del código y que son ignoradas por el intérprete. Por eso, sirven para explicar el funcionamiento del código a otras personas o incluso a la persona que programa. Son importantes para documentar el código, describiendo lo que hace y para qué sirve cada función, estructura o método. Esto puede hacer que el código sea más legible y fácil de entender.

Podemos construir dos tipos de comentarios en Python, de una y varias líneas.

Comentarios de una línea:

Estos comentarios se hacen agregando un símbolo de almohadilla/numeral (#) al principio de una línea de código. Todo lo que venga después del símbolo # en una línea se considerará un comentario, como se puede ver en el código a continuación:

# Este es un comentario de una línea
print(10) # Podemos colocar otro comentario en una línea después de un código

Puedes ejecutar el código anterior en tu cuaderno y verás que todo el texto después del símbolo # se ignora durante la ejecución.

Comentarios de varias líneas:

Los comentarios de varias líneas se hacen usando un conjunto de comillas triples: ''' o """. Todo lo que esté entre estas comillas triples se considerará un comentario, incluso si abarca varias líneas. Por ejemplo:

'''
Este es un comentario
de varias líneas.
'''

Mientras el texto esté dentro de las comillas, se ignorará durante la ejecución, ya sea en una línea de código o en cualquier otro texto. A pesar de estas formas de comentar el código, cuando trabajamos con un cuaderno de Python, tenemos la opción de crear celdas de texto en formato markdown.

Markdown:

Markdown es una forma de formato de texto que permite escribir de manera simple y fácil de leer. Permite agregar formato al texto sin necesidad de escribir código HTML u otro lenguaje de formato más complejo.

Con markdown, podemos formatear el texto para agregar negritas, cursivas, listas, encabezados, etc. Además, es una excelente opción para documentar el código describiendo lo que hemos hecho, analizando los resultados y proporcionando pasos futuros. En Ciencia de Datos, se hace un amplio uso de textos en markdown, ya que facilita en gran medida la documentación en cuadernos.

Para crear una celda de texto en Google Colab, puedes hacer clic en el botón + Texto debajo de la barra superior de botones de Colab, como se muestra en la imagen a continuación:

4.jpg

Al crear la celda de texto, puedes agregar el contenido que desees. El cuaderno de este curso está lleno de celdas de texto que explican varios aspectos de la programación en Python, todas formateadas con markdown. A continuación, te damos algunos consejos para construir texto con markdown:

Encabezados:

Para construir encabezados, puedes usar el símbolo # antes del texto. Cuantos más símbolos # uses, menor será el nivel del encabezado. Por ejemplo:

# Encabezado de nivel 1
## Encabezado de nivel 2
### Encabezado de nivel 3

Negritas e itálicas:

Para formatear el texto en negritas, puedes usar ** antes y después del texto, como en el ejemplo:

**Texto en negritas**

Para formatear el texto en cursiva, utiliza * antes y después del texto. Por ejemplo:

*Texto en cursiva*

También puedes combinar ambas formas de escritura agrupando las dos estructuras con ** y *. Por ejemplo:

***Texto en negritas y cursiva***

Listas:

Para crear listas no numeradas (con viñetas), coloca * y luego un espacio * antes del elemento, como en el ejemplo:

* Elemento 1
* Elemento 2
* Elemento 3

Para crear listas numeradas, puedes usar un número seguido de un punto y un espacio 1. antes del elemento, como en el ejemplo:

1. Elemento 1
2. Elemento 2
3. Elemento 3

Enlaces:

Para crear enlaces, a continuación, tienes un ejemplo con el enlace al sitio web de Alura:

[Página de Alura](https://www.aluracursos.com/)

Estos son ejemplos más comunes de uso de markdown, pero existen muchas otras formas y recursos disponibles para que domines el lenguaje de marcación.

### Para saber más: ¿Qué es la documentación?

La documentación de cualquier lenguaje funciona como un conjunto de guías escritas para ayudar a los desarrolladores a comprender y utilizar un lenguaje de programación. Pueden encontrarse en sitios web creados por el equipo que desarrolló ese lenguaje. Como se mencionó en clase, podemos encontrar la documentación de Python en python.org.

Estas documentaciones suelen incluir información sobre sintaxis y estructuras, bibliotecas y herramientas disponibles, funciones, ejemplos de código y otros puntos útiles para ayudar a escribir código eficiente y correcto. Se trata de un recurso valioso tanto para quienes están aprendiendo un nuevo lenguaje de programación como para personas experimentadas que buscan información específica para su código.

Un detalle a tener en cuenta es que la mayoría de las documentaciones están escritas en inglés, lo que puede dificultar para alguien que no tiene un gran conocimiento de ese idioma. Sin embargo, normalmente hay soporte para la traducción al español a través del traductor del navegador.

### Para saber más: otros operadores

Durante las clases, aprendimos a sumar, restar, multiplicar y dividir variables numéricas en Python. Pero también existen otros cálculos matemáticos que se pueden realizar mediante operadores aritméticos, como la exponenciación, el módulo y la división entera.

Exponenciación (**)

Podemos elevar un número a una potencia específica utilizando el operador **. Para obtener este resultado, definimos un valor a la izquierda del operador y la potencia deseada del número a la derecha. Por ejemplo, sabemos que 2 elevado a la 3 es igual a 8 (2 * 2 * 2 = 8). Para realizar este cálculo, escribimos:

2**3

Salida: 8

El mismo ejemplo se puede hacer con variables:

operador = 2
potencia = 3
operador ** potencia

Salida: 8

Módulo (%)

El operador de módulo % puede devolver el residuo de una división entera entre dos números. Recuerda que el residuo de una división es el número que queda cuando la división no es exacta.

Para calcular el módulo de una división, colocamos el dividendo a la izquierda del operador % y el divisor a la derecha. Por ejemplo, para encontrar el residuo de la división de 7 entre 3, podemos ejecutar los siguientes códigos:

7%3

Salida: 1

O con variables:

dividendo = 7
divisor = 3
dividendo % divisor

Salida: 1

División entera (//)

Esta operación devuelve el resultado de la división entera entre dos números, es decir, solo devuelve la parte entera de una división. Por ejemplo, sabemos que la división exacta de 7 por 3 (7/3) resulta en el valor 2.333333.... Si esta fuera una división entera, el resultado sería simplemente 2. La sintaxis consiste en colocar el valor del numerador, el operador // y luego el denominador, como se muestra a continuación:

7 // 3

Salida: 2

El mismo ejemplo se puede hacer con variables:

numerador = 7
denominador = 3
numerador // denominador

Salida: 2

Puedes probar todos los ejemplos en tu cuaderno, verificar sus resultados y realizar pruebas modificando los valores.

### Para saber más: tabla unicode

 Python es un lenguaje de programación caracterizado por el uso del estándar Unicode de caracteres. Este estándar permite que desarrolladores de todo el mundo trabajen con textos y caracteres en diferentes idiomas de manera muy sencilla, sin preocuparse por problemas de compatibilidad.

Esto fue posible gracias al desarrollo de la tabla Unicode, una tabla de codificación de caracteres que asocia códigos numéricos con caracteres específicos. Su objetivo era incluir caracteres de todos los idiomas y sistemas de escritura existentes en el mundo. Hasta la versión 15.0, el estándar ya agrupa más de 140,000 caracteres, que incluyen letras, números, símbolos y emojis. Puedes ver las estadísticas de cada versión y la cantidad de caracteres por versión en este enlace.

Además, Unicode surgió como una alternativa a otras tablas de caracteres, como ASCII, que solo admite caracteres del alfabeto inglés y algunos símbolos. Por lo tanto, es muy importante ya que permite la representación de caracteres de diferentes idiomas (como la "ç" en portugués, la "ñ" en español o la "П" en ruso) y scripts de manera consistente e independiente del dispositivo o plataforma, lo que es fundamental para la globalización y la representación precisa de textos en diferentes idiomas.

Es importante recordar que la tabla Unicode se actualiza y se expande constantemente, incluyendo nuevos caracteres y scripts. Esto asegura que siga siendo relevante y útil para admitir la representación de todos los idiomas y sistemas de escritura del mundo. Puedes seguir las actualizaciones en el sitio unicode.org y acceder a las codificaciones de cada carácter de este estándar en la Wikipedia o en documentos oficiales en PDF.

Podemos imprimir un elemento de la tabla Unicode en nuestro cuaderno utilizando la función chr, que devuelve una cadena con el carácter especificado. Su sintaxis es la siguiente: chr(número_del_carácter). Por ejemplo, vamos a imprimir el carácter "@" con chr(). Según la tabla, sabemos que "@" corresponde al número 64, así que lo reprodujimos:

'''
chr(64)
'''
Salida: '@'

Se pueden probar y observar varias combinaciones de números en las salidas. Siéntete libre de probar varias combinaciones e incluso crear frases.

También es posible concatenar cadenas con el operador "+". Sabiendo esto, si unimos varios caracteres, podemos formar una palabra. Por ejemplo, vamos a construir la palabra "Hola" ('H' + 'o' + 'l' + 'a'):

chr(72) + chr(111) +  chr(108) + chr(97)

Salida: 'Hola'

### Para saber más: diversos formatos de print()


 Podemos visualizar el resultado de variables dentro de cadenas de texto, así como imprimir el texto final con un print. Durante la lección, aprendimos a utilizar la f-string (formateo de cadena), en la que colocamos una f antes de crear la cadena y las variables se colocan entre llaves {}. Ejemplo:

nombre = "Ana María"
edad = 17
print(f"El nombre de la alumna es {nombre} y su edad es {edad} años.")

Salida: 'El nombre de la alumna es Ana María y su edad es 17 años.'

Pero existen otros métodos de formateo, como el uso del operador de formateo de cadena o la función .format().

Operador de Formateo:

Este operador de formateo permite la inserción de variables en puntos específicos en la cadena de texto utilizando el operador %. Este operador funciona como un marcador, indicando dónde se expondrá el valor de la variable en la cadena.

El % debe ir acompañado de una palabra clave para cada tipo de variable que se desee agregar. De acuerdo con la tabla siguiente:
Tipo de Variable	Palabra Clave
Cadena de texto	      %s
Entero	              %d
Punto flotante	      %f
Caractér	          %c

De esta manera, para insertar una variable, puedes agregar el operador en la cadena en el punto deseado. Luego del final de la cadena, agrega nuevamente el %, especificando la variable entre paréntesis. Podemos ver esta estructura en el ejemplo siguiente:

nombre_alumno = 'Penélope Camacho'
print('Nombre del alumno: %s' %(nombre_alumno))

Salida: 'Nombre del alumno: Penélope Camacho'

Si tienes más de una variable, debes ordenarlas según su aparición en el texto y separarlas por comas. Por ejemplo:

nombre_alumno = 'Penélope Camacho'
edad_alumno = 11
media_alumno = 9.95
print('Nombre del alumno es %s, tiene %d años y su media es %f.' %(nombre_alumno, edad_alumno, media_alumno))

Salida: 'Nombre del alumno es Penélope Camacho, tiene 11 años y su media es 9.950000.'

Cuando trabajamos con números de coma flotante (float), podemos determinar la cantidad de decimales después del punto utilizando la sintaxis %.xf, donde x es el número de decimales deseados. Utilizando las mismas variables del ejemplo anterior, el código con %.xf se vería así:

print('Nombre del alumno es %s, tiene %d años y su media es %.2f.' %(nombre_alumno, edad_alumno, media_alumno))

Salida: 'Nombre del alumno es Penélope Camacho, tiene 11 años y su media es 9.95.'

Un detalle importante es que los operadores de formateo de cadena con % no funcionan directamente con valores booleanos. Una forma de manejarlo es convirtiendo el valor booleano en una cadena antes de utilizarlo en el formateo con la función str(). Por ejemplo:

x = True
print("Valor de x: %s" % str(x))

Esto no es un problema con las f-strings o .format.

Método .format():

También es posible utilizar el método .format() para formatear cadenas. Es más flexible y permite pasar las variables directamente dentro de la cadena, sin necesidad de operadores %. Los marcadores son simplemente {}. Por ejemplo:

nombre_alumno = 'Penélope Camacho'
print('Nombre del alumno: {}'.format(nombre_alumno))

Del mismo modo que se hace con el operador, puedes usarlo con varias variables:

nombre_alumno = 'Fabricio Daniel'
edad_alumno = 15
media_alumno = 9.95
print('Nombre del alumno es {}, tiene {} años y su media es {}.' .format(nombre_alumno, edad_alumno, media_alumno))

Nota que con .format(), no tienes el problema de los decimales de coma flotante. Tampoco tienes este problema con las f-strings.

En resumen, cada uno de estos métodos tiene sus ventajas y desventajas. Se recomienda utilizar f-strings, ya que son más legibles y fáciles de usar. Sin embargo, cada desarrollador puede elegir el método que le parezca más apropiado.

Caracteres Especiales:

Además de la formateo de inserción de variables en una cadena, también existen caracteres especiales. Se utilizan para representar acciones especiales o caracteres que no se pueden escribir directamente, como el “Enter” y la tabulación. A continuación, presentamos algunos de ellos. Intenta replicar todos los ejemplos y observa el resultado final.

\n es el carácter de nueva línea y se usa para saltar una línea en el texto (similar a la función "Enter"). Ejemplo:

print("Estudiar es un esfuerzo constante,\nEs como cultivar una planta,\nNecesitamos dedicación y paciencia,\nPara ver madurar el fruto.")

\t es el carácter de tabulación y se utiliza para agregar un espacio de tabulación en el texto. Ejemplo:

print('Cantidad\tCalidad\n5 muestras\tAlta\n3 muestras\tBaja')

\\ se usa para imprimir una sola barra invertida. Si no se utiliza una doble barra invertida, el código podría generar un error o un resultado inesperado, ya que Python considera \ como un carácter especial. Usamos esta sintaxis para garantizar que no ocurran errores. Ejemplo:

print("Ruta del archivo: C:\\archivos\\documento.csv")

\" se utiliza para imprimir comillas dobles cuando estamos trabajando con una cadena creada con comillas dobles " en el interior. Sin embargo, esto no es necesario si la cadena se crea con comillas simples '. Ejemplo:

print("Una vez oí: \"Los frutos del conocimiento son los más dulces y duraderos de todos.\"")

\' se utiliza para imprimir comillas simples cuando estamos trabajando con una cadena creada con comillas simples '. Si la cadena se crea con comillas dobles ", esto no es necesario. Ejemplo:

print('Mi profesora una vez dijo: \'Estudiar es la clave del éxito.\'')


### Lo que aprendimos en esta aula:
    Crear variables en Python.
    Distinguir entre los diferentes tipos de datos.
    Realizar operaciones con variables numéricas.
    Manipular variables de texto (cadenas de caracteres).
    Recolectar datos de un usuario utilizando la función input().