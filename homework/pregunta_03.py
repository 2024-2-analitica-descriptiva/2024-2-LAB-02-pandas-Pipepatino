"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
archivo `tbl0.tsv`?

Rta/
c1
A     8
B     7
C     5
D     6
E    14
Name: count, dtype: int64
"""

import pandas as pd

def pregunta_03():
    """
    Calcula la cantidad de registros por cada letra de la columna `c1` en el archivo `tbl0.tsv`.

    Reads the `tbl0.tsv` file, groups the data by the column `c1`, and counts the occurrences
    of each unique value in the column.

    Returns:
        pandas.Series: A Series with the count of each unique value in column `c1`.
    
    Example:
        >>> pregunta_03()
        c1
        A     8
        B     7
        C     5
        D     6
        E    14
        Name: count, dtype: int64
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    # Contar las ocurrencias de cada letra en la columna c1
    conteo = tbl0['c1'].value_counts().sort_index()
    return conteo

# Ejecutar la función
print(pregunta_03())

