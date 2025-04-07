from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QListWidget, QPushButton,
    QHBoxLayout, QTextEdit, QLineEdit, QMessageBox, QLabel
)
from PyQt5.QtCore import Qt
from utils.storage import Storage
from models.perguntas import Pergunta


class EditView(QMainWindow):
    def __init__(self, main_view):
        super().__init__()
        self.main_view = main_view
        self.setWindowTitle("Editar Perguntas")
        self.setGeometry(100, 100, 1200, 800)

        self.storage = Storage()
        self.perguntas = self.storage.carregar_perguntas()

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(20)

        # Título
        titulo = QLabel("Editar Perguntas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 28px; font-weight: bold; color: #333;
            margin-bottom: 20px; padding: 10px; background-color: #f7f7f7;
            border: 2px solid #ddd; border-radius: 8px;
        """)
        self.layout.addWidget(titulo)

        # Lista de perguntas
        self.lista_perguntas = QListWidget()
        self.lista_perguntas.addItems([p.pergunta for p in self.perguntas])
        self.lista_perguntas.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #f9f9f9;
            border: 1px solid #ccc; border-radius: 5px; padding: 5px;
        """)
        self.lista_perguntas.currentRowChanged.connect(self.carregar_pergunta)
        self.layout.addWidget(self.lista_perguntas, stretch=1)

        # Área de edição
        form_layout = QVBoxLayout()
        form_layout.setSpacing(15)

        self.label_pergunta = QLabel("Pergunta:")
        self.label_pergunta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444;")
        form_layout.addWidget(self.label_pergunta)

        self.input_pergunta = QTextEdit()
        self.input_pergunta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        form_layout.addWidget(self.input_pergunta)

        self.label_resposta = QLabel("Resposta:")
        self.label_resposta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444;")
        form_layout.addWidget(self.label_resposta)

        self.input_resposta = QLineEdit()
        self.input_resposta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        form_layout.addWidget(self.input_resposta)

        self.label_explicacao = QLabel("Explicação:")
        self.label_explicacao.setStyleSheet("font-size: 18px; font-weight: bold; color: #444;")
        form_layout.addWidget(self.label_explicacao)

        self.input_explicacao = QTextEdit()
        self.input_explicacao.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        form_layout.addWidget(self.input_explicacao)

        self.layout.addLayout(form_layout, stretch=2)

        # Botões
        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(20)

        self.botao_salvar = QPushButton("Salvar Alterações")
        self.botao_salvar.setStyleSheet("""
            font-size: 16px; padding: 10px 20px; background-color: #5cb85c;
            color: white; border: none; border-radius: 5px;
        """)
        self.botao_salvar.clicked.connect(self.salvar_alteracoes)
        botoes_layout.addWidget(self.botao_salvar)

        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.setStyleSheet("""
            font-size: 16px; padding: 10px 20px; background-color: #d9534f;
            color: white; border: none; border-radius: 5px;
        """)
        self.botao_voltar.clicked.connect(self.voltar_main)
        botoes_layout.addWidget(self.botao_voltar)

        self.layout.addLayout(botoes_layout)

        # Configuração do layout principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Carregar a primeira pergunta
        self.carregar_pergunta(0)

    def carregar_pergunta(self, index):
        if 0 <= index < len(self.perguntas):
            pergunta = self.perguntas[index]
            self.input_pergunta.setPlainText(pergunta.pergunta)
            self.input_resposta.setText(pergunta.resposta)
            self.input_explicacao.setPlainText(pergunta.explicacao)
        else:
            self.input_pergunta.clear()
            self.input_resposta.clear()
            self.input_explicacao.clear()

    def salvar_alteracoes(self):
        index = self.lista_perguntas.currentRow()
        if index >= 0:
            self.perguntas[index].pergunta = self.input_pergunta.toPlainText().strip()
            self.perguntas[index].resposta = self.input_resposta.text().strip()
            self.perguntas[index].explicacao = self.input_explicacao.toPlainText().strip()

            self.storage.salvar_perguntas(self.perguntas)
            self.lista_perguntas.clear()
            self.lista_perguntas.addItems([p.pergunta for p in self.perguntas])
            QMessageBox.information(self, "Sucesso", "Pergunta atualizada com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Selecione uma pergunta para editar!")

    def voltar_main(self):
        self.close()
        self.main_view.show()
