 # Exercicios-curso-em-video-mundo-4(orientação a objetos) POO

 ### Anotações das aulas

 ### 1\. Histórico e a Crise do Software

* **A Origem:** A POO surgiu como resposta à **crise do software** na década de 1960[1][3]. A evolução dos paradigmas partiu das linguagens de baixo nível (Assembly)[5] e linguagens lineares (Fortran, COBOL, Basic, C)[6] para as linguagens estruturadas (idealizadas por Edsger Dijkstra com a linguagem Algol 60)[4][7] e modulares[8].
* **Os Pioneiros:** Kristen Nygaard criou o **Simula** (a primeira linguagem com objetos)[9][10] e Alan Kay desenvolveu o **Smalltalk**, a interface gráfica e o conceito do laptop (*Dynabook*)[11].
* **Siglas Principais:** **POO** (*Programação Orientada a Objetos*), **OOP** (*Object-Oriented Programming*) e **OOAD** (*Object-Oriented Analysis and Design*)[15][16].

---

### 2\. As 6 Vantagens da POO (Mnemônico "COMER NADA")

Para memorizar os principais benefícios da orientação a objetos, utiliza-se o mnemônico **"COMER NADA"**[17]:

1. **C**onfiabilidade: O isolamento entre as partes traz segurança e evita que alterações em um objeto corrompam outros[17][18].
2. **O**portunidade: Permite que diferentes partes do sistema sejam desenvolvidas em paralelo por uma equipe[17][19].
3. **M**anutenibilidade: Facilita a atualização, correção e otimização de módulos[17][20].
4. **E**xtensibilidade: Permite adicionar novas funcionalidades sem reconstruir o código do zero[17][21].
5. **R**eutilizável: Objetos e classes criados podem ser reaproveitados em múltiplos projetos[17].
6. **N**aturalidade: O foco do programador fica nas funcionalidades e na interface pública, e não no funcionamento interno[17].

---

### 3\. Conceitos Fundamentais

* **Objeto como Variável Evoluída:** Objetos são variáveis sofisticadas que, além de armazenar múltiplos dados, contêm e executam suas próprias funções/métodos[26].
* **Classe:** É o molde, forma ou projeto estrutural do objeto[27].
* **Objeto:** É a instância concreta criada a partir de uma classe[29][30].
* **Atributos:** Características que o objeto possui (dados)[31][32].
* **Métodos:** Ações e comportamentos que o objeto pode realizar[31][33].
* **Instanciação:** O ato de gerar um objeto físico na memória a partir da classe[30][34].
* **Estado:** O conjunto de valores dos atributos de um objeto em um determinado momento[35].

---

### 4\. Estrutura em Python e Dunder Methods

* **Declaração:** Utiliza-se `class NomeClasse:` e o método construtor `def __init__(self):` para inicializar os atributos de instância[36]. O parâmetro `self` referencia a própria instância que está executando o código[42][43].
* **Atributos e Métodos Mágicos (** **Dunder Methods/Attributes** **):**
  * `__doc__`: Acessa a documentação (*docstring*) da classe[44].
  * `__str__`: Define o retorno amigável do objeto em texto ao ser impresso[47][48].
  * `__dict__` e `__getstate__`: Exibem o estado interno dos atributos em formato de dicionário[49][50].
  * `__class__`: Exibe a classe de origem do objeto[51].

---

### 5\. Os Pilares da POO em Python

#### 5.1 Herança

* **Conceito:** Relação do tipo **"É UM"** entre uma **Superclasse** (mãe) e uma **Subclasse** (filha)[52]. A subclasse herda todos os atributos e métodos da classe mãe e pode adicionar ou especializar comportamentos[52].
* **Sintaxe:** Declara-se com `class SubClasse(SuperClasse):` e usa-se o comando `super()` para invocar o construtor da superclasse[37][57].

#### 5.2 Abstração

* **Conceito:** Focar no essencial para o escopo do sistema e ignorar detalhes irrelevantes por meio de uma **interface pública**[58][59].
* **Módulo** **ABC** **(** **Abstract Base Classes** **):** Importa-se a classe `ABC` e o decorador `@abstractmethod`[60].
* **Classes e Métodos Abstratos:** Uma **classe abstrata** serve apenas de base para suas subclasses e não pode virar objetos diretamente[63]. O **método abstrato** não possui código na mãe e obriga todas as subclasses a implementá-lo[62].

#### 5.3 Encapsulamento

* **Conceito:** Protege o estado interno do objeto contra interferências não autorizadas, garantindo a integridade do sistema[69][70].
* **Filosofia Pythônica (** **Consenting Adults** **):** O Python adota convenções de visibilidade em vez de barreiras de bloqueio rígidas ("liberdade com responsabilidade")[71]:
  * **Público** (`atributo`): Acesso livre[74][75].
  * **Protegido** (`_atributo`): Um underline indica ao desenvolvedor que não deve ser alterado diretamente fora da classe ou subclasses[74].
  * **Privado** (`__atributo`): Dois underlines acionam o *Name Mangling* (mutilação de nome)[77][78].
* **Acesso a Dados:** Pode ser feito por **Getters e Setters**[79] ou pela abordagem pythônica com o decorador **@property** para criar atributos validáveis[79].

#### 5.4 Polimorfismo

* **Conceito:** Significa "muitas formas"; é a capacidade de reutilizar um mesmo nome de método para executar comportamentos diferentes[85][86].
* **Inclusão / Sobrescrita (** **Override** **):** Ocorre quando uma subclasse reescreve um método herdado da superclasse[87].
* **Sobrecarga (** **Overload** **):**
  * **Métodos:** Em Python, é adaptado via `@single_dispatch_method` da biblioteca `functools`[90].
  * **Operadores:** Permite personalizar o comportamento de operadores lógicos e matemáticos (`+`, `==`, `&lt;=`, etc.) redefinindo dunder methods (`__add__`, `__eq__`, `__iadd__`, `__le__`, etc.)[93].
* **Duck Typing:** Prática fundamentada no princípio *"Se parece um pato, nada como um pato e faz quack, provavelmente é um pato"*, focando no que o objeto sabe fazer e não no seu tipo de classe[99].

---

### 6\. Biblioteca `Rich` (Aula Extra)

* A biblioteca `Rich` permite personalizar as saídas do terminal[102], adicionando **cores e formatações**, **emojis**, **painéis** (`Panel`)[103], **tabelas** (`Table`)[104], **inspeção visual de objetos** com `inspect()`[105] e formatação detalhada de exceções com `traceback`[106].
