Desafio 023: Implemente o seguinte diagrama de classes:

--------------------------
|Poligono{abstract}      | 
|+qtd_lados              |
|------------------------|
|+perimetro() {absctract}|   
|+area()  {absctract}    |   <--------------------
--------------------------             |         |
                                       |         |
Subclasses:                            |         |
(perimetro/area herancas)              |         |
--------------------------             |         |
|Quadrado                |             |         |
|+lado                   | ------------          |
|------------------------|                       |
|+perimetro()            |                       |
|+area()                 |                       |
--------------------------                       |
                                                 |
--------------------------                       |
|Circulo                 |                       |
|+raio                   | -----------------------
|------------------------|
|+perimetro()            |
|+area()                 |
--------------------------
