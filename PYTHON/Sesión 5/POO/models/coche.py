	
class Coche():
  #Atributos de la clase
  #PAra hacer un atributo provado se pone: '_atributo'
  marca:str
  modelo:str
  color:str
  matricula:str    
  id_seguro:str
  titular:str
  velocidad:float = 0
    
   #Método constructor
  def __init__(self, marca, modelo, color, matricula, id_seguro, titular):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.matricula = matricula
    self.id_seguro = id_seguro
    self.titular = titular
  #Método de arrancar
  def arrancar(self):
    self.velocidad = 10
    print(f'El coche con matricula {self.matricula} ha arrancado')
  #Método de frenar
  def frenar(self, presion: float):
    self.velocidad -= (presion - 10)
    print(f'El coche ha frenado. Su velocidad ahora es {self.velocidad}km/h')
  #Método de acelerar
  def acelerar(self, presion: float):
    self.velocidad += (presion + 10)
    print(f'El coche ha acelerado. Su velocidad ahora es {self.velocidad}km/h')
