'''
Desde tu cuenta de replit.com crea un nuevo proyecto. En dicho proyecto, dentro del archivo main.py crea variables que representen los siguientes datos de un contacto:
Nombre
Apellidos
Edad
Email
Teléfono
Casado (verdadero o falso)
Con Hijos (verdadero o falso)
Lista de amigos
Películas vistas (diccionario con clave y valor. El valor será el título de la película)
Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
'''
def reto1():
  nombre = "Claudia"
  apellido = "Daras"
  edad = 23
  email = "claudiadaras@gmail.com"
  telefono = "600087949"
  casado = False
  conHijos = False
  listaDeAmigos = ["Clara", "Oscar", "Irene"]
  peliculasVistas = {1:"Avatar", 2:"Titanic"}
  print(f'Hola {nombre} {apellido} con {edad} años, email {email}, teléfono {telefono}. ¿estas casado? {casado} ¿tienes hijos? {conHijos} su lista de amigos es {listaDeAmigos} y las peliculas vistas son {peliculasVistas}')