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
    
    def __lt__(self, outro):
        """Necessário para uso em fila de prioridade na busca de custo uniforme."""
        return self.custo < outro.custo


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

