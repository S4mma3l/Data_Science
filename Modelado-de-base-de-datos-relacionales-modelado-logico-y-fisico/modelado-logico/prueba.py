def analizar_ropa(registros):
    """
    Analiza una lista de registros de clientes para contar cuántas personas
    usaron ropa roja y cuántas usaron ropa negra.

    Args:
        registros (list): Una lista de diccionarios, donde cada diccionario
                          representa un cliente y contiene información sobre
                          la ropa que usó (ej. {'cliente_id': 1, 'color_ropa': 'rojo'}).

    Returns:
        dict: Un diccionario con el conteo de personas que usaron ropa roja
              y ropa negra (ej. {'rojo': 5, 'negro': 10}).
    """
    conteo_rojo = 0
    conteo_negro = 0

    for registro in registros:
        color = registro.get('color_ropa', '').lower()  # Obtener el color y convertir a minúsculas

        if color == 'rojo':
            conteo_rojo += 1
        elif color == 'negro':
            conteo_negro += 1

    return {'rojo': conteo_rojo, 'negro': conteo_negro}

# Ejemplo de registros de clientes
registros_tienda = [
    {'cliente_id': 1, 'color_ropa': 'rojo'},
    {'cliente_id': 2, 'color_ropa': 'negro'},
    {'cliente_id': 3, 'color_ropa': 'azul'},
    {'cliente_id': 4, 'color_ropa': 'ROJO'},
    {'cliente_id': 5, 'color_ropa': 'blanco'},
    {'cliente_id': 6, 'color_ropa': 'negro'},
    {'cliente_id': 7, 'color_ropa': 'rojo'},
    {'cliente_id': 8, 'color_ropa': 'gris'},
    {'cliente_id': 9, 'color_ropa': 'NEGRO'},
    {'cliente_id': 10, 'color_ropa': 'rojo'},
    {'cliente_id': 11, 'color_ropa': 'rojo'},
    {'cliente_id': 12, 'color_ropa': 'negro'},
]

# Analizar los registros
resultado_analisis = analizar_ropa(registros_tienda)

# Imprimir el resultado
print("Conteo de personas por color de ropa:")
print(f"Rojo: {resultado_analisis['rojo']}")
print(f"Negro: {resultado_analisis['negro']}")