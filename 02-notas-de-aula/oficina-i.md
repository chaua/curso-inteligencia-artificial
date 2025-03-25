# 🤖 Oficina I

## 1) Caixeiro Viajante&#x20;

Um vendedor precisa visitar uma lista de cidades **exatamente uma vez** e depois retornar à cidade de origem. Cada cidade está conectada a outras por estradas com **custos (ou distâncias)** diferentes. O objetivo é encontrar o **caminho mais curto possível** que percorra todas as cidades e retorne à inicial.

**Definir:**

* Estado inicial&#x20;
* Ações
* Função sucessora
* Teste do objetivo
* Custo do caminho

### Problema

O vendedor deve visitar as cidades: **A, B, C, D**. As distâncias entre as cidades são:

```
     A   B   C   D
A    -   10  15  20
B   10   -   35  25
C   15  35   -   30
D   20  25  30   -
```

Começando pela cidade **A**, qual o menor caminho possível que passa por todas as cidades e retorna a A?

## 2) Jarros de Água

Você possui dois jarros de água com capacidades diferentes, e deseja medir uma **quantidade exata** usando apenas esses jarros. Você pode **encher, esvaziar, ou transferir** água de um jarro para o outro, mas **não há marcações intermediárias**.

**Definir:**

* Estado inicial&#x20;
* Ações
* Função sucessora
* Teste do objetivo
* Custo do caminho

### Problema

Você tem:

* Um jarro de **4 litros**
* Um jarro de **3 litros**

Objetivo: medir exatamente **2 litros**.

Ações permitidas:

* Encher qualquer jarro até o máximo.
* Esvaziar qualquer jarro.
* Transferir água de um jarro para o outro até que o primeiro esvazie ou o segundo encha.

Qual sequência de ações resulta em exatamente 2 litros em um dos jarros?

## **N-Rainhas**

O objetivo é colocar **N rainhas** em um tabuleiro de xadrez NxN de forma que **nenhuma rainha ataque outra**. Lembre-se: uma rainha pode se mover (e atacar) em **linhas, colunas e diagonais**. Você deve encontrar uma **configuração válida**.

**Definir:**

* Estado inicial&#x20;
* Ações
* Função sucessora
* Teste do objetivo
* Custo do caminho

### Problema

Coloque 4 rainhas em um tabuleiro 4x4 de forma que elas **não se ataquem**. Uma solução possível (para visualização) seria:

```
. Q . .
. . . Q
Q . . .
. . Q .
```

## :books: **Referências Bibliográficas**

* **RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010









