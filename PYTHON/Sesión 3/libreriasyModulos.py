#Pip herramienta para poder instalar otras librerias
import time
import datetime 
import calendar

print(f'El año 2020 es bisiesto? {calendar.isleap(2020)}')

#- Fecha y hora actual
print(f'La fecha y hora actual es: {datetime.datetime.today()}')
print(f'Fecha y Hora actual: {datetime.datetime.now()}')
#- El día actual
print(f'La fecha y hora actual es: {datetime.datetime.today().day}')
#- El año actual
print(f'La fecha y hora actual es: {datetime.datetime.today().strftime("%Y")}')
#- Mes actual
print(f'el nombre dle mes es: {datetime.datetime.today().strftime("%B")}')
#- Número del mes actual
print(f'Estamos en el mes: {datetime.datetime.today().month}')
print(f'el nombre dle mes es: {datetime.datetime.today().strftime("%m")}')
#- Número de la semana actual
print(f'el número de la semana es: {datetime.datetime.today().strftime("%W")}')
#- Día del año
print(f'el día del año es: {datetime.datetime.today().strftime("%j")}')
#- Día del mes
print(f'el día del mes es: {datetime.datetime.today().day}')
print(f'el día del mes es: {datetime.datetime.today().strftime("%d")}')
#- Día de la semana
print(f'El día de la semana es: {datetime.datetime.today().strftime("%A")}')


#Imprimir el primer día de la semana (Monday)
print(f'{calendar.day_name[0]}')
#Imprimir el primer mes (Monday)
print(calendar.month_name[1])



miFecha = '23/09/2022'

print(datetime.datetime.strptime(miFecha, '%d/%M/%Y'))
