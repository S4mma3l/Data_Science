import random

# 1 - Promedio de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
promedio_gastos = sum(gastos) / len(gastos)
print(f"1. Promedio de gastos: {promedio_gastos:.2f}")

# 2 - Compras por encima de 3000 y porcentaje
compras_altas = sum(1 for gasto in gastos if gasto > 3000)
porcentaje_altas = (compras_altas / len(gastos)) * 100
print(f"2. Compras > 3000: {compras_altas}, Porcentaje: {porcentaje_altas:.2f}%")

# 3 - 5 números enteros aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(5)]  # Números entre 1 y 100
print(f"3. Números aleatorios: {numeros_aleatorios}")

# 4 - 5 números enteros en orden inverso
numeros_ingresados = []
for _ in range(5):
    numero = int(input("Ingresa un número entero: "))
    numeros_ingresados.append(numero)
print(f"4. Números en orden inverso: {numeros_ingresados[::-1]}")

# 5 - Números primos hasta un número ingresado
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numero_limite = int(input("Ingresa un número: "))
primos = [num for num in range(2, numero_limite + 1) if es_primo(num)]
print(f"5. Números primos hasta {numero_limite}: {primos}")

# 6 - Validar fecha
def es_fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12 or dia < 1:
        return False
    dias_en_mes = [0, 31, 29 if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dia <= dias_en_mes[mes]

dia = int(input("Ingresa el día: "))
mes = int(input("Ingresa el mes: "))
anio = int(input("Ingresa el año: "))

if es_fecha_valida(dia, mes, anio):
    print("6. La fecha es válida.")
else:
    print("6. La fecha no es válida.")

# 7 - Porcentaje de crecimiento de bacterias
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crecimiento = [100 * (bacterias[i] - bacterias[i - 1]) / bacterias[i - 1] for i in range(1, len(bacterias))]
print(f"7. Porcentaje de crecimiento: {crecimiento}")

# 8 - Productos dulces y amargos
ids = []
for _ in range(10):
    id_producto = int(input("Ingresa el ID del producto: "))
    ids.append(id_producto)

dulces = sum(1 for id_prod in ids if id_prod % 2 == 0)
amargos = len(ids) - dulces
print(f"8. Productos dulces: {dulces}, Productos amargos: {amargos}")

# 9 - Puntuación del estudiante
respuestas_correctas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respuestas_estudiante = []
for i in range(10):
    respuesta = input(f"Ingresa la respuesta a la pregunta {i + 1} (A, B, C o D): ").upper()
    respuestas_estudiante.append(respuesta)

puntuacion = sum(1 for i in range(10) if respuestas_estudiante[i] == respuestas_correctas[i])
print(f"9. Puntuación del estudiante: {puntuacion}")

# 10 - Temperaturas mensuales y promedio anual
temperaturas = []
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for mes in meses:
    temperatura = float(input(f"Ingresa la temperatura media de {mes}: "))
    temperaturas.append(temperatura)

promedio_anual = sum(temperaturas) / len(temperaturas)
print(f"10. Promedio anual de temperatura: {promedio_anual:.2f}")

temperaturas_altas = [(meses[i], temp) for i, temp in enumerate(temperaturas) if temp > promedio_anual]
print("Temperaturas por encima del promedio:")
for mes, temp in temperaturas_altas:
    print(f"  {mes}: {temp:.2f}")

# 11 - Ventas totales y producto más vendido
ventas = {'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}
total_ventas = sum(ventas.values())
producto_mas_vendido = max(ventas, key=ventas.get)
print(f"11. Total de ventas: {total_ventas}, Producto más vendido: {producto_mas_vendido}")

# 12 - Diseño de marca ganador
votos = {'Diseño 1': 1334, 'Diseño 2': 982, 'Diseño 3': 1751, 'Diseño 4': 210, 'Diseño 5': 1811}
total_votos = sum(votos.values())
diseno_ganador = max(votos, key=votos.get)
porcentaje_ganador = (votos[diseno_ganador] / total_votos) * 100
print(f"12. Diseño ganador: {diseno_ganador}, Porcentaje: {porcentaje_ganador:.2f}%")

# 13 - Bonificaciones de empleados
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonificaciones = {}
gasto_total_bonificaciones = 0
empleados_bonificacion_minima = 0
bonificacion_maxima = 0

for salario in salarios:
    bonificacion = 0.10 * salario
    if bonificacion < 200:
        bonificacion = 200
        empleados_bonificacion_minima += 1
    bonificaciones[salario] = bonificacion
    gasto_total_bonificaciones += bonificacion
    bonificacion_maxima = max(bonificacion_maxima, bonificacion)

print(f"13. Bonificaciones: {bonificaciones}")
print(f"Gasto total en bonificaciones: {gasto_total_bonificaciones:.2f}")
print(f"Empleados con bonificación mínima: {empleados_bonificacion_minima}")
print(f"Bonificación máxima: {bonificacion_maxima:.2f}")

# 14 - Diversidad biológica en el bosque
especies = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
promedios_especies = {}
for area, conteos in especies.items():
    promedio = sum(conteos) / len(conteos)
    promedios_especies[area] = promedio

area_mas_diversa = max(promedios_especies, key=promedios_especies.get)
print(f"14. Promedios de especies por área: {promedios_especies}")
print(f"Área con mayor diversidad: {area_mas_diversa}")

# 15 - Análisis de edades de colaboradores
edades_sectores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

promedios_sectores = {}
total_personas = 0
suma_total_edades = 0

for sector, edades in edades_sectores.items():
    promedio_sector = sum(edades) / len(edades)
    promedios_sectores[sector] = promedio_sector
    total_personas += len(edades)
    suma_total_edades += sum(edades)

promedio_general = suma_total_edades / total_personas
personas_encima_promedio = sum(sum(1 for edad in edades if edad > promedio_general) for edades in edades_sectores.values())

print(f"15. Promedios de edad por sector: {promedios_sectores}")
print(f"Promedio de edad general: {promedio_general:.2f}")
print(f"Personas por encima del promedio general: {personas_encima_promedio}")