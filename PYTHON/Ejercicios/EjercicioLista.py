#Ejercicio: lista de la compra que tenga 5 elementos. Mostrar por consola los dos últimos elementos

lista = ["pan", "leche", "huevos", "cereales", "aceite"]
print(lista[len(lista)-1], lista[len(lista)-2])
print(lista[-1], lista[-2])
print(*lista[-2:])
print(*lista[0:1:2])

#Eliminar números repetidos de una lista
misNumeros = [1,2,3,4,5,6,7,8,9,3,2,5,3]
misNumerosNoRepetidos = set(misNumeros)
#Los dos print siguientes son iguales
print(*set(misNumeros))
print(*misNumerosNoRepetidos)

#Podemos poner directamente la lista dentro del set
miOtroSetDeDatos = set(["a","a","a","b"])
print(*miOtroSetDeDatos)

#Función ordenar listas
lista = [1,4,3,7,6,9,2]
print(*lista)
#Ordenar una lista de menor a mayor
lista.sort()
print(*lista)
#Ordenar una lista de mayor a menor
lista.sort(reverse=True)
print(*lista)
#Función invertir una lista
lista = [1,4,3,7,6,9,2]
print(*lista)
lista.reverse()
print(*lista)