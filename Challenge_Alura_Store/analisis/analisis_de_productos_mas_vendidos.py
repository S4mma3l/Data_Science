import pandas as pd

# Cargamos los datos de cada tienda desde las URLs proporcionadas
url_tienda1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url_tienda2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_tienda3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_tienda4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda1_df = pd.read_csv(url_tienda1)
tienda2_df = pd.read_csv(url_tienda2)
tienda3_df = pd.read_csv(url_tienda3)
tienda4_df = pd.read_csv(url_tienda4)

# --- 1. Calcular los ingresos por producto para cada tienda ---
# Agrupamos los datos por 'Producto' y sumamos los 'Precio' para cada tienda
ingresos_por_producto_tienda1 = tienda1_df.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda2 = tienda2_df.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda3 = tienda3_df.groupby('Producto')['Precio'].sum()
ingresos_por_producto_tienda4 = tienda4_df.groupby('Producto')['Precio'].sum()

# --- 2. Encontrar los 5 productos principales por ingresos para cada tienda ---
num_top_productos = 5  # Definimos cuántos productos principales queremos
top_productos_tienda1 = ingresos_por_producto_tienda1.nlargest(num_top_productos)
top_productos_tienda2 = ingresos_por_producto_tienda2.nlargest(num_top_productos)
top_productos_tienda3 = ingresos_por_producto_tienda3.nlargest(num_top_productos)
top_productos_tienda4 = ingresos_por_producto_tienda4.nlargest(num_top_productos)

# --- 3. Crear DataFrames para los 5 productos principales ---
top_productos_tienda1_df = pd.DataFrame({'Producto': top_productos_tienda1.index, 'Ingresos': top_productos_tienda1.values})
top_productos_tienda2_df = pd.DataFrame({'Producto': top_productos_tienda2.index, 'Ingresos': top_productos_tienda2.values})
top_productos_tienda3_df = pd.DataFrame({'Producto': top_productos_tienda3.index, 'Ingresos': top_productos_tienda3.values})
top_productos_tienda4_df = pd.DataFrame({'Producto': top_productos_tienda4.index, 'Ingresos': top_productos_tienda4.values})

# --- 4. Imprimir los resultados ---
print("\nAnálisis de Productos Más Vendidos (por Ingresos):")
print("\nTop", num_top_productos, "Productos - Tienda 1:\n", top_productos_tienda1_df)
print("\nTop", num_top_productos, "Productos - Tienda 2:\n", top_productos_tienda2_df)
print("\nTop", num_top_productos, "Productos - Tienda 3:\n", top_productos_tienda3_df)
print("\nTop", num_top_productos, "Productos - Tienda 4:\n", top_productos_tienda4_df)