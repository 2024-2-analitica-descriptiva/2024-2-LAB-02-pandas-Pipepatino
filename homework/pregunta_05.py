"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_05():
    """
    Calcula el valor máximo de `c2` para cada letra en la columna `c1` del archivo `tbl0.tsv`.

    Reads the `tbl0.tsv` file, groups the data by the column `c1`, and calculates the maximum
    value in the column `c2` for each group.

    Returns:
        pandas.Series: A Series with the maximum value of `c2` grouped by `c1`.
    
    Example:
        >>> pregunta_05()
        c1
        A    9
        B    9
        C    9
        D    7
        E    9
        Name: c2, dtype: int64
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Agrupar por `c1` y calcular el máximo de `c2`
    maximos = tbl0.groupby('c1')['c2'].max()
    return maximos

# Ejecutar la función
print(pregunta_05())



