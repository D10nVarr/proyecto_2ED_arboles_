import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt


from interfaz import Ui_VentanaPrincipal
from clases_arboles import ArbolABB, ArbolAVL

class AplicacionArboles(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.setWindowTitle("Proyecto 2 - Visualizador de Árboles")

        self.mi_arbol = ArbolABB()

        self.escena = QGraphicsScene()
        self.ui.lienzo_arbol.setScene(self.escena)

        self.ui.BTarbol_abb.clicked.connect(self.cambiar_a_abb)
        self.ui.BTarbol_avl.clicked.connect(self.cambiar_a_avl)

        self.ui.bt_insertar.clicked.connect(self.accion_insertar)
        self.ui.bt_buscar.clicked.connect(self.accion_buscar)
        self.ui.bt_eliminar.clicked.connect(self.accion_eliminar)

    #Circulo de prueba
    def nodo_prueba(self):
        self.escena.clear()

        contorno = QPen(Qt.GlobalColor.black)
        relleno = QBrush(QColor("white"))


        self.escena.addEllipse(0, 0, 40, 40, contorno, relleno)

        texto = self.escena.addText("15")
        texto.setPos(10, 10)

    def cambiar_a_abb(self):
        self.mi_arbol = ArbolABB()
        self.statusBar().showMessage("Árbol ABB (Vacío)")
        print("Cambiado a árbol ABB.")

    def cambiar_a_avl(self):
        self.mi_arbol = ArbolAVL()
        self.statusBar().showMessage("Árbol AVL (Vacío)")
        print("Cambiado a árbol AVL.")

    #Operaciones
    def accion_insertar(self):
        valor_prueba = 15
        self.mi_arbol.insertar(valor_prueba)
        print(f"Insertado {valor_prueba} en la estructura.")
        self.actualizar_informacion_general()

        #Nodo de prueba
        self.nodo_prueba()

    def accion_buscar(self):
        valor_prueba = 15

        encontrado, camino = self.mi_arbol.buscar(valor_prueba)

        print(f"¿Existe el nodo {valor_prueba}?: {encontrado}")
        print(f"Camino seguido en la recursividad: {camino}")

    def accion_eliminar(self):
        valor_prueba = 15
        self.mi_arbol.eliminar(valor_prueba)
        print(f"Eliminado {valor_prueba} de la estructura.")

        self.actualizar_informacion_general()

    #Encabezado con datos del arbol
    def actualizar_informacion_general(self):
        altura = self.mi_arbol.obtener_altura()
        total_nodos = self.mi_arbol.contar_nodos()
        valor_raiz = self.mi_arbol.raiz.valor if self.mi_arbol.raiz else "Vacío"

        info = f"Raíz actual: {valor_raiz}  |  Altura total: {altura}  |  Cantidad de nodos: {total_nodos}"
        self.statusBar().showMessage(info)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = AplicacionArboles()
    ventana.show()
    sys.exit(app.exec())
