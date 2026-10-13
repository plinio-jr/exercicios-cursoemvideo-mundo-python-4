from rich.panel import Panel
from rich import print, inspect

class Caneta:
  def __init__(self, cor = 'azul'):
      opcao = ''
      match cor.lower().strip():
          case 'azul':
              opcao = '[blue]'
          case 'vermelho' | 'vermelha':
              opcao = '[red]'
          case 'verde':
              opcao = '[green]'
          case 'amarelo':
              opcao = '[yellow]'
          case 'ciano':
              opcao = '[cyan]'
          case _:
            opcao ='[white]'
      self.cor = opcao
      self.tampa = True

  def escrever(self, frase):
    if self.tampa == True:
      print(f":prohibited: A caneta esta tampada!")
    else:
      print(f"{self.cor}{frase}[/]")

  def destampar(self):
    self.tampa = False


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')
c4 = Caneta('amarelo')
c5 = Caneta('ciano')
c6 = Caneta('white')
c1.destampar()
c2.destampar()
c3.destampar()
c4.destampar()
c5.destampar()
c6.destampar()
c1.escrever('Ola mundo :globe_showing_Americas:')
c2.escrever('Perigo :warning:')
c3.escrever("Salve :hand_with_fingers_splayed_light_skin_tone:")
c4.escrever("Ola pequeno gafanhoto :vulcan_salute_medium-light_skin_tone:")
c5.escrever('Diamante :gem_stone:')
c6.escrever('teste')