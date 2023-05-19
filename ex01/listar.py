import os

def listar_ficheros_carpeta(carpeta):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            tamano = os.path.getsize(ruta_archivo)
            tamano_legible = ""
            if tamano < 1024:
                tamano_legible = f"{tamano} bytes"
            elif tamano < 1024 * 1024:
                tamano_legible = f"{tamano / 1024:.2f} KB"
            elif tamano < 1024 * 1024 * 1024:
                tamano_legible = f"{tamano / (1024 * 1024):.2f} MB"
            else:
                tamano_legible = f"{tamano / (1024 * 1024 * 1024):.2f} GB"
            print(f"{ruta_archivo}: {tamano_legible}")
        elif os.path.isdir(ruta_archivo):
            listar_ficheros_carpeta(ruta_archivo)

# Obtenemos la ruta de la carpeta Descargas
carpeta_descargas = os.path.expanduser("~/Downloads")

# Recorremos todos los archivos y directorios de la carpeta Descargas
for archivo in os.listdir(carpeta_descargas):
    ruta_archivo = os.path.join(carpeta_descargas, archivo)
    if os.path.isfile(ruta_archivo):
        tamano = os.path.getsize(ruta_archivo)
        tamano_legible = ""
        if tamano < 1024:
            tamano_legible = f"{tamano} bytes"
        elif tamano < 1024 * 1024:
            tamano_legible = f"{tamano / 1024:.2f} KB"
        elif tamano < 1024 * 1024 * 1024:
            tamano_legible = f"{tamano / (1024 * 1024):.2f} MB"
        else:
            tamano_legible = f"{tamano / (1024 * 1024 * 1024):.2f} GB"
        print(f"{ruta_archivo}: {tamano_legible}")
    elif os.path.isdir(ruta_archivo):
        listar_ficheros_carpeta(ruta_archivo)