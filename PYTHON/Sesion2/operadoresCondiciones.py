'''
PALABRAS RESERVADAS
- and o & --> concatenar condiciones
- as
- assert
- break --> parar una acción
- class --> definir clases
- continue
- def --> definir una función
- del
- elif --> else + if
- else
- except --> para capturar excepciones
- exec
- finally --> si o si se ejecute algo
- for --> bucle
- global --> para definir varibales globales. Para así pueden ser consumidas dentro de cualquier ámbito
- import --> para importar
- in --> dentro de una lista o algo iterable
- is --> para hacer condiciones de tipos
- lambda
- nonlocal
- not
- or --> o una condición u otra
- pass --> saltar una iteración
- raise
- return --> no es obligatorio consumirlo
- try --> para gestionar errores o excepciones
- while --> bucle
- with
- 
'''

a = 0
name = "pepe"

if a == 0:
  name = "martin"

print(name)

#Definición de la función suma
def suma (a,b):
  return a + b

valor = suma(1,2)
print(valor)
'''
#Bucle que pide número hasta que le da uno impar
numeroElegido = int(input("Elige un número: "))
while(numeroElegido % 2 == 0):
  numeroElegido = int(input("Elige un número: "))
'''
#Ejercicio imprimir el número de intentos
numeroElegido = int(input("Elige un número: "))
numeroBuscado = 300
intentos = 3

while(numeroElegido != numeroBuscado and intentos > 0):
  if(numeroElegido > numeroBuscado):
    
    print(f"Te quedan {intentos} intentos")
    numeroElegido = int(input("Has fallado.El número buscado es más pequeño: "))
    intentos -= 1
    
  else:
    
    print(f"Te quedan {intentos} intentos")
    numeroElegido = int(input("Has fallado,el número buscado es más grande: "))
    intentos -= 1

if(intentos == 0):
  print(f"Has perdido, el número era {numeroBuscado}")
else:
  print(f"Has ganado, el número era {numeroBuscado}")


'''
-Por consola el usuario debe acertar un número secreto
-Tiene 3 intentos
-Si acierta a la primera --> puntos += 5 y puntos *=2
- Si acierta en el segundo intneot --> puntos +=5
- Si acerta a la tercera --> puntos +=2
- Si falla todas las feces --> puntos -=2
'''