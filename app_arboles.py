import sys
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtCore import Qt, QTimer



from interfaz import Ui_VentanaPrincipal
from clases_arboles import ArbolABB, ArbolAVL, ArbolBIN

class AplicacionArboles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.setWindowTitle("Proyecto 2 - Visualizador de Árboles")

        self.mi_arbol = ArbolABB()

        self.escena = QGraphicsScene()
        self.ui.lienzo_arbol.setScene(self.escena)

        self.ui.BTarbol_bin.clicked.connect(self.cambiar_a_bin)#Conección del boton de cambio de arbol binario
        self.ui.BTarbol_abb.clicked.connect(self.cambiar_a_abb)
        self.ui.BTarbol_avl.clicked.connect(self.cambiar_a_avl)
        self.ui.bt_insertar.clicked.connect(self.accion_insertar)
        self.ui.bt_buscar.clicked.connect(self.accion_buscar)
        self.ui.bt_eliminar.clicked.connect(self.accion_eliminar)

        self.ui.accion_guardar.triggered.connect(self.accion_guardar)
        self.ui.accion_cargar.triggered.connect(self.accion_cargar)

        self.ui.bt_preo.clicked.connect(self.accion_preorden)
        self.ui.bt_ino.clicked.connect(self.accion_inorden)
        self.ui.bt_posto.clicked.connect(self.accion_postorden)

        self.timer_animacion = QTimer()
        self.timer_animacion.timeout.connect(self.paso_animacion)
        self.lista_animacion = []
        self.indice_animacion = 0

        # Control de interfaz (Botones apagados)

        self.controles_bloqueados = [
            self.ui.bt_insertar, self.ui.bt_buscar, self.ui.bt_eliminar,
            self.ui.bt_preo, self.ui.bt_ino, self.ui.bt_posto,
            self.ui.entrada_nodo, self.ui.accion_guardar
        ]

        for control in self.controles_bloqueados:
            control.setEnabled(False)

        self.ui.p_recorridos.setText("Por favor, seleccione el tipo de árbol (ABB o AVL) para comenzar.")

    # Motor de animación
    def iniciar_animacion(self, lista_nodos):
        self.lista_animacion = lista_nodos
        self.indice_animacion = 0

        self.dibujar_arbol(camino_resaltado=[])

        self.timer_animacion.start(700)

    def paso_animacion(self):

        if self.indice_animacion < len(self.lista_animacion):

            nodos_a_pintar = self.lista_animacion[:self.indice_animacion + 1]

            self.dibujar_arbol(camino_resaltado=nodos_a_pintar)

            self.indice_animacion += 1
        else:

            self.timer_animacion.stop()

        # Guardado con (JSON)
    def accion_guardar(self):

        if self.mi_arbol is None or self.mi_arbol.raiz is None:
            self.statusBar().showMessage("Error: El árbol está vacío, no hay nada que guardar.")
            return

        ruta_archivo, _ = QFileDialog.getSaveFileName(self, "Guardar Árbol", "", "JSON Files (*.json)")

        if ruta_archivo:

            if isinstance(self.mi_arbol, ArbolAVL):
                tipo = "AVL"
                nodos_guardar = self.mi_arbol.preorden()

            elif isinstance(self.mi_arbol, ArbolBIN):
                tipo = "BIN"
                nodos_guardar = []
                cola = [self.mi_arbol.raiz]
                while len(cola) > 0:
                    actual = cola.pop(0)
                    nodos_guardar.append(actual.valor)
                    if actual.izq is not None: cola.append(actual.izq)
                    if actual.der is not None: cola.append(actual.der)

            else:
                tipo = "ABB"
                nodos_guardar = self.mi_arbol.preorden()

            datos_a_guardar = {
                "tipo_arbol": tipo,
                "nodos": nodos_guardar
            }

            with open(ruta_archivo, 'w') as archivo:
                json.dump(datos_a_guardar, archivo, indent=4)

            self.statusBar().showMessage(f"Árbol guardado exitosamente en: {ruta_archivo}")

    def accion_cargar(self):
        ruta_archivo, _ = QFileDialog.getOpenFileName(self, "Cargar Árbol", "", "JSON Files (*.json)")

        if ruta_archivo:
            with open(ruta_archivo, 'r') as archivo:
                datos_cargados = json.load(archivo)

            tipo = datos_cargados["tipo_arbol"]

            if tipo == "AVL":
                self.mi_arbol = ArbolAVL()
                self.statusBar().showMessage("Árbol AVL cargado desde archivo.")

            #Caso especial de cargado para el arbol binario
            elif tipo == "BIN":
                self.mi_arbol = ArbolBIN()
                self.statusBar().showMessage("Árbol BIN cargado desde archivo.")
            else:
                self.mi_arbol = ArbolABB()
                self.statusBar().showMessage("Árbol ABB cargado desde archivo.")

            for valor in datos_cargados["nodos"]:
                self.mi_arbol.insertar(valor)

            for control in self.controles_bloqueados:
                control.setEnabled(True)


            if tipo == "BIN":
                self.ui.bt_buscar.setEnabled(False)
                self.ui.bt_eliminar.setEnabled(False)

            self.ui.p_recorridos.setText(f"Estructura cargada con {len(datos_cargados['nodos'])} nodos.")

            self.actualizar_informacion_general()
            self.dibujar_arbol()

    def dibujar_arbol(self, camino_resaltado=None):
        if camino_resaltado is None:
            camino_resaltado = []

        self.escena.clear()
        if self.mi_arbol.raiz is not None:
            self._dibujar_nodo_recursivo(self.mi_arbol.raiz, 0, -150, 120, camino_resaltado)

    def _dibujar_nodo_recursivo(self, nodo, x, y, espacio_x, camino_resaltado):
        #Lineas de union
        contorno_linea= QPen(Qt.GlobalColor.black)
        contorno_linea.setWidth(2)

        relleno_circulo = QBrush(QColor("white"))

        if nodo.valor in camino_resaltado:
            contorno_circulo = QPen(QColor("orange"))
            contorno_circulo.setWidth(3)
        else:
            contorno_circulo = QPen(Qt.GlobalColor.black)
            contorno_circulo.setWidth(3)

        #Lineas a hijos
        distancia_y = 60

        if nodo.izq is not None:
            # Línea izquierda
            self.escena.addLine(x, y, x - espacio_x, y + distancia_y, contorno_linea)
            self._dibujar_nodo_recursivo(nodo.izq, x - espacio_x, y + distancia_y, espacio_x / 1.8, camino_resaltado)

        if nodo.der is not None:
            # Línea derecha
            self.escena.addLine(x, y, x + espacio_x, y + distancia_y, contorno_linea)
            self._dibujar_nodo_recursivo(nodo.der, x + espacio_x, y + distancia_y, espacio_x / 1.8, camino_resaltado)

        #Circulo del nodo
        radio = 18
        self.escena.addEllipse(x - radio, y - radio, radio * 2, radio * 2, contorno_circulo, relleno_circulo)

        texto = self.escena.addText(str(nodo.valor))

        ancho_texto = texto.boundingRect().width()
        alto_texto = texto.boundingRect().height()
        texto.setPos(x - (ancho_texto / 2), y - (alto_texto / 2))


    def cambiar_a_bin(self):
        self.mi_arbol=ArbolBIN()
        self.statusBar().showMessage("Árbol BIN (Vacío)")

        for control in self.controles_bloqueados:
            control.setEnabled(True)
        self.ui.bt_buscar.setEnabled(False)
        self.ui.bt_eliminar.setEnabled(False)

        self.ui.p_recorridos.setText("Árbol Binario listo.")
        self.dibujar_arbol()


    def cambiar_a_abb(self):
        self.mi_arbol = ArbolABB()
        self.statusBar().showMessage("Árbol ABB (Vacío)")

        for control in self.controles_bloqueados:
            control.setEnabled(True)
        self.ui.p_recorridos.setText("Árbol Binario de Búsqueda listo.")
        self.dibujar_arbol()

    def cambiar_a_avl(self):
        self.mi_arbol = ArbolAVL()
        self.statusBar().showMessage("Árbol AVL (Vacío)")

        for control in self.controles_bloqueados:
            control.setEnabled(True)
        self.ui.p_recorridos.setText("Árbol AVL listo.")
        self.dibujar_arbol()

    #Operaciones
    def accion_insertar(self):
        valor_a_insertar = self.ui.entrada_nodo.value()

        #Insertar
        self.mi_arbol.insertar(valor_a_insertar)
        print(f"Insertado {valor_a_insertar}")

        #Actualizar
        self.actualizar_informacion_general()
        self.dibujar_arbol()

    def accion_buscar(self):
        valor_a_buscar = self.ui.entrada_nodo.value()
        encontrado, camino = self.mi_arbol.buscar(valor_a_buscar)

        if encontrado:
            self.ui.p_recorridos.setText(f"Éxito: El nodo {valor_a_buscar} existe. Camino: {camino}")
        else:
            self.ui.p_recorridos.setText(f"Fallo: El nodo {valor_a_buscar} NO existe. Camino recorrido: {camino}")

        self.dibujar_arbol(camino_resaltado=camino)

    def accion_eliminar(self):
        valor_a_eliminar = self.ui.entrada_nodo.value()

        self.mi_arbol.eliminar(valor_a_eliminar)
        print(f"Eliminado {valor_a_eliminar} de la estructura.")


        self.actualizar_informacion_general()
        self.dibujar_arbol()

    #Recorridos
    def accion_preorden(self):
        lista_preorden = self.mi_arbol.preorden()
        texto = " -> ".join(map(str, lista_preorden))
        self.ui.p_recorridos.setText(f"Recorrido Pre-Orden:\n{texto}")
        self.iniciar_animacion(lista_preorden)

    def accion_inorden(self):
        lista_inorden = self.mi_arbol.inorden()
        texto = " -> ".join(map(str, lista_inorden))
        self.ui.p_recorridos.setText(f"Recorrido In-Orden:\n{texto}")

        self.iniciar_animacion(lista_inorden)

    def accion_postorden(self):
        lista_postorden = self.mi_arbol.postorden()
        texto = " -> ".join(map(str, lista_postorden))
        self.ui.p_recorridos.setText(f"Recorrido Post-Orden:\n{texto}")

        self.iniciar_animacion(lista_postorden)

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