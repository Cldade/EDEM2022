#Ejercicio. Diccionario que saque el dni. Nombre, edad, dni y casado
#Imprimir 'El dni de 'nombre' es 'dni''
persona = {"name":"Claudia", "edad":23, "dni":"29216044H", "casado":False}
print(persona["dni"])
print(f'El dni de {persona["name"]} es {persona["dni"]}')