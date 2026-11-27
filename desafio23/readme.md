Desafio 023: Implemente o seguinte diagrama de classes:

 ________________________
|Poligono{abstract}      | 
|+qtd_lados              |
|------------------------|
|+perimetro() {absctract}|   
|+area()  {absctract}    |   <--------------------
|------------------------|             |         |
                                       |         |
Subclasses:                            |         |
(perimetro/area herancas)              |         |
 ________________________              |         |
|Quadrado                |             |         |
|+lado                   | -------------         |
|------------------------|                       |
|+perimetro()            |                       |
|+area()                 |                       |
|------------------------|                       |
                                                 |
 ________________________                        |
|Circulo                 |                       |
|+raio                   | -----------------------
|------------------------|
|+perimetro()            |
|+area()                 |
|------------------------|
