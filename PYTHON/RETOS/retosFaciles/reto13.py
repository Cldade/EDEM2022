'''
Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
'''
from math import pi, pow

def areaTriangulo(altura:float, base:float):
  return round((base*altura)/2,3)


def areaCirculo(radio:float):
  return round(pi*pow(radio,2),3)