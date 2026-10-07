 # Exercicios-curso-em-video-mundo-4(orientação a objetos) POO

 ### Anotações das aulas

 ### 1\. Origem e o Porquê da POO (Aulas 01 e 02)

* **Histórico e a Crise do Software:** Na década de 1960, o aumento exponencial na complexidade dos programas gerou a "crise do software"[4][5]. A evolução partiu do código de baixo nível (Assembly)[5] e linguagens lineares (Fortran, COBOL)[6] para linguagens estruturadas (idealizadas por Edsger Dijkstra e a linguagem Algol)[7][8] e modulares[9], culminando na POO[10][11].
* **Os Pioneiros:** Ole-Johan Dahl e Kristen Nygaard criaram a linguagem **Simula** (considerada a primeira linguagem orientada a objetos)[11][12]. Posteriormente, Alan Kay desenvolveu o **Smalltalk**, a interface gráfica, o conceito do laptop (*Dynabook*) e estruturou os conceitos modernos da POO[13].
* **Siglas Principais:** **POO** (*Programação Orientada a Objetos*), **OOP** (*Object-Oriented Programming*) e **OOAD** (*Object-Oriented Analysis and Design*)[3][16].
* **As 6 Vantagens da POO (Mnemônico "COMER NADA"):**
  1. **C**onfiabilidade: alterações em um objeto isolado não corrompem o restante do sistema[17][18].
  2. **O**portunidade: diferentes partes e classes podem ser desenvolvidas em paralelo por uma equipe[17].
  3. **M**anutenibilidade: facilidade de atualizar e otimizar componentes do sistema[17][21].
  4. **E**xtensibilidade: facilidade de adicionar novas funcionalidades sem reconstruir o código do zero[17].
  5. **R**eutilização: reaproveitamento de classes e objetos em projetos futuros[17].
  6. **N**aturalidade: foco na funcionalidade e interface, abstraindo a complexidade interna do código[17].

---

### 2\. Conceitos Fundamentais (Aulas 03 e 04)

* **Classe:** É o modelo, molde ou projeto (análogo à forma de um biscoito ou à planta baixa de uma casa)[28].
* **Objeto:** É a instância concreta criada a partir de uma classe[32].
* **Atributos:** São as características e variáveis de um objeto (ex: `nome`, `idade`, `saldo`)[36].
* **Métodos:** São os comportamentos e funções internas que o objeto pode executar (ex: `depositar()`, `sacar()`)[36][39].
* **Instanciação:** É o ato de gerar um objeto físico/memória a partir de uma classe (`objeto = Classe()`)[33][34].
* **Estado:** O conjunto dos valores atuais dos atributos de um objeto em um determinado instante[40][41].
* **Sintaxe em Python:**
  * Declaração com `class NomeClasse:`[42].
  * Método construtor `def __init__(self):` responsável por inicializar a instância[43][44].
  * O parâmetro `self` referencia a própria instância que está executando o método ou armazenando o atributo[45].

---

### 3\. Recursos do Python e Dunder Methods (Aula 05)

* **Parâmetros Opcionais no Construtor:** Permitem definir valores padrão na inicialização da classe (`def __init__(self, nome='', saldo=0):`)[48][49].
* **Métodos e Atributos Especiais (** **Dunder Methods / Attributes** **):**
  * `__doc__`: Exibe a *docstring* (documentação) da classe[50][51].
  * `__str__`: Personaliza o retorno do objeto ao ser impresso via `print(objeto)`[52][53].
  * `__dict__` ou `__getstate__`: Retorna o estado atual dos atributos do objeto em formato de dicionário[54][55].
  * `__class__`: Identifica a classe de origem de determinado objeto[56].
* **Exemplo Prático (** **ContaBancaria** **):** Implementação de criação de conta com controle de saldo, depósitos e validação de saques para impedir saldos negativos[57].

---

### 4\. Os Pilares da POO em Python

#### 4.1 Herança (Aula 07)

* **Conceito:** Relação do tipo **"É UM"** entre uma **Superclasse** (mãe/ancestral) e uma **Subclasse** (filha/derivada)[69].
* **Generalização vs. Especialização:** A classe mãe reúne os elementos comuns a todas as filhas (generalização), enquanto as filhas adicionam atributos e comportamentos específicos (especialização)[71][73].
* **Sintaxe:** Declara-se a herança passando a classe mãe nos parênteses: `class SubClasse(SuperClasse):`[74].
* **O comando** **super()** **:** Chama métodos da superclasse a partir da subclasse, como a inicialização do construtor ancestral via `super().__init__(...)`[75][76].
* **Modularização:** Organização de classes em arquivos `.py` separados e importação com `from arquivo import Classe`[77].

#### 4.2 Abstração (Aula 08)

* **Conceito:** Focar no essencial para o escopo do projeto, ignorando detalhes desnecessários ou de implementação interna por meio de uma **interface pública**[84].
* **O Módulo** **abc** **(** **Abstract Base Classes** **):** Importado via `from abc import ABC, abstractmethod`[87][88].
* **Classe Abstrata:** Herda de `ABC`, serve unicamente como modelo/contrato base para subclasses e **nunca é instanciada diretamente**[88].
* **Método Abstrato (** **@abstractmethod** **):** Declarado na classe mãe sem implementação de código, **obriga** todas as subclasses concretas a implementá-lo[90].
* **Método Concreto:** Método já programado na classe abstrata que é compartilhado diretamente por todas as subclasses (aplicando o princípio *DRY - Don't Repeat Yourself*)[94][98].

#### 4.3 Encapsulamento (Aulas 10 e 11)

* **Conceito:** Visa proteger o estado interno do objeto contra interferências externas não regulamentadas, garantindo a segurança do sistema[99][100].
* **Filosofia Pythônica (** **Consenting Adults** **):** O Python prioriza "liberdade com responsabilidade" por convenções em vez de proibições rígidas de acesso na linguagem[101].
* **Convenção de Visibilidade:**
  * `atributo` (sem prefixo): Público[105].
  * `_atributo` (1 underline): Protegido (sinaliza para desenvolvedores que não deve ser alterado diretamente fora da classe ou subclasses)[105].
  * `__atributo` (2 underlines): Privado (aplica o *Name Mangling*, alterando internamente o nome para `_NomeClasse__atributo`)[106][107].
* **Acesso a Dados Protegidos:**
  * **Métodos Acessores:** Uso de *Getters* (`get_nota()`) para leitura e *Setters* (`set_nota()`) com validações de dados[108].
  * **Decorador** **@property** **:** Abordagem pythônica e elegante para criar atributos validáveis. Utiliza-se `@property` para a leitura (getter) e `@atributo.setter` para a alteração (setter)[108].

---

### 5\. Aula Extra: A Biblioteca `Rich`

* **Objetivo:** Tornar o terminal visualmente atraente e facilitar a depuração durante o estudo da POO[119].
* **Funcionalidades:**
  * Saída formatada com cores e marcações simples via `from rich import print`[120].
  * Suporte nativo a emojis no terminal[123][124].
  * Criação de painéis emoldurados (`Panel`)[125][126] e tabelas estilizadas (`Table`)[127].
  * **Inspeção de Objetos:** O comando `inspect(objeto)` exibe uma tabela detalhada com o estado, tipo, atributos e métodos de qualquer objeto[130][131].
