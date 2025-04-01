---
description: Principais marcos históricos e evolução da IA até os dias atuais.
---

# 🧠 Aula 04 - Agentes inteligentes

{% hint style="info" %}
## **Material da aula**

* [Slides](slides/Aula04%20-%20Conceito%20de%20agentes%20inteligentes.pdf)
* **Capítulo 2 - RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010.&#x20;
{% endhint %}

## 1. Introdução

A compreensão de agentes inteligentes é um dos pilares fundamentais da Inteligência Artificial (IA), pois eles representam entidades capazes de perceber o ambiente ao seu redor e agir sobre ele de forma racional.&#x20;

***

## 2. Conceito de Agente Inteligente

* Um **agente** é qualquer entidade capaz de:
  * **Perceber** seu ambiente por meio de **sensores**.
  * **Agir** sobre o ambiente por meio de **atuadores**.

**Exemplos:**

* **Agente humano**:
  * Sensores: olhos, ouvidos, mãos.
  * Atuadores: pernas, boca, partes do corpo.
* **Agente robô**:
  * Sensores: câmeras, microfones, sensores infravermelho.
  * Atuadores: motores, caixas de som.
* **Robô aspirador de pó**:
  * Sensores: câmeras, sensores de proximidade.
  * Atuadores: rodas, sistema de aspiração.

***

## 2. Função do Agente

* A função de um agente é uma **descrição matemática abstrata** que mapeia uma **sequência de percepções** para uma **ação**:

$$
f: P^* \rightarrow A
$$

* O **programa do agente** é a implementação concreta dessa função.

***

## 3. Agente Racional

* Um agente racional é aquele que realiza a **ação correta**, com base em:
  * **Percepções anteriores**
  * **Conhecimento do ambiente**
  * **Objetivo definido**
* A **medida de desempenho** avalia a eficácia do agente com base em critérios como:
  * Sujeira removida (no exemplo do aspirador)
  * Tempo, energia e ruído gerado

{% hint style="info" %}
## Observações:

* Um agente racional não é onisciente — ele **não conhece o resultado de suas ações com certeza**.
* Ele busca **maximizar o desempenho esperado** com base nas informações disponíveis.
{% endhint %}

***

## 4. Aprendizado

* O aprendizado permite ao agente **ajustar seu comportamento** com base na experiência.
* Envolve **exploração** do ambiente e adaptação futura de ações.

***

## 5. Natureza dos Ambientes

* A especificação do ambiente é essencial para o projeto de agentes:
  * **Performance** (desempenho)
  * **Environment** (ambiente)
  * **Actuators** (atuadores)
  * **Sensors** (sensores)

**Exemplos de ambientes:**

<table data-card-size="large" data-view="cards"><thead><tr><th>Agente</th><th>Performance</th><th>Environment</th><th>Actuators</th><th>Sensors</th></tr></thead><tbody><tr><td><strong>Motorista de táxi</strong></td><td>Segurança, tempo de viagem, conforto, lucro</td><td>Ruas, trânsito, passageiros, sinais de trânsito</td><td>Volante, pedal, freio, buzina, portas</td><td>Câmeras, GPS, velocímetro, microfones</td></tr><tr><td><strong>Sistema de diagnóstico médico</strong></td><td>Precisão no diagnóstico, tempo de resposta</td><td>Prontuários, sintomas, exames</td><td>Exibição de resultados, alertas</td><td>Dados clínicos, históricos, sensores médicos</td></tr><tr><td><strong>Análise de imagens de satélite</strong></td><td>Precisão na detecção, cobertura, atualização</td><td>Imagens de satélite, clima, terreno</td><td>Interface gráfica, marcação de áreas</td><td>Imagens multiespectrais, sensores ópticos</td></tr><tr><td><strong>Robô de seleção de peças</strong></td><td>Precisão, velocidade, taxa de erro</td><td>Linha de montagem, peças, bandejas</td><td>Braços robóticos, pinças, motores</td><td>Câmeras, sensores de proximidade, RFID</td></tr><tr><td><strong>Instrutor de inglês interativo</strong></td><td>Clareza, engajamento, progresso do aluno</td><td>Interface digital, alunos, exercícios</td><td>Fala sintética, animações, feedback visual</td><td>Microfone, reconhecimento de voz, câmeras</td></tr><tr><td><strong>Sistema de engajamento em redes sociais</strong></td><td>Cliques, tempo de uso, compartilhamentos</td><td>Plataforma social, conteúdo, usuários</td><td>Notificações, recomendações, feed</td><td>Cliques, curtidas, tempo de visualização</td></tr></tbody></table>

***

## :books: **Referências Bibliográficas**

* **RUSSELL, Stuart J.; NORVIG, Peter.** _Inteligência Artificial: Uma Abordagem Moderna._ 3. ed. São Paulo: Prentice Hall, 2010
