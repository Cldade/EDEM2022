import datetime

#Creamos los diccionarios para cada disco
disco1 = {'nombre':'disco1', 'artista':'uno', 'anyo':2001, 'precio': 1, 'genero':'Pop'}
disco2 = {'nombre':'disco2', 'artista':'dos', 'anyo':2002, 'precio':2, 'genero':'Electro'}
disco3 = {'nombre':'disco3', 'artista':'tres', 'anyo':2003, 'precio':3, 'genero':'Reggaeton'}
disco4 = {'nombre':'disco4', 'artista':'cuatro', 'anyo':2004, 'precio':4, 'genero':'Rock'}
disco5 = {'nombre':'disco5', 'artista':'cinco', 'anyo':2005, 'precio':5, 'genero':'Metal'}
disco6 = {'nombre':'disco6', 'artista':'seis', 'anyo':2006, 'precio':6, 'genero':'Death Metal'}
disco7 = {'nombre':'disco7', 'artista':'siete', 'anyo':2007, 'precio':7, 'genero':'Black Metal'}
disco8 = {'nombre':'disco8', 'artista':'ocho', 'anyo':2008, 'precio':8, 'genero':'Black Metal'}
disco9 = {'nombre':'disco9', 'artista':'nueve', 'anyo':2009, 'precio':9, 'genero':'Electro'}
#Creamos la lista que contiene la información de todos los discos
listaDiscos = [disco1,disco2,disco3,disco4,disco5,disco6,disco7,disco8,disco9]

def comprarDisco():
  numero = 1
  comprados = [] #Lisa donde estarán los comprados por el usuario

  #Bucle que muestra los discos disponibles para comprar
  for disco in listaDiscos:
    print(f'El disco {numero} tiene el nombre de: {disco["nombre"]}, su artista es: {disco["artista"]}, el año de publicación es: {disco["anyo"]}, su precio es de: {disco["precio"]}€, y su género es: {disco["genero"]}')
    numero += 1

  #Bucle que permite al usuario elegir que discos quiere comprar
  discocomprado = int(input('Si quieres un disco dime su número, si no pulsa 0: '))
  while (discocomprado != 0):
    comprados.append(listaDiscos[discocomprado-10])
    discocomprado = int(input('Si quieres otro disco dime su número, si no pulsa 0: '))

  #Bucle que muestra los disco comprados
  descuento = 0
  precio = 0
  precioSinDescuento = 0
  for disco in comprados:
    if(disco["genero"] == 'Black Metal' or disco["genero"] == 'Electro'): 
      descuento += disco["precio"]*0.3
      precio += disco["precio"]-descuento
      precioSinDescuento += disco["precio"]
    else: 
      precio += disco["precio"]
      precioSinDescuento += precio
      
  #Imprimimos la fecha y hora de la compra
  print(f'La fecha y hora de compra: {datetime.datetime.today()}')
  #Imprimimos el precio de la compra
  print(f'El precio de la compra es: {precioSinDescuento}€')
  if(descuento != 0):
    #Imprimimos el descuento de la compra
    print(f'El descuento de la compra es: {descuento}€')
    #Imprimimos el precio final
    print(f'Tu precio final con descuento es: {round(precio,2)}€')
  
 
  