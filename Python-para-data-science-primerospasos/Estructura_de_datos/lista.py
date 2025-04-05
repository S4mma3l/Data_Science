# Listas

lista = ["Penelope Camacho", 9.5, 9.0, 9.7, True]
print(lista)
print(type(lista))
print(type(lista[0]))
print(type(lista[1]))

for elemento in lista:
    print( elemento )

lista[2] = 10.0
print(lista)

promedio = (lista[1] + lista[2] + lista[3]) / 3
print(promedio)