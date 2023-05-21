# -*- coding: utf-8 -*-
"""obtenerhora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wb4PKMXGWjOrGe-5BBMN5E1Ld4D7Nhs3
"""

import time

# Obtener la hora actual del sistema
hora_actual = time.localtime().tm_hour

if hora_actual >= 19:  # 19 representa las 7 PM
    print("¡Es hora de ir a casa!")
else:
    # Calcular el tiempo restante de trabajo en horas y minutos
    horas_restantes = 19 - hora_actual
    minutos_restantes = 60 - time.localtime().tm_min

    # Mostrar el tiempo restante de trabajo
    print(f"Quedan {horas_restantes} horas y {minutos_restantes} minutos de trabajo.")