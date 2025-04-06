#  lista de listas


notas_grupo = ["juan", 8.0, 9.0, 7.0, "maria", 9.0, 8.0, 10.0, "pedro", 7.0, 6.0, 5.0, "luisa", 10.0, 9.0, 8.0]
nombre = []
notas = []

for i in range(len(notas_grupo)):
    if i % 4 == 0:
        nombre.append(notas_grupo[i])
    else:
        notas.append(notas_grupo[i])
print(nombre)
print(notas)
# Separa los nombres y las notas en listas diferentes


notas_separados = []

for i in range(0, len(notas), 3):
    notas_separados.append(notas[i:i+3])
print(notas_separados)

# lista de tuplas
from random import randint
from random import choice

def generador_de_numeros():
    return randint(0, 999)

codigo_estudiantes = []
for i in range(len(nombre)):
    codigo_estudiantes.append((nombre[i], nombre[i][0]+str(generador_de_numeros())))
print(codigo_estudiantes)