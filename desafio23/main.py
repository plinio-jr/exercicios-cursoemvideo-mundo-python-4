from rich import print, inspect
from poligono import *


def main():
    q = Quadrado(20)
    inspect(q, methods=True)
    print(f'Um quadrado: {q.qtd_lado}cm tem perimetro de {q.perimetro}cm')
    print(f'Um quadrado: {q.qtd_lado}cm tem area de {q.area}cm')

    c = Circulo(12)
    inspect(c, methods=True)
    print(f'Um circulo de um raio {c}cm tem um perimetro de {c.perimetro()}cm')
    print(f'Um circulo de um raio {c}cm tem area de {c.area()}cm')

if __name__ == '__main__':
    main()
