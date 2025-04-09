empleados = {'José': 2000, 'Ana': 2200, 'Juan': 2500, 'Maria': 3800}

try:
  aumento = list(map(lambda x: x[1] * 1.1, empleados.items()))
except ValueError as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Proceso concluído!")


try:
  aumento = list(map(lambda x: x * 1.1, empleado.values()))
except Exception as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Proceso concluído!")

try:
  aumento = list(map(lambda x: x[1] * 1.1), empleados.values())
except Exception as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Proceso concluído!")

try:
  aumento = list(map(lambda x: x * 1.1, empleados.values()))
except ValueError as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Proceso concluído!")