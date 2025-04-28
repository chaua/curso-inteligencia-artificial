---
description: Conceitos e introdução ao Hill Climbing e Simulated Annealing.
---

# 🧗‍♀️ Aula 08 - Busca Local

{% hint style="info" %}
## **Material da aula**

* Slides
* **Capítulo 3.6 - 3.7 - RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010.&#x20;
{% endhint %}

## 1. Introdução

A **Busca Local** é uma classe de algoritmos de otimização que visa encontrar soluções satisfatórias para problemas em espaços de busca muito grandes, nos quais abordagens completas são inviáveis devido ao custo computacional. Diferentemente da busca cega ou heurística tradicional, a busca local foca na **melhoria incremental** de uma única configuração, sem considerar todo o histórico de estados.

***

## 2. Características Gerais

* Trabalha com **espaços de estados contínuos ou discretos grandes**, onde manter uma árvore de busca completa é impraticável.
* Opera sobre **uma única solução atual**, movendo-se para vizinhos com base em critérios locais.
* Não mantém estrutura de busca (como árvore ou grafo).
* Usada principalmente para **otimização** e não para busca de caminhos.

***

## 3. Modelagem

* **Estado atual**: uma configuração viável do problema.
* **Função objetivo** $$f(n)$$: mede a qualidade de um estado.
* **Vizinhança**: conjunto de estados próximos ao estado atual (com pequena variação).
* **Critério de parada**: pode ser número máximo de iterações, tempo, ou convergência.

***

## 4. Principais Algoritmos de Busca Local

### 4.1 Hill Climbing (Subida de Encosta)

Algoritmo que sempre se move para o vizinho com melhor valor da função objetivo.

```python
def hill_climbing(estado_inicial, funcao_objetivo, funcao_sucessora):
    estado = estado_inicial

    for _ in range(MAX_ITERACOES):
        vizinhos = funcao_sucessora(estado)
        if not vizinhos:
            break  # sem vizinhos para explorar

        # seleciona o melhor vizinho com base na função objetivo
        melhor_vizinho = max(vizinhos, key=funcao_objetivo)

        # se nenhum vizinho for melhor, encerra a busca
        if funcao_objetivo(melhor_vizinho) <= funcao_objetivo(estado):
            break

        # atualiza o estado atual
        estado = melhor_vizinho

    return estado

```

**Variantes**

* **Steepest Ascent**: avalia todos os vizinhos e escolhe o melhor.
* **First-Choice**: seleciona o primeiro vizinho melhor encontrado.
* **Random-Restart**: executa múltiplas buscas com estados iniciais aleatórios.

**Vantagens e Desvantagens**

* Simples e eficiente.
* Pode ficar preso em:
  * **Ótimos locais**
  * **Platôs**
  * **Costas íngremes**

### 4.2 Busca Tabu

A **Busca Tabu** é um algoritmo de busca local com memória que evita ciclos e melhora a exploração do espaço de busca. Para isso, mantém uma **lista tabu** contendo movimentos ou soluções recentemente exploradas, que são temporariamente proibidas (tabus), a fim de evitar que o algoritmo revisite estados já analisados.

```python
def busca_tabu(estado_inicial, 
               funcao_objetivo, 
               funcao_sucessora,
               tamanho_tabu=5):
    estado_atual = estado_inicial
    melhor_estado = estado_inicial
    lista_tabu = []

    for _ in range(MAX_ITERACOES):
        vizinhos = funcao_sucessora(estado_atual)

        # Remove vizinhos que estão na lista tabu (exceto aspiração)
        candidatos = [s for s in vizinhos if s not in lista_tabu]
        if not candidatos:
            break  # não há vizinhos válidos

        # Seleciona o melhor candidato entre os vizinhos válidos
        melhor_vizinho = max(candidatos, key=funcao_objetivo)

        # Atualiza melhor solução global
        if funcao_objetivo(melhor_vizinho) > funcao_objetivo(melhor_estado):
            melhor_estado = melhor_vizinho

        # Atualiza estado atual e lista tabu
        estado_atual = melhor_vizinho
        lista_tabu.append(estado_atual)
        if len(lista_tabu) > tamanho_tabu:
            lista_tabu.pop(0)  # mantém o tamanho máximo da lista tabu

    return melhor_estado

```

#### Vantagens

* Evita **ciclos locais** e **retorno a ótimos locais**.
* Permite **exploração intensiva e diversificada** do espaço de busca.
* Pode ser combinada com outras técnicas (ex.: busca por entornos variáveis, algoritmos genéticos).

#### Desvantagens

* **Complexidade maior** que métodos simples como Hill Climbing.
* **Parâmetros sensíveis**: tamanho da lista tabu, critérios de aspiração e definição de vizinhança.
* Pode consumir mais memória, dependendo da estratégia de armazenamento.

### 4.3 Simulated Annealing (SA)

Algoritmo estocástico inspirado no processo físico de **resfriamento térmico de materiais**. Permite movimentos para piores soluções com certa probabilidade.

**Funcionamento**

* A cada iteração, escolhe um vizinho.
* Se for melhor: aceita.
* Se for pior: aceita com probabilidade $$p = e^{-\Delta E/T}$$, onde:
  * $$\Delta E$$: degradação na função objetivo.
  * $$T$$: temperatura atual (decrescente com o tempo).

```python
import math
import random

def simulated_annealing(estado_inicial, 
                        funcao_objetivo, 
                        funcao_sucessora,
                        temperatura_inicial=1.0, 
                        taxa_resfriamento=0.95):
    estado_atual = estado_inicial
    melhor_estado = estado_inicial
    temperatura = temperatura_inicial

    while temperatura > 1e-5:
        for _ in range(MAX_ITERACOES_CONGELAMENTO):
            vizinho = random.choice(funcao_sucessora(estado_atual))
            delta = funcao_objetivo(vizinho) - funcao_objetivo(estado_atual)

            if delta > 0:
                estado_atual = vizinho
                if funcao_objetivo(estado_atual) > funcao_objetivo(melhor_estado):
                    melhor_estado = estado_atual
            else:
                probabilidade = math.exp(delta / temperatura)
                if random.random() < probabilidade:
                    estado_atual = vizinho

        temperatura *= taxa_resfriamento  # aplica resfriamento

    return melhor_estado
```

**Propriedades**

* Evita mínimos locais.
* Controlado por um **cronograma de temperatura** (annealing schedule).
* Com decaimento lento de $$T$$, pode convergir para o ótimo global.

***

### 5. Comparação entre algoritmos

<table><thead><tr><th width="127">Algoritmo</th><th width="130">Ciclos evitados</th><th width="109.5">Exploração global</th><th width="89.5">Memória</th><th width="103.5">Estocástico</th><th>Otimalidade garantida</th></tr></thead><tbody><tr><td>Hill Climbing</td><td>Não</td><td>Não</td><td>Não</td><td>Não</td><td>Não</td></tr><tr><td>Busca Tabu</td><td>Sim</td><td>Sim</td><td>Sim</td><td>Opcional</td><td>Não (mas robusta)</td></tr><tr><td>Simulated Annealing</td><td>Parcialmente</td><td>Sim</td><td>Não</td><td>Sim</td><td>Não (mas possível)</td></tr></tbody></table>

***

## :books: **Referências Bibliográficas**

* **RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010
