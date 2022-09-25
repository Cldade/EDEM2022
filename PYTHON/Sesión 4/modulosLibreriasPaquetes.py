'''
spark --> es un aliibrería
PIP --< para instalar librerías externas

-Librerías --> añade funcionalidades
-Framework --> te marca la forma de como se utilizan las cosas. Django o flask
    - Django --> para desarrollo web. Crea aplicaciónes REST(petición que devuelve una solución sin ver nada). Soluciones back y front
    - Flask --> más cercano a una librería. soluciones de tipo back, es decir REST.
    - Angular --> soluciones para crear aplicaciones web. Tiene un montón de código ya prehecho. Todo está practicamente configurado y definido.

La finalidad del módulo es la reutilización de código, para poder estructurar bien el código.
Siempre se importan al principio del código.
Como se estructura un código python:
    - Imports
    - Funciones
    - Scripting ---> opcional. Normalmente esta parte va en el main.py

'''
'''
import math as m #De esta forma le ponemos un nombre más corta al módulo
m.cos(200)
'''
import math as m 
from math import sqrt, sin, cos #Así solo nos importamos ciertas cosas. Una buena práctica es importar solo lo que vamos a utilizar y no todo el módulo
from cordialidad import saludar

numero: int = 16 
print(f'La raíz cuadrada de {numero} es {m.sqrt(numero)}') #imprime 4.0
print(f'La raíz cuadrada de {numero} es {m.isqrt(numero)}') #imprime 4. Imprime solo la parte entera.

numero: int = 16  
print(f'La raíz cuadrada de {numero} es {sqrt(numero)}') #imprime 4.0
print(f'El Seno de {numero} es {sin(numero)}') #imprime -0.287...
print(f'El Coseno de {numero} es {cos(numero)}') #imprime -0.957...

saludar('Claudia')