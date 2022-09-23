'''En Python, la estructura es con "elif" y no con "else if"'''

miEdad = 45
if (miEdad >= 60):    
  print('Apuntarse al gym')
elif (miEdad < 60 and miEdad > 30):
  if(miEdad == 45):
    print ('Adulto maduro')
  else:
    print("otro texto")
elif (miEdad == 30):    
  print ('Adulto en su sweet moment')
elif (miEdad < 30 and miEdad >= 18):    
  print ('Adulto joven, todo en orden')
else:    print ('¡A clase!')

#Bucle for
listaCompra = ["agua", "cafe","cerveza"]
for item in listaCompra:
  print(item) #Así imprimimos los elementos de una lista
print(item) #Al salir del bucle la variable item se queda con el último elemento de la lista


lista = [1,2,3,4,5,6,7,8]
for item in lista:
  if(item%2 == 0):
    print(f'{item} es par')
  else:
    continue #Es para que continue con el siguiente valor del bucle
    print(f'{item} es impar')
    #break #Si ponemos aquí el break cuando imprima el primer númeor impar el bucle parará

lista2 = [1,2,3,4,5,6,7,8,9,10]
sumatorio = 0
iteraciones = 0
for numero in lista2:
  sumatorio += numero
  iteraciones += 1
print(f'Suma total {sumatorio}. Iteraciones {iteraciones}')


#Bucle while
lista = [1,2,3,4,5,6,7,8]
while (len(lista) > 3):
  lista.pop() #Para quitar el último elemento. si ponemos entre los paréntesis un número saca el de esa posición
  print(*lista)