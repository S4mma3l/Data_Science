# Operadores lógicos
# AND, OR, NOT  
# AND: y
# OR: o
# NOT: no
#AND es usado para verificar si ambas condiciones son verdaderas
#OR es usado para verificar si al menos una de las condiciones es verdadera
#NOT es usado para invertir el resultado de una condicion

#Ejemplo de AND
v = True
f = False

if v and v:
    print("Ambas condiciones son verdaderas")
else:
    print("Una o ambas condiciones son falsas")

#Ejemplo de OR
if v or v:
    print("Ambas condiciones son verdaderas")
else:
    print("Una o ambas condiciones son falsas")

#ejemplo de NOT
if not f:
    print("Ambas condiciones son verdaderas")
else:
    print("Una o ambas condiciones son falsas")

# verificar si un elemento pertenece a una lista
lista = 'Juan Pérez, María González, Pedro Rodríguez, Ana López, Carlos Martínez,Laura Sánchez, José García, Elena Fernández, Luis Morales, Carmen Torres,David Ruiz, Isabel Ramírez, Javier Díaz, Sara Herrera, Miguel Castro,Patricia Ortega, Francisco Vargas, Marta Jiménez, Manuel Medina, Rosa Molina,Alejandro Silva, Silvia Ruiz, Andrés Torres, Natalia Soto, Diego Guerrero,Paula Ríos, Ricardo Navarro, Alicia Cordero, Carlos Vidal, Lorena Gómez'

nombre_1 = 'Miguel Castro'
nombre_2 = 'Marcelo Noguera'

if nombre_1 in lista:
    print(f"{nombre_1} pertenece a la lista")
else:
    print(f"{nombre_1} no pertenece a la lista")

if nombre_2 in lista:
    print(f"{nombre_2} pertenece a la lista")
else:
    print(f"{nombre_2} no pertenece a la lista")