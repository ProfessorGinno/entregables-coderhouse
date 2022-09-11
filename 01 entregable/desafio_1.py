# DESAFÍO ENTREGABLE NÚMERO 1
# Hecho por Ginno Andrés Vera Valencia

# Descripción del problema

"""Crear un programa para calcular la nota final del estudiante del curso de Python.
La nota final se calcula basándonos en tres notas previas de las cuales, 
cada una corresponde a un porcentaje distinto de la nota final.
Entonces, la nota final deberá estar estar compuesta por:
El 20% de la nota_1
El 30% de la nota_2
El 50% de la nota_3
Aspectos a incluir: Tener en cuenta los temas vistos en la clase 1: números, print, input, variables, operaciones matemáticas, cadena de texto. Los datos deben guardarse en variables y deben ser dinámicos por medio de input."""

# Análisis del problema
""" Pasos
- Recibir un input del usuario y almacenarlo en una variable.
- Recalcular la nota según el peso
- Mostrar la nota final"""

# Solución del problema
# Mensaje de Bienvenida e informativo para el usuario
print(""" --- Plataforma de ingreso de notas ---
Bienvenido a la plataforma de ingreso de notas.
Recuerde usar números entre 0.0 y 5.0, finalmente, no olvide los percentiles:
    La primera nota valdrá el 20% de la final.
    La segunda nota valdrá el 30% de la final.
    La tercera nota valdrá el 50% de la final.
""")

# Recepción de notas
score_1 = float(input("Ingrese la primera nota: ")) # Recibe la nota 1
score_2 = float(input("Ingrese la segunda nota: ")) # Recibe la nota 2
score_3 = float(input("Ingrese la tercera nota: ")) # Recibe la nota 3

# Ponderación de datos
ponderado_s1 = score_1 * .20 # Ponderado de la nota 1
ponderado_s2 = score_2 * .30 # Ponderado de la nota 2
ponderado_s3 = score_3 * .50 # Ponderado de la nota 3

# Suma de las notas ponderadas
final_score = ponderado_s1 + ponderado_s2 + ponderado_s3

# Muestra de la nota final
print(f"""
Usted introdujo:
Primera nota: {score_1}.
Segunda nota: {score_2}.
Tercera nota: {score_3}.

-> El promedio ponderado es: {final_score}.

Gracias por usar nuestros servicios.
""")