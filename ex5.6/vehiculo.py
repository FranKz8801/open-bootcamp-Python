# -*- coding: utf-8 -*-
"""vehiculo.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wb4PKMXGWjOrGe-5BBMN5E1Ld4D7Nhs3
"""

import pickle

# Definición de la clase Vehículo
class Vehículo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return f"Vehículo: Color={self.color}, Ruedas={self.ruedas}, Puertas={self.puertas}"


# Crear un objeto de la clase Vehículo
vehiculo = Vehículo("Rojo", 4, 2)

# Guardar el objeto en un archivo
archivo = "vehiculo.pkl"
with open(archivo, "wb") as f:
    pickle.dump(vehiculo, f)

# Cargar el objeto desde el archivo
with open(archivo, "rb") as f:
    vehiculo_cargado = pickle.load(f)

# Mostrar el objeto cargado por consola
print(vehiculo_cargado)