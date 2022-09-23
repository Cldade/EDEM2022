'''
Las variables estan alojadas en la memoria de forma temporal
Presentes siempre que se ejecuta la aplicación
String --> str
Las tuplas son estaticas en longitud. Si las declaramos con 5 valores, se mantendrán estos valores
Los decimales siempre con punto (INGLÉS)
En las listas se pueden introducir diccionarios, tuplas, strings, int. Es decir, lo que se quiera.
Las constantes se declaran por convención con mayusculas. Si quisieramos cambiarle durante el código el valor,
     python nos dejaría, pero las mayusculas solo se utilizan para constantes.
'''

'''
TIPOS:
-Datos primitivos:
    bool
    int
    float
    complex
    str
-Datos complejos:
    list [..., ...]
    tuple(..., ...)
    dict {key:value, key:value, ...}
    set
    range --> para hacer rangos
    frozenset --> set congelado
    bytes
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

'''
BOOL
'''
casado:bool = True

print(f'Casado? {casado}')

'''
LIST
'''
miLista:[str] = ["Martin", "Juan", "Pablo"]
print(*miLista) #Imprime la lista, sin necesitar el uso de un bucle

