"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

Rta/
4
"""

import pandas as pd

def pregunta_02():
    """
    Calcula la cantidad de columnas en la tabla `tbl0.tsv`.

    Reads the `tbl0.tsv` file and returns the number of columns.

    Returns:
        int: The number of columns in the table.
    
    Example:
        >>> pregunta_02()
        4
    """
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    return len(tbl0.columns)

print(pregunta_02())

