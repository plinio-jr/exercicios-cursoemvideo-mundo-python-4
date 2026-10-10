from rich.panel import Panel
from rich import print, inspect

class Churrasco:
    consumo_padrao = 0.400
    preco_kg = 32.96 #82.40

    def __init__(self, titulo, pessoas=0):
      self.titulo = titulo
      self.pessoas = pessoas


    def __str__(self):
      return f"Esse é o {self.titulo} com {self.pessoas} participantes"

    def analisar(self):
      quantidade = Churrasco.consumo_padrao * self.pessoas
      custo = self.pessoas * Churrasco.preco_kg
      quantidade = self.pessoas * Churrasco.consumo_padrao
      individual = custo / self.pessoas
      conteudo= f'\nAnalisando {self.titulo} com {self.pessoas} convidados'
      conteudo += f"\nCada participante comera 0.4Kg e cada Kg custara R$ 82.40"
      conteudo += f"\nRecomendo comprar {quantidade:.3f}Kg de carne."
      conteudo += f"\nO custo total sera de R${custo:.2f}"
      conteudo += f"\nCada pessoa pagara R${individual:.2f}"
      painel = Panel(conteudo, title=self.titulo)
      print(painel)

c1 = Churrasco("churras dos amigos", 15)
c1.analisar()

c2 = Churrasco("Churrasco do fim de ano", 70)
c2.analisar()
