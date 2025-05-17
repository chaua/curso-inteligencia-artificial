def busca_largura(problema: Problema) -> List[Estado]:
    """
    Estratégia de busca em largura (FIFO).
    Explora primeiro os nós mais rasos.
    """
    borda = [problema.estado_inicial]
    memoria = set()
    memoria.add(problema.estado_inicial)

    while borda:
        estado = borda.pop(0)

        if problema.estado_objetivo(estado):
            return problema.solucao(estado)

        for vizinho in problema.funcao_sucessora(estado):
            if vizinho not in memoria:
                borda.append(vizinho)
                memoria.add(vizinho)

    raise RuntimeError("Nenhuma solução encontrada.")

