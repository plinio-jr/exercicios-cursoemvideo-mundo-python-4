from rich.panel import Panel
from rich import print, inspect

class Gamer:
  def __init__(self, nome, nick):
    self.nome = nome
    self.nick = nick
    self.favoritos = []

  def add_game(self, game):
    self.favoritos.append(game)
    self.favoritos = sorted(self.favoritos, key=str.lower)

  def ficha(self):
      conteudo= f'\nNome real:[blue]{self.nome}[/]'
      conteudo+= f'\nJogos Favoritos:'
      for n, game in enumerate(self.favoritos):
        conteudo+= f'\n:video_game: {game}'
      painel = Panel(conteudo, title=self.nick)
      print(painel)


j1 = Gamer('Fabricio Silva', 'Detonador2025')
j1.add_game("God Of War")
j1.add_game("Minecraft")
j1.add_game("Counter Strike")
j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_game("Super Mario Bros")
j2.add_game("Tibia")
j2.add_game("Tomb Raider")
j1.ficha()
j2.ficha()
inspect(j1)
inspect(j2)
