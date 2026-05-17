import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from interfaz import Ui_VentanaPrincipal


class AplicacionArboles(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.setWindowTitle("Proyecto 2 - Visualizador de Árboles")

        self.ui.bt_insertar.clicked.connect(self.accion_insertar)

    def accion_insertar(self):
        print("Acción instertar pendiente de conectar")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = AplicacionArboles()
    ventana.show()

    sys.exit(app.exec())
