'''
Aplicación de consola que pida:
Nombre
Email
Contraseña
Edad
Aceptar

Cuando tengamos todos los datos se creará un diccionario usuario.
Y mostrar los datos por consola

Codewars --> pagina web para 
'''
persona = {}
persona["name"] = input("¿Cuál es tu nombre?: ")
persona["email"] = input("¿Cuál es tu email?: ")
persona["passw"] = input("¿Cuál es tu contraseña?: ")
persona["edad"] = int(input("¿Cuál es tu edad?: "))
persona["acept"] = input("¿Aceptas? (Y/N): ")
if(persona["acept"] == "Y"):
  respuesta = "has aceptado la política de privacidad"
else:
  respuesta = "no has aceptado la política de privacidad"

print(f'Tú nombre es {persona["name"]}, tú email es: {persona["email"]}, tu contraseña es: {persona["passw"]}, tu edad es: {persona["edad"]}. Y {respuesta}')
