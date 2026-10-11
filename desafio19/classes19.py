from rich import print
from rich import print, inspect

class Livro:
  def __init__(self, titulo, paginas):
    self.titulo = titulo
    self.paginas = paginas
    self.atual = 1
    print( f"[blue]:open_book: Você acabou de abrir o livro [green]{self.titulo}[/] que tem [red]{self.paginas}[/] paginas no total. Você esta na [yellow]{self.atual}ª[/] pagina.[/]")


  def avancar_pagina(self, avanco=1):
    contador =0
    for pagina in range(0, avanco, 1):
        if not self.final_livro():
            self.atual += 1
            print(f"Pagina {self.atual} ->", end="")
            contador += 1
    print(f"Você avançou {contador} paginas e agora esta na {self.atual}")
    if self.final_livro():
      print(f"Você terminou o livro {self.titulo}")

  def final_livro(self) ->bool:
    return True if self.atual == self.paginas else False

l1 = Livro("As 10 coisas que ja aprendi", 20)
l1.avancar_pagina(5)
l1.avancar_pagina(10)
l1.avancar_pagina(50)