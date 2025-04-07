from datetime import datetime

class Pergunta:
    def __init__(self, pergunta, resposta, explicacao=None, ultima_revisao=None):
        self.pergunta = pergunta
        self.resposta = resposta
        self.explicacao = explicacao or ""
        self.ultima_revisao = ultima_revisao or datetime.now().isoformat()

    def precisa_revisao(self, dias=2):
        if not self.ultima_revisao:
            return True
        ultima_revisao_data = datetime.fromisoformat(self.ultima_revisao)
        return (datetime.now() - ultima_revisao_data).days > dias

    def atualizar_revisao(self):
        self.ultima_revisao = datetime.now().isoformat()

    def to_dict(self):
        return {
            "pergunta": self.pergunta,
            "resposta": self.resposta,
            "explicacao": self.explicacao,
            "ultima_revisao": self.ultima_revisao,
        }

    @staticmethod
    def from_dict(data):
        return Pergunta(
            pergunta=data["pergunta"],
            resposta=data["resposta"],
            explicacao=data.get("explicacao", ""),
            ultima_revisao=data.get("ultima_revisao"),
        )
