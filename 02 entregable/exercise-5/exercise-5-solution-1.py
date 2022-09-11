# --- Análisis ---

# Pasos
"""
1. Sacar los números de las listas.
2. Sumar las listas individualmente.
3. Agregar el resultado a las listas del paso 2.
4. Concatenar todas las listas.
"""

# --- Solución 1: Solución larga ---

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
    ]

# 1. Sacar los números de las listas
row_1 = matriz[0]
row_2 = matriz[1]
row_3 = matriz[2]
row_4 = matriz[3]

# 2. Sumar las listas individualmente.
sum_row_1 = [sum(row_1)]
sum_row_2 = [sum(row_2)]
sum_row_3 = [sum(row_3)]
sum_row_4 = [sum(row_4)]

# 3. Agregar las sumas a las listas del paso 2.

row_1 = row_1 + sum_row_1
row_2 = row_2 + sum_row_2
row_3 = row_3 + sum_row_3
row_4 = row_4 + sum_row_4

# 4. Concatenar todas las litas
matriz = [row_1] + [row_2] + [row_3] + [row_4]

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