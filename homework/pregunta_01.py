"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.

¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

Rta/
40
"""

import pandas as pd

def pregunta_01():
    """
    Calcula la cantidad de filas en la tabla `tbl0.tsv`.

    Reads the `tbl0.tsv` file and returns the number of rows.

    Returns:
        int: The number of rows in the table.
    
    Example:
        >>> pregunta_01()
        40
    """
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    return len(tbl0)


# Ejecutar la función
print(pregunta_01())
