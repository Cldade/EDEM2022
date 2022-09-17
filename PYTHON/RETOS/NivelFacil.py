#RETO 1:variables que representen los siguientes datos de un contacto
nombre = "Claudia"
apellido = "Daras"
edad = 23
email = "claudiadaras@gmail.com"
telefono = "600087949"
casado = False
conHijos = False
listaDeAmigos = ["Clara", "Oscar", "Irene"]
peliculasVistas = {1:"Avatar", 2:"Titanic"}

#RETO 2: programa capaz de mostrar todos los números impares desde un número de inicio y otro final
numero_inicial = 2
numero_final = 8
n = numero_inicial
while (n<numero_final):
    if n%2 == 0:
      n += 1
      print(n)
    else: n += 1

#RETO 3: programa que sea capaz de mostrar los números del 1 al 100 en orden inverso
n = 100
while (n>0):
    print(n)
    n -= 1

#RETO 4: programa que sea capaz de mostrar los elementos de una lista en orden inverso al original
lista = [1,2,3,4,5]
n = len(lista) -1
while (n >= 0):
  print(lista[n])
  n -= 1