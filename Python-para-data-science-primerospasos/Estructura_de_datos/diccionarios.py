# Diccionarios
# Un diccionario es una colección desordenada, modificable e indexada de pares clave-valor.

diccionario = {"llave1": 1,
               "llave2": 2 }
print(diccionario)
print(type(diccionario)) # <class 'dict'>

estudiante = {
                "Matricula": 2000168933,
                "dia_registro": 25,
                "mes_registro": 10,
                "grupo": "2E"
            }
print(estudiante)
print(estudiante["Matricula"]) # 2000168933
print(estudiante["grupo"]) # 2E

estudiante["grupo"] = "2G" # Cambia el valor de la llave "grupo"
print(estudiante)

estudiante["modalidad"] = "EAD" # Agrega una nueva llave y su valor
print(estudiante)

print(len(estudiante)) # 5

# Que se puede hacer con un diccionario:
# - Crear un diccionario
# - Acceder a los valores de un diccionario
# - Modificar un diccionario
# - Eliminar un diccionario
# - Limpiar un diccionario
# - Copiar un diccionario
# - Iterar un diccionario
# - Comprobar si una llave existe en un diccionario
# - Obtener las llaves de un diccionario
# - Obtener los valores de un diccionario
# - Obtener los items de un diccionario
# - Obtener la longitud de un diccionario
# - Obtener el tipo de un diccionario


# Pop elimina un elemento del diccionario y lo devuelve
estudiante.pop("grupo") # Elimina la llave "grupo" y su valor
print(estudiante) # {'Matricula': 2000168933, 'dia_registro': 25, 'mes_registro': 10, 'modalidad': 'EAD'}

# item devuelve una tupla con la llave 
estudiante.items() # devuelve una lista de tuplas con las llaves y sus valores
print(estudiante.items()) # dict_items([('Matricula', 2000168933), ('dia_registro', 25), ('mes_registro', 10), ('modalidad', 'EAD')])

# keys devuelve una lista con las llaves del diccionario
print(estudiante.keys()) # dict_keys(['Matricula', 'dia_registro', 'mes_registro', 'modalidad'])

# values devuelve una lista con los valores del diccionario
print(estudiante.values()) # dict_values([2000168933, 25, 10, 'EAD'])

#for llave, in estudiante.keys():
#    print(llave) # Matricula, dia_registro, mes_registro, modalidad

for llave,valor in estudiante.items():
    print(llave, "-->", valor)