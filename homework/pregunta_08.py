"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.

Agregue una columna llamada `suma` con la suma de `c0` y `c2` al
data frame que contiene el archivo `tbl0.tsv`.

Rta/
     c0  c1   c2          c3  suma
0     0   E    1  1999-02-28     1
1     1   A    2  1999-10-28     3
2     2   B    5  1998-05-02     7
...
37   37   C    9  1997-07-22    46
38   38   E    1  1999-09-28    39
39   39   E    5  1998-01-26    44
"""

import pandas as pd

def pregunta_08():
    """
    Agrega una columna llamada `suma` al DataFrame que contiene el archivo `tbl0.tsv`.
    La nueva columna `suma` es la suma de las columnas `c0` y `c2`.

    Reads the `tbl0.tsv` file and adds a new column `suma`, which contains the sum of
    the values in columns `c0` and `c2`.

    Returns:
        pandas.DataFrame: The modified DataFrame with the additional column `suma`.
    
    Example:
        >>> pregunta_08()
              c0  c1  c2          c3  suma
        0      0   E   1  1999-02-28     1
        1      1   A   2  1999-10-28     3
        2      2   B   5  1998-05-02     7
        ...
        37    37   C   9  1997-07-22    46
        38    38   E   1  1999-09-28    39
        39    39   E   5  1998-01-26    44
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    # Agregar la nueva columna `suma` como la suma de `c0` y `c2`
    tbl0['suma'] = tbl0['c0'] + tbl0['c2']
    return tbl0

# Ejecutar la función
print(pregunta_08())
