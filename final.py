import numpy as np
filas=5
columnas=7
valores=list(map(int, input("introduce valores por un espacio: ").split()))
matriz=np.array(valores).reshape(filas, columnas)
print(matriz)