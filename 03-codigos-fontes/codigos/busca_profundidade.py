def busca_profundidade(problema: Problema) -> List[Estado]:
    """
    Estratégia de busca em profundidade (LIFO).
    Explora primeiro os caminhos mais profundos.
    """
    borda = [problema.estado_inicial]
    memoria = set()
    memoria.add(problema.estado_inicial)

    while borda:
        estado = borda.pop()  # LIFO: último inserido

        if problema.estado_objetivo(estado):
            return problema.solucao(estado)

        for vizinho in problema.funcao_sucessora(estado):
            if vizinho not in memoria:
                borda.append(vizinho)
                memoria.add(vizinho)

    raise RuntimeError("Nenhuma solução encontrada.")

