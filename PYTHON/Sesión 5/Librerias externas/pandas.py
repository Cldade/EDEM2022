import pandas as pd
import chunk #bloques, para hacer las lecturas más grandes
import re #expresiones regulares, permiten hacer busquedas sobre datos que nosotrso queramos

#Leer csv
#Cuando ponemos df hacemos referencia a un dataframe
pokemon_csv_df = pd.read_csv('pokemon_data.csv',dtype = {'Name':str, 'Type 1':str, 'Speed':int, 'Generation':int})

#Leer excel
#pokemon_excel_df = pd.read_excel('pokemon_data.xlsx')

#Leer un txt
#pokemon_txt_df = pd.readcsv('pokemon_data.txt',delimeter = '\t')


#Imprimir los valores
print(pokemon_csv_df)
#Imprimir solo las 5 primeras filas
print(pokemon_csv_df.head(5))
#Imprimir los 5 últimos
print(pokemon_csv_df.tail(5))

#Conocer los nombre de las columnas
print(pokemon_csv_df.columns)

#Obtener todos los nombres
nombres = pokemon_csv_df["Name"]
print(*nombres)

#Obtener todos sus nombres y velocidades
#Opcion 1:
#nombres_velocidades = pokemon_csv_df[['Name','Speed']]
#print(nombres_velocidades)

#Opcion 2:
lista_columnas = ['Name', 'Speed']
nombres_velocidades = pokemon_csv_df[lista_columnas]
print(nombres_velocidades)


#Obtener los primeros 5 nombres
primeros_5 = pokemon_csv_df['Name'][0:5]
print(primeros_5)


#Obtener primera fila
print(pokemon_csv_df.iloc[0])

#Obtener las 3 primeras filas 
print(pokemon_csv_df.iloc[0:3])
