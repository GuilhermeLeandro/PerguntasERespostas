from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit,
    QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import Qt
from utils.storage import Storage
from models.perguntas import Pergunta
from views.review_view import ReviewView

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Perguntas - Revisão")
        self.setGeometry(100, 100, 1200, 800)

        # Gerenciamento de dados
        self.storage = Storage()
        self.perguntas = self.storage.carregar_perguntas()

        # Layout principal
        self.layout = QVBoxLayout()

        # Título
        titulo = QLabel("Gerenciador de Perguntas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
                    font-size: 28px; font-weight: bold; color: #333;
                    margin-bottom: 20px; padding: 10px; background-color: #f2f2f2;
                    border: 2px solid #ccc; border-radius: 8px;
                """)
        self.layout.addWidget(titulo)

        # Campos gerais
        self.label_pergunta = QLabel("Pergunta:")
        self.label_pergunta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444; margin-bottom: 2px;")
        self.input_pergunta = QTextEdit()
        self.input_pergunta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        self.input_pergunta.setPlaceholderText("Digite a pergunta aqui...")
        self.input_pergunta.setFixedHeight(250)
        self.label_resposta = QLabel("Resposta:")
        self.label_resposta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444; margin-bottom: 2px;")
        self.input_resposta = QLineEdit()
        self.input_resposta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        self.input_resposta.setPlaceholderText("Digite a resposta aqui...")
        self.label_explicacao = QLabel("Explicação da resposta:")
        self.label_explicacao.setStyleSheet("font-size: 18px; font-weight: bold; color: #444; margin-bottom: 2px;")
        self.input_explicacao = QTextEdit()
        self.input_explicacao.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        self.input_explicacao.setPlaceholderText("Explique o motivo da resposta, se necessário...")
        self.layout.addWidget(self.label_pergunta)
        self.layout.addWidget(self.input_pergunta)
        self.layout.addWidget(self.label_resposta)
        self.layout.addWidget(self.input_resposta)
        self.layout.addWidget(self.label_explicacao)
        self.layout.addWidget(self.input_explicacao)

        # Botões
        self.botao_cadastrar = QPushButton("Cadastrar Pergunta")
        self.botao_cadastrar.setStyleSheet("""
            font-size: 14px; padding: 10px; background-color: #5cb85c; color: white;
            border: none; border-radius: 5px;
        """)
        self.botao_cadastrar.clicked.connect(self.cadastrar_pergunta)
        self.layout.addWidget(self.botao_cadastrar)

        self.botao_editar = QPushButton("Editar Perguntas")
        self.botao_editar.setStyleSheet("""
            font-size: 14px; padding: 10px; background-color: #f0ad4e; color: white;
            border: none; border-radius: 5px;
        """)
        self.botao_editar.clicked.connect(self.abrir_edicao)
        self.layout.addWidget(self.botao_editar)

        self.botao_revisao = QPushButton("Entrar na Revisão")
        self.botao_revisao.setStyleSheet("""
            font-size: 14px; padding: 10px; background-color: #0275d8; color: white;
            border: none; border-radius: 5px;
        """)
        self.botao_revisao.clicked.connect(self.abrir_revisao)
        self.layout.addWidget(self.botao_revisao)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def cadastrar_pergunta(self):
        pergunta_texto = self.input_pergunta.toPlainText().strip()
        resposta_texto = self.input_resposta.text().strip()
        explicacao_texto = self.input_explicacao.toPlainText().strip()

        if not pergunta_texto or not resposta_texto:
            QMessageBox.warning(self, "Erro", "Os campos de pergunta e resposta são obrigatórios!")
            return

        # Verificar duplicidade
        if any(p.pergunta == pergunta_texto for p in self.perguntas):
            QMessageBox.warning(self, "Erro", "Essa pergunta já foi cadastrada!")
            return

        nova_pergunta = Pergunta(pergunta=pergunta_texto, resposta=resposta_texto, explicacao=explicacao_texto)
        self.perguntas.append(nova_pergunta)
        self.storage.salvar_perguntas(self.perguntas)

        QMessageBox.information(self, "Sucesso", "Pergunta cadastrada com sucesso!")

        self.input_pergunta.clear()
        self.input_resposta.clear()
        self.input_explicacao.clear()

    def abrir_revisao(self):
        self.revisao_view = ReviewView(self)
        self.revisao_view.showMaximized()
        self.close()

    def abrir_edicao(self):
        from views.edit_view import EditView
        self.edit_view = EditView(self)
        self.edit_view.showMaximized()
        self.close()

