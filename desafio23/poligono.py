from abc import ABC, abstractmethod
from rich import print, inspect
from math import pi


class Poligono(ABC):
  def __init__(self, qtd_lados):
    self.qtd_lados = qtd_lados

  @abstractmethod
  def perimetro(self) -> float:
    pass

  @abstractmethod
  def area(self) -> float:
    pass

class Quadrado(Poligono):
  def __init__(self, qtd_lado = 1):
    super().__init__(4)
    self.qtd_lado = qtd_lado

  def perimetro(self, qtd_lado):
    return qtd_lado * 4

  def area(self, qtd_lado):
    return qtd_lado ** 2


class Circulo(Poligono):
  def __init__(self, raio = 1):
    super().__init__(0)
    self.raio = raio

  def perimetro(self):
    return 2 * pi * self.raio

  def area(self):
    return pi * self.raio**2