from abc import ABC, abstractmethod
from rich import print, inspect

class BebidaQuente(ABC):

  def preparar(self):
    self.preparar


  def ferver_agua(self):
    self.ferver_agua


  @abstractmethod
  def misturar(self):
    pass


  @abstractmethod
  def servir(self):
    pass


class Cafe(BebidaQuente):
  print('Preparando o cafe')


  def misturar(self):
    self.misturar
    print('Misturando o cafe')
    return self.misturar


  def servir(self):
    self.servir
    print('Servindo o cafe')
    return self.servir


class Cha(BebidaQuente):
  print('Preparando o cha')


  def misturar(self):
    self.misturar
    print('Misturando o cha')
    return self.misturar


  def servir(self):
    self.servir
    print('Servindo o cha')
    return self.servir


class Leite(BebidaQuente):
  print('Preparando o leite')


  def misturar(self):
    self.misturar
    print('Misturando o leite')
    return self.misturar


  def servir(self):
    self.servir
    print('Servindo o leite')
    return self.servir