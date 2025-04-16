### Para saber más: diferencia entre modelos

El modelado de datos es uno de los procesos más importantes al trabajar en un proyecto de base de datos. Durante este proceso, los datos se recopilan, se tratan y se estructuran para crear una base sólida que permita construir una base de datos eficiente.

Además del modelo conceptual, que se utiliza para comprender los requisitos del sistema y explorar las estructuras y conceptos del negocio, también podemos trabajar con otros dos modelos: el lógico y el físico.

El modelo lógico se crea para describir cómo se almacenarán los datos en el sistema, explorando los conceptos del dominio. En este modelo se definen las entidades, los atributos, las claves principales y foráneas, así como sus relaciones.

Por otro lado, el modelo físico se utiliza para describir las tablas, sus columnas y relaciones. A diferencia del modelo lógico, este modelo emplea un lenguaje específico para su representación: SQL, el lenguaje utilizado para trabajar con bases de datos relacionales.

En esta clase, se discute la importancia de entender los Sistemas de Gestión de Bases de Datos (SGBD) antes de modelar una base de datos. Martha, una de las integrantes del equipo, enfatiza que es crucial diseñar una estructura inteligente que refleje los requisitos del negocio y del cliente para que la base de datos sea funcional y realista.

Se aclara que el SGBD es la interfaz que permite interactuar con la base de datos, realizando acciones como incluir, alterar, eliminar y consultar datos. A menudo, se confunden los términos "base de datos" y "SGBD", pero es importante diferenciarlos, ya que el SGBD es el software que se utiliza para gestionar la base de datos.

Además, se menciona la relevancia de tener un inventario o registro de datos en diferentes contextos, como bibliotecas, supermercados o empresas de ecommerce. Por último, se introduce la diferencia entre el lenguaje de alto nivel, que se relaciona con el modelaje conceptual, y el lenguaje de bajo nivel, que es el que utilizan las máquinas. La clase concluye con la expectativa de que el equipo aprenda a modelar su base de datos en las próximas sesiones.

# diagrams.net = https://www.drawio.com/

### Para saber más: herramientas para el modelaje



Es posible aplicar las técnicas de modelaje sin el uso de una herramienta CASE (Computer-Aided Software Engineering, o Ingeniería de Software Asistida por Computador), pero este trabajo manual sería bastante extenso. Además, la conversión del esquema conceptual al esquema lógico (rediseñando las formas, por ejemplo), puede tornar el trabajo exhaustivo y estresante. Al emplear una herramienta CASE logramos observar las alteraciones del modelo, conforme vamos tomando las decisiones (proceso “causa-efecto”).

Pero, ¿Será que existe una herramienta CASE ideal?

Una herramienta CASE necesita tener la capacidad de utilizar diversas formas geométricas para: desarrollar una buena representación visual, el diccionario de datos, la integración entre el diagrama entidad-relación y el diccionario de datos, además de posibilitar una mínima interacción con el usuario.

Existen varias herramientas avanzadas disponibles en el mercado que pueden auxiliar el modelaje del banco de datos. Algunas de las más conocidas son:

    OracleDesigner ™ (Oracle ®): Posee una arquitectura flexible y puede ser instalada en múltiples plataformas; https://www.oracle.com/database/technologies/developer-tools/designer.html
    PowerDesigner ™ (Sybase ®): Es uno de los más utilizados en el mercado; https://www.sapstore.com/solutions/61111/SAP-PowerDesigner
    ERWin (CA ®): Muy utilizado en el mercado, también; https://www.erwin.com/
    Freeware DBDesigner: Posee una gran cantidad de recursos también; https://dbdesigner.softonic.com.br/
    PyDesigner: Disponible para la plataforma Linux; https://pydesigner.readthedocs.io/en/latest/installation/pydesigner.html#pydesigner
    VISIO ™ (Microsoft ®): Herramienta con enfoque exclusivo para el diseño.  https://www.microsoft.com/es-es/microsoft-365/visio/flowchart-software

Durante nuestro entrenamiento utilizaremos diagrams.net, ¿pero qué motivó esta elección? Esta herramienta posee las siguientes ventajas:

    Permite realizar alteraciones estructurales al modelo, a medida que el analista toma nuevas decisiones;
    Dar especial atención a los atributos y a todas sus especificaciones;
    Posibilitar una visualización más “limpia” del esquema al ocultar los atributos que no tengan relevancia en el modelo conceptual, pero que sí importan en el modelo lógico, por ejemplo;
    Posee un diccionario de datos muy completo.


https://app.diagrams.net/?src=about


### Lo que aprendimos en esta aula:

    Identificar un modelo lógico de datos y un modelo físico de datos.
    Diferenciar un modelo de alto nivel de un modelo de bajo nivel.
    Entender qué son los SGBDs.
    Aplicar las técnicas de modelaje utilizando una herramienta CASE.


