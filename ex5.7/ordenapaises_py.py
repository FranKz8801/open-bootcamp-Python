# -*- coding: utf-8 -*-
"""ordenapaises.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wb4PKMXGWjOrGe-5BBMN5E1Ld4D7Nhs3
"""

paises = input("Ingrese una lista de países separados por comas: ")
paises = paises.split(",")  # Dividir la entrada en una lista

# Eliminar posibles espacios en blanco alrededor de cada país
paises = [pais.strip() for pais in paises]

# Utilizar un conjunto (set) para eliminar países duplicados
paises = list(set(paises))

# Ordenar alfabéticamente la lista de países
paises.sort()

# Mostrar la lista de países separados por comas
paises_str = ", ".join(paises)
print("Lista de países ordenados alfabéticamente:")
print(paises_str)