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