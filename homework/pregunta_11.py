"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.

Construya una tabla que contenga `c0` y una lista separada por ',' de
los valores de la columna `c4` del archivo `tbl1.tsv`.

Rta/
     c0       c4
0     0    b,f,g
1     1    a,c,f
2     2  a,c,e,f
3     3      a,b
...
37   37  a,c,e,f
38   38      d,e
39   39    a,d,f
"""

import pandas as pd

import pandas as pd

def pregunta_11():
    """
    Construye una tabla que contenga la columna `c0` y una lista separada por ',' 
    de los valores de la columna `c4` del archivo `tbl1.tsv`.

    Lee el archivo `tbl1.tsv`, agrupa los datos por la columna `c0`, y combina los valores 
    únicos de la columna `c4` en una lista separada por comas.

    Returns:
        pandas.DataFrame: DataFrame con las columnas `c0` y `c4`, donde `c4` es una lista separada por ','.
    
    Example:
        >>> pregunta_11()
             c0       c4
        0     0    b,f,g
        1     1    a,c,f
        2     2  a,c,e,f
        3     3      a,b
        ...
        37   37  a,c,e,f
        38   38      d,e
        39   39    a,d,f
    """
    # Leer el archivo tbl1.tsv
    tbl1 = pd.read_csv('files/input/tbl1.tsv', sep='\t')
    # Agrupar por `c0` y concatenar los valores únicos de `c4` como lista separada por ','
    result = tbl1.groupby('c0')['c4'].apply(lambda x: ','.join(sorted(x.unique()))).reset_index()
    return result

# Ejecutar la función
print(pregunta_11())


