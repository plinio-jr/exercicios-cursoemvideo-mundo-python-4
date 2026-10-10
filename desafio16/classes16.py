from rich import print, inspect


class Funcionario:

    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f":handshake:Ola, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}."


f1 = Funcionario("Maria", "Administração", "Diretora")
f2 = Funcionario("Pedro", "TI", "Programador")

inspect(f1)
f1.empresa = 'Javanauta'
inspect(f1)
print(f1.apresentar())
inspect(f2)
print(f2.apresentar())

