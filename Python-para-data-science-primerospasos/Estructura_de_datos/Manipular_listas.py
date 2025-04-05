# Manipular listas
lista = ["Penelope Camacho", 9.5, 9.0, 9.7, True]

print(len(lista)) # 5
print(lista[0:2]) # ["Penelope Camacho", 9.5]
print(lista[:3]) # ["Penelope Camacho", 9.5, 9.0]
print(lista[3:]) # [9.7, True]
print(lista[:]) # ["Penelope Camacho", 9.5, 9.0, 9.7, True]
print(lista[-1]) # True

lista[2] = 10.0
print(lista)

promedio = (lista[1] + lista[2] + lista[3]) / 3
print(promedio)

lista.append(promedio) # agrega el promedio al final de la lista en una nueva posición
print(lista) # ["Penelope Camacho", 9.5, 10.0, 9.7, True, 9.733333333333334]

lista.extend([10.0, 8.0, 9.0]) # agrega los elementos de la lista al final de la lista asignado una posición a cada uno
print(lista) # ["Penelope Camacho", 9.5, 10.0, 9.7, True, 9.733333333333334, 10.0, 8.0, 9.0]

lista.remove(10.0) # elimina el primer elemento que coincide con el valor 10.0
print(lista) # ["Penelope Camacho", 9.5, 9.7, True, 9.733333333333334, 8.0, 9.0]