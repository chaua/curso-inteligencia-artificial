---
description: Análise Comparativa da Implementação de Algoritmos Genéticos
---

# 📄 Estudo Dirigido 03

## Atividade

Os alunos devem implementar **Algoritmos Genéticos (AGs)** para resolver um **problema clássico de otimização** e comparar diferentes configurações dos operadores genéticos. O objetivo é analisar o impacto da variação de parâmetros como **crossover, mutação, inicialização da população e critério de parada** no desempenho do AG.

Sugestões de problemas clássicos para implementação:

1. **Problema do Caixeiro Viajante (TSP)** – Encontrar o caminho mais curto entre várias cidades.
2. **Problema da Mochila (Knapsack Problem)** – Selecionar itens para maximizar o valor sem exceder o peso permitido.
3. **Otimização de Funções Matemáticas** – Encontrar o mínimo/máximo de uma função complexa.

{% file src="../.gitbook/assets/ED03 - Instâncias dos problemas.zip" %}

Os alunos devem implementar um **Algoritmo Genético base** e testá-lo com diferentes configurações dos seguintes operadores:

* **Crossover:** Um ponto, dois pontos, uniforme.
* **Mutação:** Taxas baixas, médias e altas.
* **Inicialização da População:** Aleatória vs. baseada em heurísticas.
* **Critério de Parada:** Número fixo de gerações, convergência para uma solução ótima.

O relatório científico (até 6 páginas) deve conter:

1. **Introdução** – Explicação do problema escolhido e justificativa do uso de AGs.
2. **Metodologia** – Implementação do AG e variações testadas.
3. **Resultados** – Comparação quantitativa entre diferentes configurações (tempo de execução, qualidade da solução).
4. **Discussão** – Análise dos impactos das variações nos operadores genéticos.
5. **Conclusão** – Melhor configuração encontrada e sugestões para melhorias futuras.

O relatório deverá ser escrito usando o **template de artigos da SBC**.&#x20;

{% file src="../.gitbook/assets/SBC Conferences Template.zip" %}

## **Entrega**

A entrega deve ser feita **online via GitHub**, no repositório do aluno, dentro do diretório:\
📂 `/ed03/relatorio.pdf`\
📂 `/ed03/codigo/` (Arquivos contendo a implementação do Algoritmo Genético).

## **Material de Apoio**

* [Introdução a Algoritmos Genéticos](https://bioinfo.com.br/algoritmos-geneticos/)
* [Biblioteca DEAP para Algoritmos Evolutivos](https://deap.readthedocs.io/en/master/)
