# Daniel Nieves NC=1343
    
import sys
import os
import io
import pandas as pd

# Permitir importar dicc_1343.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-1343')))
import dicc_1343

print("Daniel Nieves Machine Learning pandas, NC 1343")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Daniel Nieves Machine Learning pandas, NC 1343"
contenido_md.append(f"# Reporte de Análisis de Datos - Supermercados (Pandas)\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario importado a DataFrame
df = pd.DataFrame(dicc_1343.datos_supermercados)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de Columnas Numéricas
registrar("3. Estadísticas Generales de 'Sucursales'", df['Sucursales'].describe())
registrar("3.1 Estadísticas Generales de 'Empleados'", df['Empleados'].describe())

# 4. Ordenar Ascendente por Sucursales
df_asc_sucursales = df.sort_values(by="Sucursales", ascending=True)
registrar("4. Ordenar Ascendente por Sucursales", df_asc_sucursales)

# 5. Ordenar Descendente por Empleados
df_desc_empleados = df.sort_values(by="Empleados", ascending=False)
registrar("5. Ordenar Descendente por Empleados", df_desc_empleados)

# 6. Guardar el archivo resultados-ml-1343.md dentro de resultados-1343
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-1343'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1343.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Daniel Nieves Machine Learning pandas, NC 1343")
