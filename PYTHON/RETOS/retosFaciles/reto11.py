'''
Escribe un programa que pida al usuario los siguientes datos por consola:
Título de la película
Director
Año
País
E introduzca esos valores en una variable GLOBAL llamada "pelicula"
'''
def pelicula() -> dict:
  tituloPeli:str = input('Dime el título de una película: ')
  director:str = input('Dime el director de la película: ')
  anyo:int = int(input('Dime el año de la película: '))
  pais:str = input('Dime el país de la película: ')
  pelicual:dict = {'titulo':tituloPeli, 'director':'x'}