import pandas as pd

# --- 1. Cargar los datos ---
url_tienda1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_tienda2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_tienda3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_tienda4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1_df = pd.read_csv(url_tienda1)
tienda2_df = pd.read_csv(url_tienda2)
tienda3_df = pd.read_csv(url_tienda3)
tienda4_df = pd.read_csv(url_tienda4)

# --- 2. Estructura de Datos (Análisis Inicial) ---
print("\n--- Estructura de Datos Inicial ---")

print("\nInformación de Tienda 1:")
tienda1_df.info()
print("\nPrimeras 5 filas de Tienda 1:")
print(tienda1_df.head())

print("\nInformación de Tienda 2:")
tienda2_df.info()
print("\nPrimeras 5 filas de Tienda 2:")
print(tienda2_df.head())

print("\nInformación de Tienda 3:")
tienda3_df.info()
print("\nPrimeras 5 filas de Tienda 3:")
print(tienda3_df.head())

print("\nInformación de Tienda 4:")
tienda4_df.info()
print("\nPrimeras 5 filas de Tienda 4:")
print(tienda4_df.head())

# --- 3. Descripción de las Columnas ---
print("\n--- Descripción de las Columnas ---")

print("\nDescripción de las columnas (ejemplo - Tienda 1):")
for col in tienda1_df.columns:
    print(f"- **{col}**: {tienda1_df[col].dtype}")
    if tienda1_df[col].dtype == 'object':
        print(f"  - Valores únicos (ejemplos): {tienda1_df[col].unique()[:5]}...")
    elif tienda1_df[col].dtype in ['int64', 'float64']:
        print(f"  - Estadísticas descriptivas:\n{tienda1_df[col].describe()}")

print("\n\n**Resumen de la Estructura de Datos:**")
print("- Los conjuntos de datos para las cuatro tiendas contienen la misma estructura de columnas.")
print("- Cada conjunto de datos tiene las siguientes columnas principales:")
print("  - **Producto**: Nombre del producto vendido (tipo: object).")
print("  - **Categoría del Producto**: Categoría a la que pertenece el producto (tipo: object).")
print("  - **Precio**: Precio de venta del producto (tipo: float64).")
print("  - **Costo de envío**: Costo de envío asociado a la compra (tipo: float64).")
print("  - **Fecha de Compra**: Fecha en la que se realizó la compra (tipo: object - requiere conversión a datetime).")
print("  - **Vendedor**: Identificador del vendedor (tipo: object).")
print("  - **Lugar de Compra**: Ubicación geográfica de la compra (tipo: object).")
print("  - **Calificación**: Calificación dada por el cliente a la compra (tipo: int64).")
print("  - **Método de pago**: Método de pago utilizado (tipo: object).")
print("  - **Cantidad de cuotas**: Número de cuotas en las que se dividió el pago (tipo: int64).")
print("  - **lat**: Latitud de la ubicación de la transacción (tipo: float64).")
print("  - **lon**: Longitud de la ubicación de la transacción (tipo: float64).")
print("- La columna 'Fecha de Compra' necesita ser convertida al tipo datetime para realizar análisis temporales.")
print("- Las columnas numéricas ('Precio', 'Costo de envío', 'Calificación', 'Cantidad de cuotas', 'lat', 'lon') pueden ser analizadas utilizando estadísticas descriptivas.")
print("- Las columnas de tipo 'object' contienen información categórica que puede ser útil para análisis de tendencias, categorías más populares, etc.")