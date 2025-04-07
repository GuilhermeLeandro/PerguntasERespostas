import random
from datetime import datetime

def ordenar_com_randomizacao(perguntas, fator_randomizacao=0.1):
    """
    Ordena as perguntas pela data de revisão com uma leve randomização.

    :param perguntas: Lista de objetos Pergunta.
    :param fator_randomizacao: Quanto maior o fator, mais desordenada será a lista (0.0 a 1.0).
    :return: Lista ordenada e randomizada.
    """
    # Cria um índice baseado na data de revisão
    perguntas_com_peso = [
        (p, datetime.fromisoformat(p.ultima_revisao)) for p in perguntas
    ]

    # Ordena pela data de revisão
    perguntas_com_peso.sort(key=lambda x: x[1])

    # Aplica uma leve randomização
    random.shuffle(perguntas_com_peso)  # Mistura levemente
    perguntas_com_peso = sorted(
        perguntas_com_peso,
        key=lambda x: x[1].timestamp() + random.uniform(0, fator_randomizacao),
    )

    # Retorna apenas as perguntas, agora ordenadas e randomizadas
    return [p[0] for p in perguntas_com_peso]
