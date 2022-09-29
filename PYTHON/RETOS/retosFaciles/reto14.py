'''
Escribe una función que use la función del área del círculo para devolver el volumen de un cilindro, obteniendo por parámetro la longitud del mismo.
'''
from retosFaciles.reto13 import areaCirculo

def volumenCilindro(longitud:float, radio:float) -> float:
  return round(areaCirculo(radio)*longitud,3)