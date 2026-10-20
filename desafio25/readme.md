Desafio 025: Crie classes capazes de calcular fretes de veiculos diferentes

Transporte{abstract}
----------------------
+distancia
+frete
----------------------
+calc_frete(){abstract}
Heranças

Caminhao
----------------------
fator = 1.20
+calc_frete()
obs: minimo 50 km.
Moto
----------------------
fator = 0.50
+calc_frete()
obs: livre.
Drone
----------------------
fator = 9.50
+calc_frete()
obs:maximo 10 km
