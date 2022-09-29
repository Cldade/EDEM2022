'''
Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
'''
def contrasenyaCorrecta(contra:str, contra2:str) -> bool:
  if(contra.lower() == contra2.lower()): return True
  else: return False