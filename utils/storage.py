import json
from models.perguntas import Pergunta  # Corrigido o caminho do import

class Storage:
    def __init__(self, arquivo="perguntas.json"):
        self.arquivo = arquivo

    def carregar_perguntas(self):
        try:
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                return [Pergunta.from_dict(p) for p in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON. Verifique se ele está corrompido.")
            return []

    def salvar_perguntas(self, perguntas):
        try:
            with open(self.arquivo, "w") as f:
                json.dump([p.to_dict() for p in perguntas], f, indent=4)
        except IOError as e:
            print(f"Erro ao salvar o arquivo: {e}")
