from rich.panel import Panel
from rich import print
import os

class ControleRemoto:
    canal_minimo:int = 1
    canal_maximo:int = 5
    volume_minimo:int = 1
    volume_maximo:int = 5

    def __init__(self, canal=1, volume=1):
      self.canal:int = canal
      self.volume:int = volume
      self.ligar:bool = False

    def liga_desliga(self):
      self.ligar = not self.ligar

    def passar_canal(self):
      if self.ligar:
        if self.canal == ControleRemoto.canal_maximo:
          self.canal = ControleRemoto.canal_minimo
        else:
          self.canal += 1

    def voltar_canal(self):
      if self.ligar:
        if self.canal == ControleRemoto.canal_minimo:
          self.canal = ControleRemoto.canal_maximo
      else:
        self.canal -= 1

    def aumentar_volume(self):
      if self.ligar:
        if self.volume != ControleRemoto.volume_maximo:
          self.volume += 1

    def diminuir_volume(self):
      if self.ligar:
        if self.volume != ControleRemoto.volume_minimo:
          self.volume -= 1

    def exibir(self):
      conteudo = ''
      if not self.ligar:
          conteudo = f"TV desligada!"
      else:
        conteudo = f"\nCanal = "
        for canal in range(ControleRemoto.canal_minimo, ControleRemoto.canal_maximo + 1):
          if canal == self.canal:
            conteudo += f"[blue on white] {canal} [/]"
          else:
            conteudo += f" {canal} "

        conteudo += '\nVolume = '
        for volume in range(ControleRemoto.volume_minimo, ControleRemoto.volume_maximo +1):
          if volume <= self.volume:
            conteudo += f'[black on cyan] [/]'
          else:
            conteudo += f'[black on white] [/]'

      imagem = Panel(conteudo, title='TV')
      print(imagem)

tv = ControleRemoto()
while True:
  tv.exibir()
  opcao = str(input("\n< CH > - VOL +: "))
  match opcao:
    case '0':
      print("Programa finalizado!")
      break
    case '@':
      tv.liga_desliga()
    case '>':
      tv.passar_canal()
    case '<':
      tv.voltar_canal()
    case '+':
      tv.aumentar_volume()
    case '-':
      tv.diminuir_volume()