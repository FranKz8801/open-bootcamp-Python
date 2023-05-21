# -*- coding: utf-8 -*-
"""obtener_seleccion.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wb4PKMXGWjOrGe-5BBMN5E1Ld4D7Nhs3
"""

import tkinter as tk

def obtener_seleccion():
    seleccion = lista.get(lista.curselection())
    label_text.set(f"Elemento seleccionado: {seleccion}")

# Crear ventana
ventana = tk.Tk()

# Crear lista de elementos seleccionables
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
lista = tk.Listbox(ventana, selectmode=tk.SINGLE)
for elemento in elementos:
    lista.insert(tk.END, elemento)

# Crear label
label_text = tk.StringVar()
label_text.set("")

label = tk.Label(ventana, textvariable=label_text)

# Crear botón
boton_obtener = tk.Button(ventana, text="Obtener selección", command=obtener_seleccion)

# Posicionar elementos en la ventana
lista.pack()
label.pack()
boton_obtener.pack()

# Ejecutar ventana
ventana.mainloop()