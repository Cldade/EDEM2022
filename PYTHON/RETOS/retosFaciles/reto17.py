'''
Partiendo de la siguiente tupla:
tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
Realiza las siguientes operaciones
Encontrar los elementos de 3 a 5
Encontrar los 6 primeros elementos
Muestra la tupla desde el 5 elemento hasta el final
Muestra toda la tupla haciendo uso de [:]
Muestra todos los elementos desde la posición 2 a la 9 de dos en dos
Devuelve la tupla con un salto cada 4 elementos
Usa un step negativo para mostrar la tupla desde la posición 9 a la 2
'''

tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

def enc3y5(tupla:tupla) ->tupla:
  return tupla[3:6:1]

def primerosSeis(tupla:tupla) ->tupla:
  return tupla[0:6:1]

def desde5aFinal(tupla:tupla) ->tupla:
  return tupla[5::1]

def muestraToda(tupla:tupla) ->tupla:
  return tupla[0::1]

def desde2a9de2en2(tupla:tupla) ->tupla:
  return tupla[2:9:2]

def salto4(tupla:tupla) ->tupla:
  return tupla[::4]

def de9a2(tupla:tupla) ->tupla:
  return tupla[-1:-9:-1]