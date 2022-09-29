'''
Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
'''
def mostrarOrdenInverso() -> list:
  n = 100
  lista = []
  while n > 0:
    lista.append(n)
    n -= 1
  return lista
