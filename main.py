import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainView()
    janela.showMaximized()
    sys.exit(app.exec_())
