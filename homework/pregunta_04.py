"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
Calcule el promedio de `c2` por cada letra de la `c1` del archivo
`tbl0.tsv`.

Rta/
c1
A    4.625000
B    5.142857
C    5.400000
D    3.833333
E    4.785714
Name: c2, dtype: float64
"""


import pandas as pd

def pregunta_04():
    """
    Calcula el promedio de `c2` para cada letra en la columna `c1` del archivo `tbl0.tsv`.

    Reads the `tbl0.tsv` file, groups the data by the column `c1`, and calculates the mean
    of the values in the column `c2` for each group.

    Returns:
        pandas.Series: A Series with the average of `c2` grouped by `c1`.
    
    Example:
        >>> pregunta_04()
        c1
        A    4.625000
        B    5.142857
        C    5.400000
        D    3.833333
        E    4.785714
        Name: c2, dtype: float64
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    # Agrupar por `c1` y calcular el promedio de `c2`
    promedio = tbl0.groupby('c1')['c2'].mean()
    return promedio

# Ejecutar la función
print(pregunta_04())

