from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QTextEdit,
    QLineEdit, QPushButton, QMessageBox, QFrame
)
from PyQt5.QtCore import Qt
from utils.storage import Storage
from utils.random_sort import ordenar_com_randomizacao

class ReviewView(QMainWindow):
    def __init__(self, main_view):
        super().__init__()
        self.main_view = main_view
        self.setWindowTitle("Revisão de Perguntas")
        self.setGeometry(100, 100, 1200, 800)

        self.storage = Storage()
        self.perguntas_para_revisar = ordenar_com_randomizacao(self.storage.carregar_perguntas(), fator_randomizacao=0.2)


        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setSpacing(20)

        # Título
        titulo = QLabel("Revisão de Perguntas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("""
            font-size: 28px; font-weight: bold; color: #333;
            margin-bottom: 20px; padding: 10px; background-color: #f2f2f2;
            border: 2px solid #ccc; border-radius: 8px;
        """)
        self.layout.addWidget(titulo)

        # Área de exibição da pergunta
        pergunta_frame = QFrame()
        pergunta_layout = QVBoxLayout()
        pergunta_layout.setContentsMargins(10, 10, 10, 10)
        pergunta_layout.setSpacing(5)  # Reduz o espaçamento geral entre os elementos do layout

        # Adicionando o rótulo acima do campo de texto
        self.label_pergunta = QLabel("Pergunta:")
        self.label_pergunta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444; margin-bottom: 2px;")
        pergunta_layout.addWidget(self.label_pergunta)  # Adiciona o rótulo no layout

        self.input_pergunta = QTextEdit()
        self.input_pergunta.setReadOnly(True)
        self.input_pergunta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #f9f9f9;
            border: 1px solid #ccc; border-radius: 5px; padding: 10px;
            margin-top: 0px;  /* Remove qualquer margem superior */
        """)
        pergunta_layout.addWidget(self.input_pergunta)  # Adiciona o campo de entrada no layout

        pergunta_frame.setLayout(pergunta_layout)
        self.layout.addWidget(pergunta_frame)

        # Área de entrada de resposta
        resposta_frame = QFrame()
        resposta_layout = QVBoxLayout()
        resposta_layout.setContentsMargins(10, 10, 10, 10)
        resposta_layout.setSpacing(10)

        self.label_resposta = QLabel("Sua Resposta:")
        self.label_resposta.setStyleSheet("font-size: 18px; font-weight: bold; color: #444; margin-bottom: 5px;")
        resposta_layout.addWidget(self.label_resposta)

        self.input_resposta = QLineEdit()
        self.input_resposta.setStyleSheet("""
            font-size: 16px; color: #333; background-color: #fff;
            border: 1px solid #ccc; border-radius: 5px; padding: 8px;
        """)
        self.input_resposta.setPlaceholderText("Digite sua resposta aqui...")
        resposta_layout.addWidget(self.input_resposta)

        resposta_frame.setLayout(resposta_layout)
        self.layout.addWidget(resposta_frame)

        # Botões
        botoes_layout = QHBoxLayout()
        botoes_layout.setSpacing(20)

        self.botao_voltar = QPushButton("Voltar")
        self.botao_voltar.setStyleSheet("""
            font-size: 16px; padding: 10px 20px; background-color: #d9534f;
            color: white; border: none; border-radius: 5px;
        """)
        self.botao_voltar.clicked.connect(self.voltar_main)
        botoes_layout.addWidget(self.botao_voltar)

        self.botao_enviar = QPushButton("Enviar Resposta")
        self.botao_enviar.setStyleSheet("""
            font-size: 16px; padding: 10px 20px; background-color: #0275d8;
            color: white; border: none; border-radius: 5px;
        """)
        self.botao_enviar.clicked.connect(self.enviar_resposta)
        botoes_layout.addWidget(self.botao_enviar)

        self.layout.addLayout(botoes_layout)

        # Configuração do layout principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.pergunta_atual = 0
        self.carregar_pergunta()

    def voltar_main(self):
        self.close()
        self.main_view.show()

    def carregar_pergunta(self):
        if self.pergunta_atual < len(self.perguntas_para_revisar):
            pergunta = self.perguntas_para_revisar[self.pergunta_atual]
            self.input_pergunta.setPlainText(pergunta.pergunta)
            self.input_resposta.clear()
        else:
            QMessageBox.information(self, "Revisão Completa", "Todas as perguntas foram revisadas!")
            self.voltar_main()

    def enviar_resposta(self):
        resposta_usuario = self.input_resposta.text().strip()
        if not resposta_usuario:
            QMessageBox.warning(self, "Erro", "Por favor, insira sua resposta!")
            return

        pergunta_atual = self.perguntas_para_revisar[self.pergunta_atual]
        resposta_correta = pergunta_atual.resposta

        resposta = QMessageBox(self)
        resposta.setIcon(QMessageBox.Question)
        resposta.setWindowTitle("Confirmação de Resposta")

        # Definindo o texto da mensagem
        resposta.setText(
            f"<p style='font-size: 14px; width: 600px;'>"
            f"Você respondeu: <b>{resposta_usuario}</b><br><br>"
            f"A resposta correta é: <b>{resposta_correta}</b><br><br>"
            f"<b>Explicação:</b> {pergunta_atual.explicacao}<br><br>"
            f"Você acertou?"
            f"</p>"
        )

        # Configurando os botões
        resposta.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resposta.button(QMessageBox.Yes).setText("Sim")
        resposta.button(QMessageBox.No).setText("Não")

        # Ajustando a largura
        resposta.setStyleSheet("""
            QMessageBox {
                min-width: 600px;
                font-size: 14px;
            }
        """)

        # Exibe a mensagem e captura a resposta
        user_response = resposta.exec_()

        if user_response == QMessageBox.Yes:
            pergunta_atual.atualizar_revisao()  # Atualiza a data da última revisão
            self.storage.salvar_perguntas(self.perguntas_para_revisar)  # Salva as alterações no arquivo
        else:
            QMessageBox.warning(self, "Continue Estudando", "Não desista! Continue revisando.")

        self.pergunta_atual += 1
        self.carregar_pergunta()

    def exibir_resposta_correta(self, resposta_correta, explicacao):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Resposta Correta")

        texto = f"""
            <p style='text-align: center; font-size: 16px;'>
                <b>Resposta Correta:</b><br><br>
                {resposta_correta}<br><br>
                <b>Explicação:</b><br><br>
                {explicacao if explicacao else "Nenhuma explicação fornecida."}
            </p>
        """
        msg_box.setText(texto)

        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.button(QMessageBox.Ok).setText("Continuar")
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #f9f9f9;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QPushButton {
                font-size: 14px; padding: 8px 16px;
            }
        """)

        msg_box.exec_()

