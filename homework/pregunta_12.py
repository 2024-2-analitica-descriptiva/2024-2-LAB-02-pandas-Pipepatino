"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.

Construya una tabla que contenga `c0` y una lista separada por ','
de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
tabla `tbl2.tsv`.

Rta/
     c0                                   c5
0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
1     1              aaa:3,ccc:2,ddd:0,hhh:9
2     2              ccc:6,ddd:2,ggg:5,jjj:1
...
37   37                    eee:0,fff:2,hhh:6
38   38                    eee:0,fff:9,iii:2
39   39                    ggg:3,hhh:8,jjj:5

"""

import pandas as pd

def pregunta_12():
    """
    Construye una tabla que contenga `c0` y una lista separada por ','
    de los valores de las columnas `c5a` y `c5b` (unidos por ':') de la tabla `tbl2.tsv`.

    Lee el archivo `tbl2.tsv`, agrupa los datos por la columna `c0`, y combina
    los valores de `c5a` y `c5b` en el formato `c5a:c5b`, separados por comas.

    Returns:
        pandas.DataFrame: DataFrame con las columnas `c0` y `c5`, donde `c5`
        contiene las combinaciones de `c5a` y `c5b` separadas por comas.
    
    Example:
        >>> pregunta_12()
             c0                                   c5
        0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
        1     1              aaa:3,ccc:2,ddd:0,hhh:9
        2     2              ccc:6,ddd:2,ggg:5,jjj:1
        ...
        37   37                    eee:0,fff:2,hhh:6
        38   38                    eee:0,fff:9,iii:2
        39   39                    ggg:3,hhh:8,jjj:5
    """
    # Leer el archivo tbl2.tsv
    tbl2 = pd.read_csv('files/input/tbl2.tsv', sep='\t')

    # Crear una columna combinando `c5a` y `c5b` con el formato `c5a:c5b`
    tbl2['c5'] = tbl2['c5a'] + ':' + tbl2['c5b'].astype(str)

    # Agrupar por `c0` y concatenar los valores de `c5` separados por ','
    result = tbl2.groupby('c0')['c5'].apply(lambda x: ','.join(sorted(x))).reset_index()

    return result

# Ejecutar la función
print(pregunta_12())

