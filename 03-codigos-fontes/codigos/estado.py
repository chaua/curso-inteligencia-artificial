from copy import deepcopy

# Classe que representa um estado do problema.
class Estado:
    def __init__(self, vetor = [], custo = 0, acao = None, pai = None):
        """
        Construtor da classe Estado.
        :param vetor: representação do estado (ex: lista de números, posições etc.)
        :param custo: custo acumulado até chegar neste estado
        :param acao: ação que foi tomada para chegar a este estado
        :param pai: estado anterior (utilizado para reconstruir o caminho da solução)
        """
        self.vetor = vetor
        self.custo = custo
        self.acao = acao
        self.pai = pai

    def __getitem__(self, i):
        """Permite acessar os elementos do vetor diretamente pelo índice."""
        return self.vetor[i]

    def __eq__(self, outro):
        """Define igualdade entre estados com base no vetor de representação."""
        return self.vetor == outro.vetor


# Classe abstrata que representa um problema de busca genérico.
class Problema:

    @property
    def estado_inicial(self):
        """
        Deve ser sobrescrita na subclasse para retornar o estado inicial do problema.
        Ex: o estado inicial de um quebra-cabeça ou labirinto.
        """
        # return Estado()

    def estado_objetivo(self, estado):
        """
        Deve ser sobrescrita para definir a condição de parada.
        Verifica se o estado atual é o estado objetivo.
        """
        # objetivo = Estado()
        # return estado == objetivo

    def solucao(self, estado):
        """
        Reconstrói o caminho desde o estado inicial até o estado objetivo.
        A partir do estado final, percorre os 'pais' até o início.
        """
        resultado = []
        ptr = estado

        # Enquanto houver um pai (ou seja, ainda não chegou ao estado inicial)
        while not ptr.pai:
            resultado.append(ptr)
            ptr = ptr.pai

        # Inverte a lista para que a solução vá do início ao fim
        return resultado.reverse()

    def funcao_sucessora(self, estado):
        """
        Função responsável por gerar os estados vizinhos (sucessores) a partir do estado atual.
        Deve ser sobrescrita para aplicar todas as ações válidas sobre o estado.
        """
        vizinhos = []

        # Exemplo genérico:
        # para cada ação válida no estado:
        #   novo_estado = resultado da aplicação da ação
        #   vizinhos.append(novo_estado)

        return vizinhos


# Função que implementa a busca em largura (Breadth-First Search - BFS)
def busca(problema: Problema):
    """
    Agente de busca que resolve um problema aplicando a estratégia de busca em largura (BFS).
    Esta estratégia explora primeiro os estados mais superficiais (mais próximos da raiz).
    """

    # 1. Inicializa a borda (fringe) com o estado inicial
    borda = [problema.estado_inicial]

    # Lista de memória usada para armazenar os estados já visitados
    memoria = [problema.estado_inicial]

    while True:

        # 2. Se a borda estiver vazia, significa que todos os estados foram explorados e não houve solução
        if not borda:
            raise RuntimeError('Falha ao encontrar solucao')

        # 3. Remove o próximo estado da borda (FIFO = fila = busca em largura)
        estado = borda.pop(0)

        # 4. Verifica se este é o estado objetivo
        if problema.estado_objetivo(estado):
            return problema.solucao(estado)

        # 5. Aplica a função de transição para gerar os estados vizinhos
        vizinhos = problema.funcao_sucessora(estado)

        # 6. Para cada vizinho, verifica se já foi visitado
        for vizinho in vizinhos:
            if vizinho not in memoria:
                borda.append(vizinho)       # Adiciona ao final da fila
                memoria.append(vizinho)     # Marca como visitado

