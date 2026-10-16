
import sys
import os
import pandas as pd

# Permitir importar dicc_1110.py desde la subcarpeta hermana
ruta_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-1110'))
sys.path.insert(0, ruta_datos)

import dicc_1110

print("Mario Yañez Machine Learning pandas, NC 1110")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Mario Yañez Machine Learning pandas, NC 1110"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_1110.datos_carnicerias)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Kg_dia)
registrar("3. Estadísticas Generales de la Columna 'Kg_dia'", df['Kg_dia'].describe())

# 4. Ordenar Ascendente por Kg_dia
df_asc_Kg_dia = df.sort_values(by="Kg_dia", ascending=True)
registrar("4. Ordenar Ascendente por Kg_dia", df_asc_Kg_dia)

# 5. Ordenar Descendente por Cortes
df_desc_Cortes = df.sort_values(by="Cortes", ascending=False)
registrar("5. Ordenar Descendente por Cortes", df_desc_Cortes)

# 7. Guardar el archivo resultados-ml-1110.md dentro de resultados-1110
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-1110'))
os.makedirs(carpeta_resultados, exist_ok=True)

ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-1110.md")

with open(ruta_archivo_md, "w", encoding="utf-8") as archivo:
    archivo.write("\n".join(contenido_md))

print("\nReporte guardado correctamente en:")
print(ruta_archivo_md)
