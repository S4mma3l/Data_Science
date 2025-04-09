def promedio(lista: list=[0]) -> float:
    """
    Calcula el promedio de una lista de números.

    :param lista: Lista de números.
    :return: Promedio de la lista.
    """
    calculo = sum(lista) / len(lista)

    return calculo

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

promedios = [round(promedio(nota), 1) for nota in notas]
print(promedios)
# [(9.0, 1), (7.333333333333333, 1), (5.466666666666667, 1), (7.366666666666666, 1), (8.166666666666666, 1)]


nombres = [['juan', 'j259'], ['maria', 'm829'], ['pedro', 'p874'], ['luisa', 'l61']]
promedios = [9.0, 7.3, 5.8, 6.7, 8.5]

nombres = [nombre[0] for nombre in nombres]
print(nombres)

estudiantes = list(zip(nombres, promedios))
print(estudiantes)
# [('juan', 9.0), ('maria', 7.3), ('pedro', 5.8), ('luisa', 6.7)]

candidatos = [estudiante[0] for estudiante in estudiantes if estudiante[1] >= 8.0]
print(candidatos)