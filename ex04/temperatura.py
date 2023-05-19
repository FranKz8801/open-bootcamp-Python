import requests
import urllib.parse

# Definimos la clave de API de OpenWeatherMap
API_KEY = "tu_clave_de_api_aqui"

# Pedimos al usuario que introduzca el nombre de la ciudad
ciudad = input("Introduce el nombre de la ciudad: ")

# Codificamos el nombre de la ciudad en formato URL
ciudad_codificada = urllib.parse.quote(ciudad)

# Definimos la URL de la API y sustituimos los parámetros necesarios
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad_codificada}&appid={API_KEY}"

# Realizamosla petición GET a la API y almacenamos la respuesta en la variable 'respuesta'
respuesta = requests.get(url)

# Comprobamos si la petición ha sido correcta (código de respuesta 200)
if respuesta.status_code == 200:
    # Convertimos la respuesta de la API (en formato JSON) a un diccionario de Python
    datos = respuesta.json()
    # Obtenemos la temperatura mínima y máxima en grados Celsius y las mostramos por pantalla
    temp_min = round(datos["main"]["temp_min"] - 273.15, 2)
    temp_max = round(datos["main"]["temp_max"] - 273.15, 2)
    print(f"La temperatura mínima en {ciudad} es de {temp_min} °C")
    print(f"La temperatura máxima en {ciudad} es de {temp_max} °C")
else:
    print("Ha ocurrido un error al realizar la petición a la API")