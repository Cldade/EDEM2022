'''
Escribe un programa que pueda decirte si un número (número entero) es primo o no
'''
def esPrimo(n:int) -> bool:
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True