# Para saber más: operadores de atribución

Los operadores de asignación permiten asignar un valor a una variable. Ya hemos trabajado bastante con el principal en Python, que es el operador "=" que realiza una asignación literal de un valor a una variable, como en "edad = 20" o "escolaridad = 'superior'", etc.

También conocemos el operador de suma "+=" que agrega un valor especificado a la variable, como se muestra en el siguiente ejemplo:

precio = 2.00
precio += 3
print(precio)

Salida: 5.0

Además de estos, existen otros operadores de asignación que permiten modificar los valores de las variables. Puede encontrar información sobre los operadores, su descripción y ejemplos en la siguiente tabla:
Operador	                      Descripción	                                                                                  Ejemplo
-=	                         Resta un valor de la variable precio	                                                               -= 5
*=	                         Multiplica un valor por la variable precio	                                                           *= 3
/=	                         Divide la variable por un valor precio	                                                               /= 2
//=	                         Realiza una división entera de la variable por un valor precio	                                       //= 6
%=	                         Calcula el resto de la división del valor en la variable y asigna el resultado a la variable precio   %= 5

### Para saber más: comandos de control

Cuando trabajamos con bucles, podemos controlar el flujo de ejecución dentro del bloque de código, lo que nos permite manipular la ejecución de los bucles. continue y break son los comandos de control que podemos usar con los bucles for y while.

continue interrumpe la iteración actual del bucle y salta a la siguiente, es decir, regresa al inicio del código. Como ejemplo, aquí hay un código que cuenta del 1 al 5 con un bucle for:

for i in range(1, 6):
    if i == 4:
        continue
    print(i)

Este código imprime todos los números del 1 al 5, excepto el 4. Cuando el valor de i es 4, continue salta a la siguiente iteración, omitiendo la instrucción print después de la condición en la iteración actual.

Por otro lado, break detiene por completo la ejecución del bucle, saliendo del bloque de código. Utilicemos el mismo ejemplo de conteo, pero esta vez con break:

for i in range(1, 6):
    if i == 4:
        break
    print(i)

En este caso, el código imprime todos los números del 1 al 3. Cuando el valor de i es 4, break interrumpe por completo la ejecución del bucle y sale de él, ignorando cualquier otra iteración que esté dentro de la estructura.

### Lo que aprendimos


Lo que aprendimos en esta aula:

    Estructurar bucles de repetición for y while.
    Decidir qué bucle de repetición utilizar.
    Utilizar comandos de control de bucles.