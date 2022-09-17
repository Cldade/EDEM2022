'''
Las variables estan alojadas en la memoria de forma temporal
Presentes siempre que se ejecuta la aplicación
String --> str
'''

#Imprimir por pantalla una varibale
#Antes de esta linea la variable nombre no va a existir.
nombre:str = "Claudia"
print("!Hola " + nombre + "!")
#La 'f' permite formatear las variables, por lo que no hay que poner todo el rato el '+'
print(f"!Hola {nombre}¡")


'''
Aunque nombre lo hayamos declarado como string 
no va a dar problemas si luego le asignamos un entero
'''
nombre = 200
nombre = 200*2
print(nombre)
print(f"!Hola {nombre}¡")

nombre = "Claudia"
bienvenida = f"Hola {nombre}"
print(bienvenida)
