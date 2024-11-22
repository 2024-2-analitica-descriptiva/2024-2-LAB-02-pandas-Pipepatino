"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

Rta/
c1
A    146
B    134
C     81
D    112
E    275
Name: c5b, dtype: int64
"""

import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    computa la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Se realiza un merge de los dos DataFrames utilizando `c0` como clave,
    y luego se agrupa por `tbl0.c1` para calcular la suma de `tbl2.c5b`.

    Returns:
        pandas.Series: Serie con la suma de `c5b` agrupada por `c1`.
    
    Example:
        >>> pregunta_13()
        c1
        A    146
        B    134
        C     81
        D    112
        E    275
        Name: c5b, dtype: int64
    """
    # Leer los archivos tbl0.tsv y tbl2.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='\t')
    
    # Realizar un merge de tbl0 y tbl2 utilizando `c0` como clave
    merged = pd.merge(tbl0, tbl2, on='c0')
    
    # Agrupar por `c1` y calcular la suma de `c5b`
    result = merged.groupby('c1')['c5b'].sum()
    
    return result

# Ejecutar la función
print(pregunta_13())
