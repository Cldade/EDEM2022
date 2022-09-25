from utilidades.interacciones.cordialidad import saludar, despedida
from utilidades.kpis import puntuacion
import pandas

puntos = puntuacion(0)
 
print(f'{saludar("Pedro")} tu puntuación es de {puntos}')
print(f'{despedida("Pedro")} tu puntuación es de {puntos}')

#para instalar en la consola tendremos que poner > pip install paquete



