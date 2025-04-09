'''
# notas = [6, 7, 8, 9, 10] # tiene un numero mas de notas de las permitidas para provocar un error del tipo ValueError
# notas = [6, 7, 8, 9, "10"] # Cambiamos el 10 por un string para provocar un error del tipo TypeError

def promedio(lista: list=[0]) -> float:
  Función para calcular el promedio de notas en una lista

  lista: list, default [0]
    Lista con las notas para calcular el promedio
  return = calculo: float
    Promedio calculado
  

  calculo = sum(lista) / len(lista)

  if len(lista) > 4:
    raise ValueError("La lista no puede poseer mas de 4 notas")
  

  return calculo



try:
  notas = [6, 7, 8, 9, "10"]
  resultado = promedio(notas)
except TypeError:
  print("No fue posible calcular el promedio del(la) estudiante. Solo se admiten valores numéricos!")
except ValueError as e:
  print(e)
else:
    print(f"Las notas del estudiante son: ", resultado)
finally:
    print("La consulta ha finalizado")

resultado = promedio(notas)
print(resultado)
'''


# notas = [6, 7, 8, 9, 10] # tiene un numero mas de notas de las permitidas para provocar un error del tipo ValueError
# notas = [6, 7, 8, 9, "10"] # Cambiamos el 10 por un string para provocar un error del tipo TypeError

def promedio(lista: list=[0]) -> float:
    ''' Función para calcular el promedio de notas en una lista

    lista: list, default [0]
        Lista con las notas para calcular el promedio
    return = calculo: float
        Promedio calculado
    '''
    if not lista:  # Manejamos el caso de una lista vacía para evitar ZeroDivisionError
        raise ValueError("La lista de notas no puede estar vacía.")

    # Verificamos el tipo de los elementos antes de intentar sumarlos
    for nota in lista:
        if not isinstance(nota, (int, float)):
            raise TypeError("La lista solo puede contener valores numéricos (int o float).")

    if len(lista) > 4:
        raise ValueError("La lista no puede poseer más de 4 notas.")

    calculo = sum(lista) / len(lista)
    return calculo

try:
    notas = [6, 7, 8, 9, 10]
    resultado = promedio(notas)
except TypeError:
    print("No fue posible calcular el promedio del(la) estudiante. Solo se admiten valores numéricos!")
except ValueError as e:
    print(e)
else:
    print(f"Las notas del estudiante son: {resultado}")
finally:
    print("La consulta ha finalizado")

# La siguiente llamada a promedio fuera del bloque try-except podría generar un error no manejado.
# Comentamos esta línea para evitar una posible interrupción si ocurre un error.
# resultado_fuera_try = promedio(notas)
# print(resultado_fuera_try)