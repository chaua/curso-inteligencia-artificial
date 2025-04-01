---
description: Estruturas de problemas, espaços de estados e ambientes de busca.
---

# 🌎 Aula 05 - Ambientes e problemas de busca

{% hint style="info" %}
## **Material da aula**

* [Slides](slides/Aula05%20-%20Resolu%C3%A7%C3%A3o%20de%20problemas%20por%20meio%20de%20busca.pdf)
* **Capítulo 3 - RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010.&#x20;
{% endhint %}

## 1. Introdução

A resolução de problemas por meio de busca é uma abordagem central em Inteligência Artificial (IA), utilizada para tomar decisões e encontrar soluções em ambientes onde o agente não possui todas as respostas prontas.

## 1. Tipos de Ambientes

### 1.1 Observabilidade

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Completamente Observável</strong></td><td>O agente tem acesso total ao estado do ambiente por meio dos sensores.</td><td>Jogo de xadrez — todas as peças visíveis.</td></tr><tr><td><strong>Parcialmente Observável</strong></td><td>O agente não consegue observar todo o ambiente, exigindo memória ou inferência.</td><td>Dirigir em neblina — visão limitada.</td></tr></tbody></table>

### 1.2 Determinismo

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Determinístico</strong></td><td>O resultado das ações é previsível e não envolve incerteza.</td><td>Resolver um quebra-cabeça.</td></tr><tr><td><strong>Estocástico</strong></td><td>As ações podem levar a diferentes resultados, mesmo no mesmo estado.</td><td>Jogo de pôquer — depende de sorte e blefe.</td></tr></tbody></table>

### 1.3 Episodicidade

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Episódico</strong></td><td>As ações e percepções são independentes entre si.</td><td>Classificação de imagens médicas.</td></tr><tr><td><strong>Sequencial</strong></td><td>As ações atuais influenciam as percepções e decisões futuras.</td><td>Jogo de xadrez ou dirigir um carro.</td></tr></tbody></table>

### 1.4 Dinamicidade

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Estático</strong></td><td>O ambiente não muda enquanto o agente decide o que fazer.</td><td>Resolver palavras cruzadas.</td></tr><tr><td><strong>Dinâmico</strong></td><td>O ambiente pode mudar a qualquer momento, mesmo sem ação do agente.</td><td>Controlar um drone — o vento altera o ambiente.</td></tr><tr><td><strong>Semi-dinâmico</strong></td><td>O ambiente é estático, mas a performance do agente pode piorar com o tempo.</td><td>Prova com tempo — ambiente fixo, tempo importa.</td></tr></tbody></table>

### 1.5 Continuidade

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Discreto</strong></td><td>O agente possui percepções e ações bem definidas e finitas.</td><td>Jogo da velha ou xadrez.</td></tr><tr><td><strong>Contínuo</strong></td><td>As percepções e/ou ações são baseadas em valores contínuos (infinas possibilidades).</td><td>Controle de um braço robótico.</td></tr></tbody></table>

### 1.6 Número de Agentes

<table data-card-size="large" data-view="cards"><thead><tr><th>Tipo</th><th>Descrição</th><th>Exemplo</th></tr></thead><tbody><tr><td><strong>Agente Único</strong></td><td>Apenas um agente atua no ambiente, sem interferência de outros.</td><td>Robô limpando uma sala vazia.</td></tr><tr><td><strong>Multi-agente</strong></td><td>Há vários agentes interagindo, cooperando ou competindo entre si.</td><td>Jogo de futebol de robôs ou mercado financeiro com bots.</td></tr></tbody></table>

***

## 2. Tipos de Agentes

* **Agentes de reflexo simples**: Reagem diretamente à percepção atual.
* **Agentes baseados em modelo**: Mantêm representação interna do estado do mundo.
* **Agentes baseados em objetivos**: Agem para atingir objetivos específicos.
* **Agentes com aprendizagem**: Adaptam-se com base na experiência.
* **Agentes de resolução de problemas**: Planejam sequências de ações para alcançar um objetivo.

***

## 3. Agentes de Resolução de Problemas

* Utilizam **representações atômicas** dos estados (sem estrutura interna).
* Focados em:
  * **Maximizar a medida de desempenho**
  * **Alcançar um objetivo**
  * **Planejar ações futuras**

#### Processo

1. **Formulação do objetivo**: o que o agente deseja alcançar.
2. **Formulação do problema**: como o agente pode alcançar o objetivo.

***

## 4. Componentes de um Problema de Busca

Todo problema de busca pode ser descrito por:

1. **Estado inicial**: ponto de partida do agente.
2. **Ações**: conjunto de operações possíveis.
3. **Modelo de transição**: resultado da aplicação de uma ação.
4. **Teste de objetivo**: verificação se o objetivo foi alcançado.
5. **Custo do caminho**: soma dos custos das ações realizadas.

> O espaço de estados é representado por um **grafo dirigido**:
>
> * **Vértices**: estados
> * **Arestas**: ações entre estados

***

## 5. Exemplos de Problemas

### :broom: Mundo do Aspirador de Pó

<table><thead><tr><th width="190">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Localização do aspirador (ex: A ou B) e estado de limpeza (sujo/limpo).</td></tr><tr><td><strong>Ações</strong></td><td>Esquerda, Direita, Aspirar, Nada.</td></tr><tr><td><strong>Modelo de transição</strong></td><td>A ação muda a posição ou o estado do local (de sujo para limpo).</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>Todos os locais estão limpos.</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Número de ações executadas (ou energia consumida, ou tempo).</td></tr></tbody></table>

### :jigsaw: Quebra-Cabeça de 8 Peças

<table><thead><tr><th width="188.5">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Posição atual das 8 peças e do espaço vazio no tabuleiro 3x3.</td></tr><tr><td><strong>Ações</strong></td><td>Mover peça para cima, baixo, esquerda ou direita (se houver espaço).</td></tr><tr><td><strong>Modelo de transição</strong></td><td>Troca da peça com o espaço vazio.</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>Posições das peças correspondem ao estado final desejado.</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Quantidade de movimentos (pode ser uniforme ou ponderado).</td></tr></tbody></table>

### :crown: Problema das 8 Rainhas

<table><thead><tr><th width="189">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Tabuleiro vazio.</td></tr><tr><td><strong>Ações</strong></td><td>Colocar uma rainha em uma linha, respeitando as restrições.</td></tr><tr><td><strong>Modelo de transição</strong></td><td>Avança para a próxima linha com posição válida para a rainha.</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>Oito rainhas posicionadas sem atacar umas às outras.</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Número de rainhas colocadas (geralmente uniforme).</td></tr></tbody></table>

### :door: Labirinto

<table><thead><tr><th width="192">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Posição inicial do agente no labirinto.</td></tr><tr><td><strong>Ações</strong></td><td>Mover-se para cima, baixo, esquerda ou direita (se permitido).</td></tr><tr><td><strong>Modelo de transição</strong></td><td>Movimento para a nova célula do labirinto.</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>O agente alcança a posição de destino (ex: ossinho 🦴 para o cão 🐶).</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Número de passos (ou distância total percorrida).</td></tr></tbody></table>

### :ice\_cube: Cubo Mágico (Rubik's Cube)

<table><thead><tr><th width="191">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Disposição atual das cores nas faces do cubo.</td></tr><tr><td><strong>Ações</strong></td><td>Rotacionar uma das 6 faces em sentido horário/anti-horário.</td></tr><tr><td><strong>Modelo de transição</strong></td><td>Aplicação de uma rotação altera os adesivos em 3 eixos.</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>Todas as faces do cubo têm cores uniformes.</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Número de rotações realizadas.</td></tr></tbody></table>

## :potable\_water: Problema das Garrafas (5L e 2L)

<table><thead><tr><th width="191">Elemento</th><th>Descrição</th></tr></thead><tbody><tr><td><strong>Estado inicial</strong></td><td>Garrafa de 5L cheia; garrafa de 2L vazia.</td></tr><tr><td><strong>Ações</strong></td><td>Transferir água, esvaziar garrafa, encher garrafa.</td></tr><tr><td><strong>Modelo de transição</strong></td><td>O volume das garrafas muda conforme a ação.</td></tr><tr><td><strong>Teste de objetivo</strong></td><td>Garrafa de 2L contém exatamente 1 litro.</td></tr><tr><td><strong>Custo do caminho</strong></td><td>Número de ações realizadas (ou tempo/energia consumida).</td></tr></tbody></table>

***

## :books: **Referências Bibliográficas**

* **RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010









