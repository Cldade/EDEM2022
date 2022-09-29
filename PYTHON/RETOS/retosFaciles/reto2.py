'''
Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
'''
def impares(numeroInicial:int, numeroFinal:int) -> list:
  n = numeroInicial
  lista = []
  while (n< numeroFinal):
    if(n%2 != 0): lista.append(n)
    n += 1
  return lista
  