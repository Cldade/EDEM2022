'''
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
'''
def bisiesto(anyo:int) -> bool:
  bisiesto = False
  if (anyo%4 == 0 and ((anyo%100 == 0 and anyo%400 == 0) or ( anyo%100 != 0))):
    bisiesto = True
  return bisiesto