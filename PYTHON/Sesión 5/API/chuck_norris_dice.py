import requests


def obtenerChiste():
  URL = 'https://api.chucknorris.io/jokes/random'
  respuesta = requests.get(url = URL)
  if (respuesta.status_code >= 200 and respuesta.status_code < 300):
    # Extraemos los datos en formato JSON
    datos = respuesta.json()
    # Obtenemos valor en la clave 'value' del JSON que nos interesa
    frase_chuck: str = datos['value']
    return frase_chuck
  else: return 'Ha ocurrido un error'