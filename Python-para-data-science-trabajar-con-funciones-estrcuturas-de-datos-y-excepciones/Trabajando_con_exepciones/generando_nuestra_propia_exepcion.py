
def exhibir_notas_anuales(lista):
    
    if lista > 3:
        raise ValueError("La lista de notas debe tener 3 elementos")
    
    for i, nota in enumerate(lista):
        print(f"{i+1}ª Trimestre = {nota}")

def exhibir_notas_anuales(lista):
    
    for i, nota in enumerate(lista):
        print(f"{i+1}ª Trimestre = {nota}")

    if len(lista) > 3:
        raise ValueError("La lista de notas debe tener 3 elementos")
    

def exhibir_notas_anuales(lista):
    
    if len(lista) > 3:
        raise ValueError("La lista de notas debe tener 3 elementos")
    
    for i, nota in enumerate(lista):
        print(f"{i+1}ª Trimestre = {nota}")

try:
  notas = [5.0, 2.0, 6.0, 8.0]
  exhibir_notas_anuales(notas)
except Exception as e:
  print(type(e), f'Erro: {e}')