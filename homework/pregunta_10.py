"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
Rta/
                                c2
c1
A               1:1:2:3:6:7:8:9
B                 1:3:4:5:6:8:9
C                     0:5:6:7:9
D                   1:2:3:5:5:7
E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
"""


import pandas as pd

def pregunta_10():
    """
    Construye una tabla que contenga `c1` y una lista separada por ':' de los 
    valores de la columna `c2` agrupados por `c1` en el archivo `tbl0.tsv`.

    Lee el archivo `tbl0.tsv`, agrupa los datos por la columna `c1`, y combina 
    los valores de la columna `c2` en una lista separada por ':'.

    Returns:
        pandas.DataFrame: DataFrame con las columnas `c1` y `c2`, donde los valores de `c2` están separados por ':'.
    
    Example:
        >>> pregunta_10()
                                 c2
        c1
        A               1:1:2:3:6:7:8:9
        B                 1:3:4:5:6:8:9
        C                     0:5:6:7:9
        D                   1:2:3:5:5:7
        E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    # Leer el archivo tbl0.tsv
    tbl0 = pd.read_csv('files/input/tbl0.tsv', sep='\t')
    # Agrupar por `c1` y concatenar los valores de `c2` como lista separada por ':'
    result = tbl0.groupby('c1')['c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()
    # Establecer `c1` como índice
    result.set_index('c1', inplace=True)
    return result

# Ejecutar la función
print(pregunta_10())
