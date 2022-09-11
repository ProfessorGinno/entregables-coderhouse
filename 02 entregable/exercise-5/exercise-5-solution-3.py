# --- Análisis ---

# Pasos
"""
1. Acceder a la matriz en la posición de slicing
2. Sumar los objetos y agregar a la matriz
Todos los pasos combinados en un bloque
"""

# --- Solución 3: Solución más eficiente con slicing ---

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
    ]

matriz[0][len(matriz[0]):] = [sum(matriz[0])]
matriz[1][len(matriz[1]):] = [sum(matriz[1])]
matriz[2][len(matriz[2]):] = [sum(matriz[2])]
matriz[3][len(matriz[3]):] = [sum(matriz[3])]

# Test:

matriz_test = [
    [1, 5, 1, 7],
    [2, 1, 2, 5],
    [3, 0, 1, 4],
    [1, 4, 4, 9]
    ]

if matriz == matriz_test:
  print("Todo bien")
else:
  print("todo mal")