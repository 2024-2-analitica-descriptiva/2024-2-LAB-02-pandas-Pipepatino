"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
Calcule la suma de la `c2` por cada letra de la `c1` del archivo
`tbl0.tsv`.

Rta/
c1
A    37
B    36
C    27
D    23
E    67
Name: c2, dtype: int64
"""

import pandas as pd

def pregunta_07():
    """
    Calcula la suma de la columna `c2` para cada letra en la columna `c1` del archivo `tbl0.tsv`.

    Reads the `tbl0.tsv` file, groups the data by the column `c1`, and calculates the sum
    of the values in the column `c2` for each group.

    Returns:
        pandas.Series: A Series with the sum of `c2` grouped by `c1`.
    
    Example:
        >>> pregunta_07()
        c1
        A    37
        B    36
        C    27
        D    23
        E    67
        Name: c2, dtype: int64
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    # Agrupar por `c1` y calcular la suma de `c2`
    suma = tbl0.groupby('c1')['c2'].sum()
    return suma

# Ejecutar la función
print(pregunta_07())




