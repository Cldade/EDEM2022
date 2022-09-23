'''
SINTAXIS DE UNA FUNCIÓN
def nombre_funcion (parametros) -> str: #la flechita indica el tipo del valor de retorno
'''

def suma(a:int,b:int) -> int:
  return a + b

'''
por referencia --> lista, diccionario y una cadena de texto
Al pasar una variable por referencia, lo que hagamos en la función con ella afectará a la variable original.
'''

# Función con Parámetros No Tipados

def miFuncionConParametros(a: str,b: str):    
  print(f"¡{a}, {b}!") 

# llamando la función y pasándole algunos parámetros
miFuncionConParametros('Hola', 'Mundo')
miFuncionConParametros(a='Hola',b='Mundo')
miFuncionConParametros(b='Hola',a='Mundo')
miFuncionConParametros('Hola',b='Mundo')
#miFuncionConParametros('Hola',a='Mundo')


# Función con muchos parámetros
def miFuncionConMultiplesParametros(*elementos) :    
  for elemento in elementos:        
    print(f"Elemento: {elemento}") 

# llamando la función y pasándole una lista de parámetros
lista = [1, 2, 3, 4, 5]
miFuncionConMultiplesParametros(lista)


'''
Por consola, solicitar al usuario un número
- El programa debe pedir números hasta que el usuario introduzca un año bisiesto
 1. '''
#Función que devuelve si un año es bisiesto (True) o si no lo es (False)
def bisiesto(anyo:int) -> bool:
  bisiesto = False
  if (anyo%4 == 0 and ((anyo%100 == 0 and anyo%400 == 0) or ( anyo%100 != 0))):
    bisiesto = True
  return bisiesto


anyo = int(input("Escribe un año: "))
#Mientras sea falso que el año es bisiesto pide más años
while (not bisiesto(anyo)):
  anyo = int(input("Escribe otro año: "))

print('¡Has escrito un año bisiesto!')

#Otra opción de Buscar un año bisiesto
def leap_year(year: int):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

while not leap_year(int(input('introduce año: '))):
    print('ese año no es bisiesto')
print('has acertado')


''' 
PASO POR REFERENCIA
Paso de parámetros por Referencia Los valores simples se pasan, por defecto, por valor
Los valores complejos se pasan, por defecto, por referencia 
''' 

# las listas al ser complejos se pasan por referencia
# Esto quiere decir que si la función edita el parámetro,
# éste se edita también en origen 
def doblar_valores(numeros):    
  for indice,numero in enumerate(numeros):        
    numeros[indice] *= 2
    print(numero)

ns = [10,50,100]
#doblar_valores(ns) #Si lo pasamos así nos modificará la lista original
doblar_valores(ns[:])#Así le pasamos los valores y no modificará la lista ns

print(f'Lista Original Modificada: {ns}')
