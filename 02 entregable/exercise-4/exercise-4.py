"""Ejercicio 4

🧠 A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. Cada nota tiene un valor porcentual:

La primera nota vale un 15% del total.
La segunda nota vale un 35% del total.
La tercera nota vale un 50% del total.
📌 Tener en cuenta: puede usar los siguientes datos para válidar el código. Recuerda hacer uso del input.

nota_1 = 10
nota_2 = 7
nota_3 = 4"""

# --- Análisis ---

# Pasos

"""
1. Ingreso de notas.
2. Procesamiento de notas.
3. Impresión de notas.
"""

# --- Solución ---

# Ingreso de notas
print(""""Bienvenido a SIGA, por favor ingrese las notas
recuerde usar números entre 0.0 y 5.0.
""")

nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))

# Procesamiento de notas
nota_final = (nota_1 * .15) + (nota_2 * .35) + (nota_3 * .5)

# Impresión de notas:
print(f"""
Usted ingresó
Nota 1: {nota_1}.
Nota 2: {nota_2}.
nota 3: {nota_3}.

Su nota final es: {nota_final}""")