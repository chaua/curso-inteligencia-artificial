# 📓 Revisão 02

## Computação Evolutiva

### Questão 1

A Computação Evolutiva é inspirada em um processo natural. Qual alternativa representa corretamente essa fonte de inspiração?

a. Evolução das espécies por seleção natural\
b. Redes Neurais Biológicas\
c. Dinâmica de partículas em sistemas físicos\
d. Processos de inferência lógica\
e. Otimização matemática clássica

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** A Computação Evolutiva é baseada na teoria da evolução por seleção natural, proposta por Darwin, em que soluções melhores sobrevivem e se reproduzem.

</details>

### Questão 2

Qual dos itens abaixo representa um componente típico de um algoritmo evolutivo?

a. Sistema especialista baseado em regras\
b. Representação genotípica e operadores de cruzamento e mutação\
c. Rede bayesiana probabilística\
d. Grafo acíclico direcionado\
e. Árvore de decisão supervisionada

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Algoritmos evolutivos utilizam representações genotípicas de soluções e operadores como cruzamento e mutação para explorar o espaço de busca.

</details>

### Questão 3

Em um algoritmo genético, qual o principal objetivo da operação de seleção?

a. Garantir diversidade genotípica\
b. Otimizar o número de gerações\
c. Escolher os indivíduos mais aptos para reprodução\
d. Reduzir o número de mutações\
e. Eliminar a elitização do processo

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A seleção visa identificar os indivíduos com melhor desempenho para compor a próxima geração, favorecendo a convergência para boas soluções.

</details>

### Questão 4

Qual das opções melhor define um algoritmo evolutivo?

a. Algoritmo determinístico baseado em lógica formal\
b. Algoritmo recursivo para ordenação de dados\
c. Algoritmo baseado em redes de Petri\
d. Algoritmo probabilístico inspirado em processos evolutivos naturais\
e. Algoritmo construído a partir de árvores de decisão

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** Algoritmos evolutivos são métodos estocásticos que simulam o processo de evolução natural para resolver problemas de otimização.

</details>

### Questão 5

Em um algoritmo genético, a operação de **mutação** tem como principal função:

a. Garantir a reprodução dos melhores indivíduos\
b. Introduzir diversidade na população\
c. Maximizar o número de gerações\
d. Corrigir soluções malformadas\
e. Evitar o uso de operadores de cruzamento

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A mutação altera aleatoriamente partes do genótipo de um indivíduo, introduzindo diversidade e ajudando a evitar a convergência prematura.

</details>

### Questão 6

A representação de soluções em algoritmos evolutivos pode ser feita de várias formas. Qual das opções abaixo **não** é comumente utilizada?

a. Cadeias binárias\
b. Vetores de números reais\
c. Árvores sintáticas\
d. Matrizes booleanas\
e. Grafos cíclicos com pesos negativos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** Representações baseadas em cadeias, vetores e árvores são comuns. Grafos cíclicos com pesos negativos não são representações típicas devido à complexidade e dificuldade de avaliação.

</details>

### Questão 7

Qual das abordagens a seguir é mais eficaz quando o algoritmo evolutivo está convergindo prematuramente para uma solução subótima?

a. Aumentar a pressão seletiva\
b. Reduzir a taxa de mutação\
c. Aumentar o tamanho da população e aplicar mutações mais frequentes\
d. Eliminar os operadores de cruzamento\
e. Utilizar somente seleção elitista

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Aumentar o tamanho da população e intensificar a mutação pode ajudar a escapar de ótimos locais e promover exploração do espaço de busca.

</details>

## Algoritmos Genéticos

### Questão 1

Algoritmos Genéticos (AGs) pertencem a qual categoria de métodos de otimização?

a. Métodos determinísticos exatos\
b. Metaheurísticas estocásticas inspiradas na natureza\
c. Métodos heurísticos baseados em gradiente\
d. Algoritmos simbólicos baseados em lógica formal\
e. Técnicas supervisionadas de aprendizado de máquina

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** AGs são metaheurísticas estocásticas que simulam a evolução natural, explorando soluções por meio de recombinação e seleção.

</details>

### Questão 2

Considere as etapas de um algoritmo genético: I. Avaliação de aptidão, II. Inicialização, III. Crossover, IV. Seleção, V. Mutação. Qual a ordem correta de execução em um ciclo evolutivo típico?

a. II → I → III → IV → V\
b. II → I → IV → III → V\
c. I → II → IV → V → III\
d. IV → II → I → V → III\
e. II → IV → I → III → V

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Após a inicialização, avalia-se a aptidão, selecionam-se os indivíduos, aplica-se o crossover e, por fim, a mutação.

</details>

### Questão 3

A convergência de um algoritmo genético para soluções subótimas pode ser causada por:

a. Alta taxa de crossover e elitismo\
b. Baixa taxa de mutação e falta de diversidade\
c. Alto número de gerações e população grande\
d. Uso de representação em ponto flutuante\
e. Seleção por torneio com grande variabilidade

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A baixa diversidade genética impede a exploração eficiente do espaço de busca, levando à convergência prematura.

</details>

### Questão 4

Qual das afirmativas a seguir descreve corretamente uma característica essencial dos algoritmos genéticos?

a. Sempre encontram a solução ótima global\
b. Utilizam derivadas para atualizar os cromossomos\
c. Trabalham com múltiplas soluções simultaneamente\
d. Requerem inicialização com soluções conhecidas\
e. Só funcionam com variáveis discretas

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** AGs operam com uma população de soluções, permitindo exploração paralela do espaço de busca e maior robustez.

</details>

### Questão 5

O crossover em ordem (Order Crossover - OX) é especialmente adequado para:

a. Problemas com variáveis contínuas em ponto flutuante\
b. Representações binárias de genes\
c. Algoritmos baseados em regras simbólicas\
d. Funções lógicas com árvores de decisão\
e. Problemas de permutação, como sequenciamento e roteamento

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** O crossover em ordem preserva a sequência relativa dos elementos e é indicado para problemas onde a solução é uma permutação.

</details>

### Questão 6

No crossover em ordem (OX), qual é o comportamento esperado ao aplicar o operador?

a. Gerar filhos com todos os genes em ordem crescente\
b. Combinar intervalos de um pai e preencher o restante com a ordem do outro pai\
c. Trocar os genes entre os pais posição a posição\
d. Gerar filhos com mutações gaussianas\
e. Realizar cruzamento bit a bit com probabilidade 0.5

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** O OX seleciona uma subsequência de um pai e preenche as posições restantes com os elementos do outro pai, mantendo a ordem relativa.

</details>

### Questão 7

Dado `P1 = [A, B, C, D, E, F, G]` e `P2 = [D, E, F, A, G, B, C]`, aplique o crossover em ordem com o segmento entre as posições 2 e 4 de `P1`. Qual parte intermediária será herdada diretamente?

a. \[B, C, D]\
b. \[A, B, C]\
c. \[C, D, E]\
d. \[D, E, F]\
e. \[C, D, E, F]

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** As posições 2 a 4 de `P1` são \[B, C, D], que serão herdadas diretamente no filho gerado por OX.

</details>

### Questão 8

O crossover aritmético é uma técnica de recombinação comumente usada quando:

a. Os indivíduos são codificados como cadeias binárias\
b. A representação é ordinal ou categórica\
c. Os genes são valores contínuos em ponto flutuante\
d. O problema exige apenas mutações discretas\
e. A população possui representação simbólica

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Crossover aritmético gera novos genes como combinação linear dos genes dos pais, aplicável à representação em ponto flutuante.

</details>

### Questão 9

Se dois pais têm os genes `x1 = 2.0` e `x2 = 4.0`, e o crossover aritmético usa um coeficiente alfa = 0.25, qual será o valor do gene do filho?

a. 1.5\
b. 2.5\
c. 2.75\
d. 3.5\
e. 3.0

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** O gene do filho será `0.25 * 2.0 + 0.75 * 4.0 = 0.5 + 3.0 = 3.5`. O crossover aritmético gera combinações ponderadas dos genes parentais.

</details>

### Questão 10

A representação **em ordem** (ou ordinal) é comumente utilizada em algoritmos evolutivos para resolver:

a. Problemas de classificação com múltiplas classes\
b. Problemas de otimização contínua em alta dimensão\
c. Problemas de lógica simbólica com restrições booleanas\
d. Problemas que requerem redes neurais profundas\
e. Problemas de roteamento ou ordenação, como o Caixeiro Viajante

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** A representação em ordem é ideal para problemas onde a solução é uma permutação de elementos, como o problema do Caixeiro Viajante (TSP)

</details>

### Questão 11

Qual das alternativas representa corretamente uma cadeia válida na representação em ordem para um problema com 5 cidades?

a. \[5, 4, 3, 2, 1]\
b. \[1, 1, 2, 3, 4]\
c. \[0, 2, 3, 3, 1]\
d. \[2.5, 3.7, 4.2, 1.8, 0.9]\
e. \[a, b, c, d, e]

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** Uma permutação válida deve conter todos os elementos uma única vez. A cadeia \[5, 4, 3, 2, 1] é uma permutação válida dos números 1 a 5.

</details>

### Questão 12

A representação **em ponto flutuante** é mais adequada quando:

a. As variáveis do problema são contínuas e possuem domínio real\
b. As soluções precisam ser enumeradas em listas discretas\
c. O algoritmo usa apenas mutações bit a bit\
d. A representação binária for mais simples de implementar\
e. Os dados de entrada são do tipo booleano

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** Quando os parâmetros do problema variam continuamente, como pesos de funções ou coordenadas, a representação em ponto flutuante é apropriada.

</details>

### Questão 13

Em algoritmos com representação em ponto flutuante, a mutação é frequentemente realizada por:

a. Troca de bits por operadores lógicos\
b. Alterações estruturais por árvores sintáticas\
c. Modificação do valor de genes com pequenas perturbações gaussianas\
d. Troca de posições entre elementos do vetor\
e. Reversão do vetor genético

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Em representações contínuas, a mutação geralmente utiliza ruído gaussiano para modificar os genes de maneira suave e controlada.

</details>

### Questão 14

Uma desvantagem da representação em ponto flutuante em relação à binária é:

a. Dificuldade de representar variáveis reais\
b. Maior chance de elitismo prematuro\
c. Requer operadores específicos para cruzamento e mutação\
d. Menor diversidade genética inicial\
e. Inviabilidade de modelar problemas reais

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A representação contínua exige operadores específicos para garantir variações úteis nos genes, o que aumenta a complexidade da implementação.

</details>

### Questão 15

O objetivo da seleção dos sobreviventes em um algoritmo evolutivo é:

a. Escolher os indivíduos com maior diversidade\
b. Garantir que os indivíduos menos aptos não sejam descartados\
c. Selecionar os indivíduos com menor custo computacional\
d. Determinar quais indivíduos farão parte da próxima geração\
e. Reduzir o espaço de busca para acelerar o algoritmo

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** A seleção dos sobreviventes decide quais indivíduos permanecem na população após operadores genéticos, assegurando progresso evolutivo.

</details>

### Questão 16

Qual das estratégias abaixo **não** é uma abordagem comum de seleção de sobreviventes?

a. Seleção elitista\
b. Substituição total aleatória\
c. Sobreposição de gerações\
d. Substituição geracional\
e. Seleção baseada em fitness

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Substituição aleatória total não é comum, pois ignora completamente a qualidade dos indivíduos, comprometendo a eficácia da evolução.

</details>

### Questão 17

Na estratégia de **elitismo**, qual é o procedimento adotado?

a. Clonar todos os indivíduos com aptidão acima da média\
b. Garantir que os piores indivíduos sobrevivam para manter diversidade\
c. Aplicar mutações adicionais aos indivíduos menos aptos\
d. Preservar os melhores indivíduos da geração anterior na nova geração\
e. Utilizar apenas seleção por torneio para determinar sobreviventes

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** O elitismo assegura que os melhores indivíduos não sejam perdidos entre gerações, promovendo a retenção de boas soluções.

</details>

### Questão 18

Uma vantagem do uso de elitismo em algoritmos evolutivos é:

a. Aumentar a diversidade genética\
b. Reduzir a complexidade computacional\
c. Garantir que a aptidão da população não diminua\
d. Evitar o uso de operadores de cruzamento\
e. Eliminar a necessidade de avaliação de fitness

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Ao preservar os melhores indivíduos, o elitismo garante que a qualidade da população nunca piore, promovendo progresso contínuo.

</details>

### Questão 19

Na substituição geracional com elitismo, uma porcentagem dos melhores indivíduos é mantida. O restante da população:

a. É preenchido com indivíduos gerados aleatoriamente\
b. É mantido igual ao da geração anterior\
c. É preenchido com os filhos gerados por cruzamento e mutação\
d. É removido sem critérios de avaliação\
e. É clonado diretamente a partir dos melhores indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Os melhores indivíduos são mantidos, e os demais são substituídos pelos filhos gerados, combinando preservação e inovação.

</details>

### Questão 20

No contexto de algoritmos genéticos com codificação binária, o operador de crossover de **um ponto** realiza:

a. A divisão dos indivíduos em um ponto e a troca das partes subsequentes\
b. A troca de um único bit entre dois indivíduos\
c. A substituição aleatória de bits nos pais\
d. A clonagem do indivíduo com melhor aptidão\
e. A recombinação sem uso de probabilidade

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** No crossover de um ponto, escolhe-se uma posição na cadeia binária e troca-se a parte posterior entre dois pais.

</details>

### Questão 21

Considere dois indivíduos representados por cadeias binárias: `P1 = 11001` e `P2 = 10111`. Qual o resultado do crossover de um ponto na posição 2 (após o segundo bit)?

a. `P1' = 11001`, `P2' = 10111`\
b. `P1' = 11111`, `P2' = 10001`\
c. `P1' = 11111`, `P2' = 10001`\
d. `P1' = 11111`, `P2' = 10001`\
e. `P1' = 11111`, `P2' = 10001`

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** O crossover em posição 2 gera `P1' = 11|111` e `P2' = 10|001`, resultando nas novas cadeias `11111` e `10001`.

</details>

### Questão 22

A operação de **mutação binária** normalmente consiste em:

a. Inverter todos os bits da cadeia\
b. Trocar pares de bits entre dois indivíduos\
c. Alterar aleatoriamente bits específicos com baixa probabilidade\
d. Substituir a cadeia por uma nova gerada aleatoriamente\
e. Usar funções booleanas para combinar genes

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A mutação binária altera bits individuais com baixa probabilidade, como forma de manter diversidade genética.

</details>

### Questão 23

Qual das afirmativas está correta sobre a taxa de mutação em algoritmos genéticos com codificação binária?

a. Deve ser sempre superior a 50% para garantir diversidade\
b. Normalmente é alta, acima de 30%, para promover exploração\
c. Pode ser ignorada quando o crossover é bem projetado\
d. É irrelevante para algoritmos com elitismo\
e. Deve ser moderada, pois taxas altas prejudicam a convergência

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** Taxas altas de mutação podem transformar o algoritmo em uma busca aleatória. O ideal é uma taxa moderada, como 1% a 5%.

</details>

### Questão 24

Em um algoritmo genético com representação binária, a principal função do operador de **crossover** é:

a. Introduzir soluções completamente novas no espaço de busca\
b. Garantir convergência prematura\
c. Recombinar informação genética de pais para gerar filhos potencialmente melhores\
d. Substituir o papel da mutação para diversificação\
e. Controlar a taxa de sobrevivência dos indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** O crossover combina partes de dois pais, buscando explorar boas soluções por meio da recombinação genética.

</details>

### Questão 25

A seleção por roleta viciada (ou roleta proporcional) é baseada em qual princípio?

a. Escolha aleatória de indivíduos com probabilidade uniforme\
b. Seleção dos indivíduos mais distantes no espaço de busca\
c. Proporcionalidade entre a aptidão do indivíduo e sua chance de ser selecionado\
d. Probabilidade inversa à aptidão dos indivíduos\
e. Seleção determinística dos melhores indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A roleta viciada atribui a cada indivíduo uma probabilidade de seleção proporcional à sua aptidão, favorecendo soluções melhores.

</details>

### Questão 26

Na seleção por torneio, dois ou mais indivíduos são escolhidos aleatoriamente. Qual critério é usado para selecionar o vencedor?

a. Indivíduo com melhor aptidão entre os selecionados\
b. Indivíduo selecionado por sorteio\
c. Indivíduo com menor valor de aptidão\
d. Indivíduo com maior diversidade genotípica\
e. Indivíduo com maior taxa de mutação

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** A seleção por torneio seleciona aleatoriamente um grupo de indivíduos e escolhe o de maior aptidão como vencedor do torneio.

</details>

### Questão 27

Qual é uma vantagem da seleção por torneio em relação à roleta viciada?

a. Maior foco em diversidade genotípica\
b. Simplicidade de implementação e controle da pressão seletiva\
c. Garantia de convergência global\
d. Redução do número de operadores genéticos necessários\
e. Utilização de estatísticas bayesianas para escolha dos indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A seleção por torneio é simples de implementar e permite ajuste direto da pressão seletiva pelo tamanho do torneio.

</details>

### Questão 28

Em um ambiente altamente ruidoso, qual método tende a ser mais robusto em relação a flutuações da aptidão?

a. Seleção por roleta viciada\
b. Seleção determinística por elitismo\
c. Seleção por torneio\
d. Seleção aleatória uniforme\
e. Seleção por g

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A seleção por torneio é menos sensível a pequenas variações de aptidão, sendo mais estável em ambientes com ruído.

</details>

### Questão 29

Uma possível desvantagem da seleção por roleta viciada em comparação à seleção por torneio é:

a. Excesso de elitismo\
b. Rejeição de indivíduos com alta aptidão\
c. Baixa aleatoriedade\
d. Dependência da normalização da aptidão\
e. Dificuldade em promover competição entre os indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** A roleta viciada requer normalização da aptidão para evitar enviesamento excessivo, o que pode ser problemático em distribuições assimétricas.

</details>

### Questão 30

Na etapa de inicialização de um algoritmo evolutivo, qual é o objetivo principal da criação da população inicial?

a. Reutilizar indivíduos da geração anterior\
b. Estabelecer uma população com soluções otimizadas\
c. Criar uma população diversificada de soluções candidatas\
d. Iniciar o processo de mutação genética\
e. Maximizar a função de aptidão desde a primeira geração

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A população inicial deve conter indivíduos diversos para permitir ampla exploração do espaço de busca ao longo das gerações.

</details>

### Questão 31

Qual das estratégias abaixo é comumente utilizada para gerar uma população inicial diversificada?

a. Geração aleatória com distribuição uniforme no espaço de busca\
b.Reutilização de soluções elitistas de execuções anteriores\
c. Clonagem de um único indivíduo ótimo\
d. Introdução manual de soluções com conhecimento especializado\
e. Uso de gradiente descendente para inicializar indivíduos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** A geração aleatória com distribuição uniforme permite uma boa cobertura do espaço de busca, promovendo diversidade inicial.

</details>

### Questão 32

Em certos casos, pode-se usar conhecimento prévio do problema para gerar parte da população inicial. Essa prática é chamada de:

a. Recombinação dirigida\
b. Heurística de elitismo\
c. Crossover determinístico\
d. Mutação de base fixa\
e. Inicialização informada ou guiada

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** A inicialização informada incorpora conhecimento do domínio para criar indivíduos potencialmente promissores desde o início.

</details>

## Computação em Enxames

### Questão 1

A Computação em Enxames (Swarm Intelligence) é inspirada em:

a. Comportamentos coletivos de organismos sociais\
b. Processos neurobiológicos de sinapses\
b. Cadeias de Markov em estados discretos\
d. Regras de inferência lógica proposicional\
e. Técnicas de agrupamento supervisionado

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** A Computação em Enxames se baseia no comportamento distribuído e auto-organizado de populações naturais, como formigas e pássaros.

</details>

### Questão 2

No algoritmo Particle Swarm Optimization (PSO), as partículas ajustam sua posição com base em:

a. Vizinhança genotípica e pressão seletiva\
b. Resultados anteriores de mutações e cruzamentos\
c. Conhecimento individual e da melhor solução global\
d. Elitismo multigeracional e pressão fitness\
e. Regras simbólicas pré-programadas

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Em PSO, cada partícula considera sua melhor posição e a melhor posição do enxame para guiar seu movimento.

</details>

### Questão 3

O Algoritmo Ant Colony Optimization (ACO) é especialmente adequado para:

a. Problemas contínuos com gradiente conhecido\
b. Problemas de roteamento e caminhos mínimos\
c. Problemas de classificação linear \
d. Otimização simbólica com lógica fuzzy\
e. Mineração de dados supervisionada

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** ACO é eficaz para problemas combinatórios como o Caixeiro Viajante, simulando o uso de feromônios pelas formigas.

</details>

### Questão 4

Em ACO, o feromônio tem qual papel fundamental?

a. Restringir a diversidade genética\
b. Estimular soluções aleatórias\
c. Guiar a escolha de caminhos mais promissores\
d. Representar a função de aptidão como variável contínua\
e. Realizar mutações em grafos direcionados

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** O feromônio representa uma forma de memória distribuída, indicando a qualidade dos caminhos explorados pelas formigas.

</details>

### Questão 5

Qual das afirmativas caracteriza corretamente uma vantagem da Computação em Enxames?

a. Baixa aplicabilidade em problemas reais\
b. Alta dependência de derivadas analíticas\
c. Exclusividade para problemas com representação binária\
d. Capacidade de encontrar soluções boas sem modelagem matemática explícita\
e. Inviabilidade em ambientes dinâmicos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** A Computação em Enxames é robusta e eficaz mesmo quando não se conhece uma modelagem matemática precisa do problema.

</details>

### Questão 6

O algoritmo Particle Swarm Optimization (PSO) é inspirado em:

a. Comportamento coletivo de bandos de aves ou cardumes de peixes\
b. Dinâmica de populações predador-presa\
c. Interações neuronais em redes profundas\
d. Evolução genética por mutações e cruzamentos\
e. Árvores de decisão supervisionadas

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** O PSO simula o movimento coletivo de seres como pássaros ou peixes, onde cada indivíduo ajusta sua trajetória com base em experiências próprias e do grupo.

</details>

### Questão 7

No PSO, a atualização da velocidade de uma partícula leva em consideração:

a. O gradiente da função objetivo\
b. A profundidade da árvore sintática\
c. A posição atual, a melhor posição pessoal e a melhor posição global\
d. A mutação binária com probabilidade fixa\
e. A normalização estatística da população

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A velocidade de cada partícula é ajustada com base em sua posição atual, a melhor posição que já visitou e a melhor posição conhecida pelo enxame.

</details>

### Questão 8

O termo de inércia no PSO tem qual função?

a. Reduzir a influência do feromônio\
b. Eliminar flutuações randômicas\
c. Substituir a avaliação da função objetivo\
d. Penalizar partículas com fitness baixo\
e. Controlar a contribuição da velocidade anterior

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** O fator de inércia controla a influência do movimento anterior da partícula, balanceando exploração e exploração.

</details>

### Questão 9

No PSO, uma partícula é composta por:

a. Um vetor de pesos e um valor de elitismo\
b. Um vetor posição, vetor velocidade e histórico de melhores posições\
c. Uma árvore de decisão e um grafo de adjacência\
d. Um gene binário e um operador lógico\
e. Um classificador e um otimizador simbólico

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Cada partícula armazena sua posição atual no espaço de busca, sua velocidade e a melhor posição pessoal visitada.

</details>

### Questão 10

Um problema pode ocorrer no PSO quando as partículas convergem rapidamente para um ponto sem mais exploração. Qual técnica pode mitigar esse problema?

a. Reduzir o tamanho da população\
b. Aumentar a taxa de cruzamento\
c. Ajustar o fator de inércia e introduzir ruído estocástico\
d. Eliminar a melhor posição global da memória\
e. Usar codificação binária para o espaço de busca

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Reduzir a inércia ou adicionar ruído favorece a diversificação das trajetórias, impedindo a estagnação prematura em ótimos locais.

</details>

## Agentes Lógicos

### Questão 1

Inferência lógica consiste em:

a. Derivar conclusões válidas a partir de um conjunto de premissas\
b. Utilizar aprendizado supervisionado para construir hipóteses\
c. Aplicar operadores probabilísticos para gerar soluções\
d. Avaliar a similaridade semântica entre documentos\
e. Transformar proposições em representações numéricas

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** Inferência lógica é o processo de obtenção de novas sentenças que decorrem logicamente de sentenças conhecidas, segundo regras formais.

</details>

### Questão 2

Qual das regras abaixo é uma forma válida de inferência na lógica proposicional?

a. Silogismo circular\
b. Exclusão tautológica\
c. Modus ponens\
d. Inferência probabilística bayesiana\
e. Recursão combinatória

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** O modus ponens afirma que, dadas as proposições "P" e "P implica Q", pode-se inferir logicamente "Q".

</details>

### Questão 3

Seja o conjunto de sentenças:

1. Se está chovendo, então o chão está molhado.
2. Está chovendo.\
   Qual a conclusão obtida por inferência?

a. O chão está seco\
b. O chão está molhado\
c. Está ventando\
d. Não se pode concluir nada\
e. A chuva foi causada pelo chão molhado

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Aplicando o modus ponens, conclui-se que o chão está molhado.

</details>

### Questão 4

A inferência por resolução é usada principalmente em:

a. Lógica de primeira ordem e algoritmos simbólicos\
b. Redes neurais artificiais supervisionadas\
c. Regressão linear multivariada\
d. Algoritmos evolutivos com codificação binária\
e. Algoritmos de agrupamento não supervisionado

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** A

**Justificativa:** A técnica de resolução é um método de inferência completo na lógica de primeira ordem, utilizado para provar teoremas e realizar deduções automatizadas.

</details>

### Questão 5

No contexto de inferência lógica automatizada, o uso de base de conhecimento (KB) é necessário para:

a. Estimar parâmetros desconhecidos\
b. Armazenar as sentenças a partir das quais serão feitas as deduções\
c. Gerar cruzamentos entre proposições genéticas\
d. Executar testes estatísticos sobre as proposições\
e. Traduzir lógica em linguagem natural

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A base de conhecimento contém as sentenças conhecidas (fatos e regras), que são utilizadas como ponto de partida para a inferência lógica.

</details>

### Questão 6

No contexto de agentes lógicos, um agente é dito **racional** quando:

a. Executa sempre a mesma ação para situações iguais\
b. Baseia-se apenas em regras simbólicas fixas\
c. Escolhe ações que maximizam seu desempenho com base no conhecimento disponível\
d. Atua de forma aleatória para evitar padrões\
e. Reage unicamente a estímulos imediatos do ambiente

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** Um agente racional utiliza as percepções e o conhecimento para tomar decisões que maximizem seu desempenho esperado.

</details>

### Questão 6

Em Prolog, qual é a notação correta para uma lista com os elementos 1, 2 e 3?

a. (1, 2, 3)\
b. \[1;2;3]\
c. list(1, 2, 3)\
d. \[1, 2, 3]\
e. {1, 2, 3}

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** A sintaxe padrão de listas em Prolog utiliza colchetes com elementos separados por vírgula, como `[1, 2, 3]`.

</details>

### Questão 7

Considere a seguinte regra Prolog:

```
cabeca([H|_], H).
```

O que ela retorna?

a. O último elemento da lista\
b. O tamanho da lista\
c. O primeiro elemento da lista\
d. A lista sem o primeiro elemento\
e. Uma lista ordenada

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A notação `[H|_]` extrai o primeiro elemento (cabeça) da lista e o unifica com `H`.

</details>

### Questão 8

Qual é o resultado da consulta abaixo, considerando a base:

```
ultimo([X], X).
ultimo([_|T], X) :- ultimo(T, X).
```

Consulta:

```
?- ultimo([1,2,3,4], X).
```

a. X = 1\
b. X = 4\
c. X = 3\
d. X = 2\
e. X = \[4]

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A recursão percorre a lista até restar um único elemento, que é retornado como o último.

</details>

### Questão 9

Dada a seguinte regra:

```
soma([], 0).
soma([H|T], S) :- soma(T, ST), S is H + ST.
```

Qual o resultado da consulta `soma([2,4,6], S).`?

a. S = 6\
b. S = 12\
c. S = 10\
d. S = 2\
e. S = 0

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** A soma é calculada recursivamente: 2 + 4 + 6 = 12.

</details>

### Questão 10

A operação `[H|T]` em Prolog é utilizada para:

a. Unificar dois predicados distintos\
b. Verificar se a lista contém apenas números pares\
c. Decompor uma lista em cabeça e cauda\
d. Combinar duas listas em um vetor\
e. Ordenar uma lista em tempo constante

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A operação `[H|T]` separa o primeiro elemento (H) do restante da lista (T), sendo fundamental para recursão com listas.

</details>

### Questão 11

Prolog é uma linguagem baseada em:

a. Programação imperativa com ponteiros explícitos\
b. Regras de inferência lógica e fatos declarativos\
c. Paradigmas orientados a objeto com herança múltipla\
d. Redes neurais com aprendizado profundo\
e. Algoritmos evolucionários com codificação binária

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Prolog utiliza fatos e regras como base de conhecimento e executa inferência lógica para responder a consultas.

</details>

### Questão 12

Dado o seguinte conjunto de fatos em Prolog:

```
pai(joao, maria).
pai(joao, pedro).
```

Qual consulta retorna verdadeiro?

a. pai(maria, joao).\
b. pai(pedro, joao).\
c. pai(joao, pedro).\
d. pai(pedro, maria).\
e. pai(joao, joao).

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** C

**Justificativa:** A relação está definida com João como pai de Pedro, logo `pai(joao, pedro).` é um fato verdadeiro.

</details>

### Questão 13

Considerando a regra Prolog abaixo:

```
avo(X, Y) :- pai(X, Z), pai(Z, Y).
```

O que ela representa?

a. X é pai de Z ou pai de Y\
b. X é tio de Y\
c. X é filho de Z que é pai de Y\
d. Z é pai de X e Y\
e. X é avô de Y se X é pai de Z e Z é pai de Y

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** E

**Justificativa:** A regra define que X é avô de Y se houver uma relação intermediária Z tal que X é pai de Z e Z é pai de Y.

</details>

### Questão 14

Em Prolog, a inferência é realizada por:

a. Algoritmo MinMax com heurísticas específicas\
b. Busca em profundidade com retrocesso (backtracking)\
c. Rede convolucional com aprendizado supervisionado\
d. Simulação estocástica de eventos lógicos\
e. Caminhamento por grafos acíclicos dirigidos

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** B

**Justificativa:** Prolog utiliza busca em profundidade com backtracking para explorar as regras e fatos da base de conhecimento.

</details>

### Questão 15

Qual das sentenças a seguir é uma **regra** válida em Prolog?

a. pai(maria, joao).\
b. X :- Y.\
c. pai(X, Y) :- mae(X, Y).\
d. pai(X, Y) :- pai(X, Z), mae(Z, Y).\
e. mae(X, Y), pai(Y, Z) :- irmao(X, Z).

<details>

<summary><span data-gb-custom-inline data-tag="emoji" data-code="270f">✏️</span> Solução</summary>

> **Resposta:** D

**Justificativa:** A regra `pai(X, Y) :- pai(X, Z), mae(Z, Y).` define um relacionamento lógico válido entre predicados, com corpo e cabeça corretos.

</details>
