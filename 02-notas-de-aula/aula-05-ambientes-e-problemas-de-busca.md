---
description: Estruturas de problemas, espaços de estados e ambientes de busca.
---

# 🤖 Aula 05 - Ambientes e problemas de busca

{% hint style="info" %}
## **Material da aula**

*
* **Capítulo 1 - RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010.&#x20;
{% endhint %}

## Exemplos de modelagem

### **Quebra-cabeça 8 (8-Puzzle)**

Você tem um tabuleiro 3x3 com 8 peças numeradas e um espaço vazio (`0`). O objetivo é mover as peças uma a uma para que fiquem na ordem certa.

**Objetivo final:** colocar as peças assim:

```
1 2 3
4 5 6
7 8 0
```

#### 👀 **Sensores:**

* O agente consegue **"ver" o tabuleiro atual** e a posição do espaço vazio.

#### 🛠️ **Atuadores (movimentos possíveis):**

* CIMA
* BAIXO
* ESQUERDA
* DIREITA

#### 🔄 **Exemplo: Estado Inicial**

```
1 2 3
4 0 6
7 5 8
```

#### 🔧 **Ações possíveis a partir desse estado:**

| Ação     | Resultado                         |
| -------- | --------------------------------- |
| CIMA     | `0` troca com o número acima      |
| BAIXO    | `0` troca com o número abaixo     |
| ESQUERDA | `0` troca com o número à esquerda |
| DIREITA  | `0` troca com o número à direita  |

Exemplo:\
Aplicando **DIREITA**:

```
ANTES:                DEPOIS:
1 2 3                 1 2 3
4 0 6     ---->       4 6 0
7 5 8                 7 5 8
```

#### 🧩 **1) Estado Inicial**

O tabuleiro como ele está no começo.

#### 🚶 **2) Ações**

Mover a peça para **cima, baixo, esquerda ou direita** do espaço vazio.

#### 🔁 **3) Função Sucessora**

Para cada ação válida, o agente gera um novo estado:

```python
função_sucessora(estado_atual):
    vizinhos = []
    para cada ação em [cima, baixo, esquerda, direita]:
        se for possível aplicar a ação:
            novo_estado = aplicar_acao(estado_atual, ação)
            vizinhos.append(novo_estado)
    retorna vizinhos
```

#### ✅ **4) Teste do Objetivo**

Verifica se o tabuleiro está na seguinte configuração:

```
1 2 3
4 5 6
7 8 0
```

#### 💰 **5) Custo do Caminho**

Cada movimento custa **+1**.

### **Missionários e Canibais**

Temos 3 missionários e 3 canibais em uma margem do rio. O barco pode levar **1 ou 2 pessoas por vez**. Você precisa atravessar todos para o outro lado **sem deixar os canibais em maioria** em nenhum lado.

#### 👀 **Sensores:**

* Quantas pessoas há em cada margem.
* Onde está o barco.

#### 🛠️ **Atuadores:**

* Mover o barco (DIR ou ESQ)
* Colocar/tirar missionários ou canibais no barco

#### 🧩 **1) Estado Inicial**

```
Margem esquerda: 3 missionários, 3 canibais, barco
Margem direita: vazia
```

Visual:

```
[ C C C M M M | B |    |       ]
```

#### 🚶 **2) Ações possíveis**

* Enviar no barco:
  * 1 missionário
  * 1 canibal
  * 2 missionários
  * 2 canibais
  * 1 missionário + 1 canibal\
    → Tanto **ida quanto volta**!

#### 🔁 **3) Função Sucessora**

Para cada ação válida, gerar o novo estado, **desde que** a margem que ficar não tenha mais canibais que missionários.

```python
função_sucessora(estado_atual):
    vizinhos = []
    para cada ação:
        novo_estado = aplicar_acao(estado_atual, ação)
        se novo_estado for seguro (não come ninguém):
            vizinhos.append(novo_estado)
    retorna vizinhos
```

#### ✅ **4) Teste do Objetivo**

Todos os missionários e canibais estão na margem direita:

```
[      |    | B | C C C M M M ]
```

#### 💰 **5) Custo do Caminho**

Cada travessia custa **+1**.

### **Lobo, Cabra e Alface**

#### 🧠 **Resumo do Problema:**

Você é um fazendeiro e precisa atravessar o rio com:

* 🐺 Lobo
* 🐐 Cabra
* 🥬 Alface

O barco só leva você e **um item por vez**.\
⚠️ Se o lobo ficar sozinho com a cabra → 💀\
⚠️ Se a cabra ficar sozinha com a alface → 💀

#### 👀 **Sensores:**

* Onde estão o fazendeiro e os itens.

#### 🛠️ **Atuadores:**

* Levar o lobo / cabra / alface
* Voltar sozinho

#### 🧩 **1) Estado Inicial**

```
Margem esquerda: Fazendeiro, Lobo, Cabra, Alface
Margem direita: vazia
```

Visual:

```
[ F, 🐺, 🐐, 🥬 ] ~~~~ [     ]
```

#### 🚶 **2) Ações possíveis**

* Levar 1 item (ou nada) para o outro lado.

Exemplos:

* Levar a cabra
* Levar o lobo
* Voltar sozinho

#### 🔁 **3) Função Sucessora**

Aplica as ações e verifica se o estado resultante é **seguro**:

```python
função_sucessora(estado_atual):
    vizinhos = []
    para cada item em [nada, lobo, cabra, alface]:
        novo_estado = atravessar(estado_atual, item)
        se estado_novo é seguro:
            vizinhos.append(novo_estado)
    retorna vizinhos
```

#### ✅ **4) Teste do Objetivo**

Todos os itens e o fazendeiro estão na margem direita:

```
[     ] ~~~~ [ F, 🐺, 🐐, 🥬 ]
```

#### 💰 **5) Custo do Caminho**

Cada travessia custa **+1**.



## :books: **Referências Bibliográficas**

* **RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010









