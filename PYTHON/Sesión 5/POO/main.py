from models.coche import Coche

coche1:Coche = Coche('Audi','A3','BLANCO','123456HAS','xx','Claudia')

coche1.arrancar()
print(f'La velocidad del coche 1 actual es: {coche1.velocidad}')

coche2:Coche = Coche('BMW','I5','BLANCO','123456LAS','xx','Juan')
print(f'La velocidad del coche 2 actual es: {coche2.velocidad}')

miTaller: [Coche] = [coche1,coche2]

for coche in miTaller:
  print(f'- {coche.matricula}')

def velocidadCoche(matricula:str):
  for coche in miTaller:
    if(coche.matricula == matricula):
      print(f'Su velocidad es: {coche.velocidad}')