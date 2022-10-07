from coche import Coche

class Carrera:
  coches: [Coche]

  def __init__(self, participantes: [Coche]):
    self.coches = participantes

  def iniciaar_carrera(self):
    print('Ha iniciado la carrera. Los participantes son:')
    for coche in self.coches:
      print(f'-> {coche.matricula}')
      