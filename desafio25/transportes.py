from abc import ABC, abstractmethod
from rich import print, inspect

class Transporte(ABC):

  def __init__(self, distancia=0, frete=0):
    self.distancia = distancia
    self.frete = frete


  def distancia(self):
    pass


  def frete(self):
    pass


  @abstractmethod
  def calcular_frete(self):
    self


class Moto(Transporte):
  fator = 0.50

  def __init__(self, distancia):
    super().__init__(distancia)

  def calcular_frete(self):
    self.frete = self.distancia * Moto.fator
    return f'{round(self.frete,2)}'


class Caminhao(Transporte):
  fator = 1.20

  def __init__(self, distancia):
    super().__init__(distancia)

  def calcular_frete(self):
    if self.distancia < 50:
      self.frete = 0
      return f'Raio minimo é de 50km'
    else:
      self.frete = self.distancia * Caminhao.fator
      return f'{round(self.frete,2)}'


class Drone(Transporte):
  fator = 9.50
  def __init__(self, distancia):
    super().__init__(distancia)


  def calcular_frete(self):
    if self.distancia > 10:
      self.frete = 0
      return f'Raio minimo é de 50km'
    else:
      self.frete = self.distancia * Drone.fator
      return f'{round(self.frete, 2)}'