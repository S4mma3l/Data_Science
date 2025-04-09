nombres = [['juan', 'j259'], ['maria', 'm829'], ['pedro', 'p874'], ['luisa', 'l61']]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
promedios = [9.0, 7.3, 5.8, 6.7, 8.5]

situacion = ["Aprobado(a)" if promedio >= 8.0 else "Reprobado(a)" for promedio in promedios]
print(situacion)

registros = [x for x in [nombres, notas, promedios, situacion]] # esta no es necesaria, pero es para mostrar que se puede hacer una lista de listas
# registros = [nombres, notas, promedios, situacion]
print(registros)

lista_completa = [nombres, notas, promedios, situacion]
print(lista_completa)

alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)
