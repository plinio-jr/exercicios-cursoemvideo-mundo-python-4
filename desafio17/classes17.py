from rich.panel import Panel
from rich import print, inspect

class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco


  def __str__(self) -> str:
    return f"{self.nome} R${self.preco}"


  def etiqueta(self) -> str:
    conteudo = f'{self.nome}'
    etiqueta = Panel(conteudo, title='Produto')
    print(etiqueta)

p1 = Produto("Notebook", 3000)
p2 = Produto("Mouse",100)

print(p1)
print(p2)