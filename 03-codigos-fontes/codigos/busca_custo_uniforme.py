def busca_custo_uniforme(problema: Problema) -> List[Estado]:
    """
    Estratégia de busca de custo uniforme.
    Utiliza fila de prioridade baseada no custo acumulado.
    """
    fronteira = []
    heapq.heappush(fronteira, (problema.estado_inicial.custo, problema.estado_inicial))
    memoria = set()
    memoria.add(problema.estado_inicial)

    while fronteira:
        _, estado = heapq.heappop(fronteira)

        if problema.estado_objetivo(estado):
            return problema.solucao(estado)

        for vizinho in problema.funcao_sucessora(estado):
            if vizinho not in memoria:
                heapq.heappush(fronteira, (vizinho.custo, vizinho))
                memoria.add(vizinho)

    raise RuntimeError("Nenhuma solução encontrada.")

