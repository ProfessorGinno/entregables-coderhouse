# --- Solución 2: Solución eficiente ---

matriz = [
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
    ]

# 1. Acceder a las listas y sumar columnas.
sum_row_1 = sum(matriz[0])
sum_row_2 = sum(matriz[1])
sum_row_3 = sum(matriz[2])
sum_row_4 = sum(matriz[3])

# 2. Agregar resultado del anterior paso a las columnas

matriz[0].append(sum_row_1)
matriz[1].append(sum_row_2)
matriz[2].append(sum_row_3)
matriz[3].append(sum_row_4)

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
  print("Todo mal")