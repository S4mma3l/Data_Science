# 1 - Operaciones con la lista
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tamano = len(lista)
mayor = max(lista)
menor = min(lista)
suma = sum(lista)

print(f"La lista tiene {tamano} números, donde el mayor es {mayor} y el menor es {menor}. La suma de los valores es {suma}.")


# 2 - Tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

numero_tabla = int(input("Ingresa un número entero para la tabla de multiplicar: "))
tabla_multiplicar(numero_tabla)

# 3 - Múltiplos de 3
lista_numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos_de_3(lista):
  return [num for num in lista if num % 3 == 0]

nueva_lista = multiplos_de_3(lista_numeros)
print(f"Múltiplos de 3: {nueva_lista}")

# 4 - Cuadrados de números
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = list(map(lambda x: x**2, lista_original))
print(f"Cuadrados: {cuadrados}")

## aplicado a proyectos

# 5 - Puntuación de skaters
def calcular_puntuacion():
    notas = []
    for i in range(5):
        nota = float(input(f"Ingresa la nota del juez {i + 1}: "))
        notas.append(nota)
    
    notas.remove(max(notas))
    notas.remove(min(notas))

    puntuacion = sum(notas)
    print(f"Puntuación del atleta: {puntuacion:.2f}")

calcular_puntuacion()

# 6 - Análisis de rendimiento de estudiantes
def analisis_rendimiento(notas):
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacion = "Aprobado(a)" if media >= 6 else "Reprobado(a)"
    return media, mayor, menor, situacion

notas_estudiante = []
for i in range(4):
    nota = float(input(f"Ingresa la nota {i + 1}: "))
    notas_estudiante.append(nota)

media, mayor, menor, situacion = analisis_rendimiento(notas_estudiante)
print(f"El estudiante obtuvo una media de {media:.2f}, con la mayor nota de {mayor:.2f} puntos y la menor nota de {menor:.2f} puntos y fue {situacion}.")

# 7 - Nombres completos
nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

nombres_completos = list(map(lambda n, a: n.capitalize() + " " + a.capitalize(), nombres, apellidos))
print(f"Nombres completos: {nombres_completos}")

# 8 - Puntuación del equipo de fútbol
def calcula_puntos(goles_marcados, goles_recibidos):
    puntos = 0
    partidos = len(goles_marcados)
    
    for i in range(partidos):
        if goles_marcados[i] > goles_recibidos[i]:
            puntos += 3
        elif goles_marcados[i] == goles_recibidos[i]:
            puntos += 1
    
    desempeno = (puntos / (partidos * 3)) * 100
    return puntos, desempeno

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

puntos, desempeno = calcula_puntos(goles_marcados, goles_recibidos)
print(f"La puntuación del equipo fue {puntos} y su rendimiento fue {desempeno:.2f}%")

# 9 - Gastos de viaje
def gasto_hotel(dias):
    return dias * 150

def gasto_gasolina(distancia):
    litros = (distancia * 2) / 14  # Viaje de ida y vuelta
    return litros * 5

def gasto_paseo(dias, paseo_diario):
    return dias * paseo_diario

dias_viaje = 3
distancias = [850, 800, 300, 550]
paseos_diarios = [200, 400, 250, 300]
ciudades = ["Salvador", "Fortaleza", "Natal", "Aracaju"]

for i, ciudad in enumerate(ciudades):
  gastos = gasto_hotel(dias_viaje) + gasto_gasolina(distancias[i]) + gasto_paseo(dias_viaje, paseos_diarios[i])
  print(f"Con base en los gastos definidos, un viaje de {dias_viaje} días a {ciudad} desde Recife costaría {gastos:.2f} reales.")

# 10 - Filtrar palabras por longitud
frase = "Aprender Python aquí en Alura es muy bueno"
frase_limpia = frase.replace(",", "").replace(".", "").replace("!", "").replace("?", "")

palabras_largas = list(filter(lambda palabra: len(palabra) >= 5, frase_limpia.split()))
print(f"Palabras con 5 o más letras: {palabras_largas}")