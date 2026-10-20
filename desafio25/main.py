import transportes
from desafios.desafio25.transportes import Caminhao
from desafios.desafio25.transportes import Moto
from desafios.desafio25.transportes import Drone


def main():
    distancia = 80
    m = Moto(distancia)
    c = Caminhao(distancia)
    d = Drone(distancia)

    print(f'Distancia em KM: {m.distancia}')
    print(f'Valor do frete: R$ {m.calcular_frete()}')
    print(f'Distancia em KM: {c.distancia}')
    print(f'Valor do frete: {c.calcular_frete()}')
    print(f'Distancia em KM: {d.distancia}')
    print(f'Valor do frete: {d.calcular_frete()}')


if __name__ == '__main__':
    main()