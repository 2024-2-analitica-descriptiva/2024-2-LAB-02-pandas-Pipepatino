"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.

Retorne una lista con los valores unicos de la columna `c4` del archivo
`tbl1.csv` en mayusculas y ordenados alfabéticamente.

Rta/
['A', 'B', 'C', 'D', 'E', 'F', 'G']
"""

import pandas as pd

def pregunta_06():
    """
    Retorna una lista con los valores únicos de la columna `c4` del archivo `tbl1.csv`,
    convertidos a mayúsculas y ordenados alfabéticamente.

    Reads the `tbl1.csv` file, extracts the unique values from the column `c4`,
    converts them to uppercase, and sorts them alphabetically.

    Returns:
        list: A list of unique values in `c4` in uppercase and sorted alphabetically.
    
    Example:
        >>> pregunta_06()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    # Leer el archivo tbl1.csv
    tbl1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')
    # Extraer valores únicos de la columna `c4`, convertir a mayúsculas, y ordenar
    valores_unicos = sorted(tbl1['c4'].str.upper().unique())
    return valores_unicos

# Ejecutar la función
print(pregunta_06())
