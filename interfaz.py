# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QHBoxLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(757, 506)
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(129, 419))
        self.frame.setMaximumSize(QSize(129, 419))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 111, 121))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.BTarbol_bin = QPushButton(self.groupBox)
        self.BTarbol_bin.setObjectName(u"BTarbol_bin")
        self.BTarbol_bin.setGeometry(QRect(10, 20, 91, 26))
        self.BTarbol_bin.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.BTarbol_bin.setAutoRepeatInterval(104)
        self.BTarbol_abb = QPushButton(self.groupBox)
        self.BTarbol_abb.setObjectName(u"BTarbol_abb")
        self.BTarbol_abb.setGeometry(QRect(10, 50, 91, 26))
        self.BTarbol_avl = QPushButton(self.groupBox)
        self.BTarbol_avl.setObjectName(u"BTarbol_avl")
        self.BTarbol_avl.setGeometry(QRect(10, 80, 91, 26))
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 150, 111, 121))
        self.bt_insertar = QPushButton(self.groupBox_2)
        self.bt_insertar.setObjectName(u"bt_insertar")
        self.bt_insertar.setGeometry(QRect(10, 20, 81, 26))
        self.bt_buscar = QPushButton(self.groupBox_2)
        self.bt_buscar.setObjectName(u"bt_buscar")
        self.bt_buscar.setGeometry(QRect(10, 50, 81, 26))
        self.byeliminar = QPushButton(self.groupBox_2)
        self.byeliminar.setObjectName(u"byeliminar")
        self.byeliminar.setGeometry(QRect(10, 80, 81, 26))
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 290, 111, 111))
        self.bt_ino = QPushButton(self.groupBox_3)
        self.bt_ino.setObjectName(u"bt_ino")
        self.bt_ino.setGeometry(QRect(10, 20, 81, 26))
        self.bt_preo = QPushButton(self.groupBox_3)
        self.bt_preo.setObjectName(u"bt_preo")
        self.bt_preo.setGeometry(QRect(10, 50, 81, 26))
        self.bt_posto = QPushButton(self.groupBox_3)
        self.bt_posto.setObjectName(u"bt_posto")
        self.bt_posto.setGeometry(QRect(10, 80, 81, 26))

        self.horizontalLayout.addWidget(self.frame)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 757, 33))
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Tipos de \u00e1rboles", None))
        self.BTarbol_bin.setText(QCoreApplication.translate("VentanaPrincipal", u"Arbol Binario", None))
        self.BTarbol_abb.setText(QCoreApplication.translate("VentanaPrincipal", u"Arbol ABB", None))
        self.BTarbol_avl.setText(QCoreApplication.translate("VentanaPrincipal", u"Arbol AVL", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Operaciones", None))
        self.bt_insertar.setText(QCoreApplication.translate("VentanaPrincipal", u"Insertar", None))
        self.bt_buscar.setText(QCoreApplication.translate("VentanaPrincipal", u"Buscar", None))
        self.byeliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("VentanaPrincipal", u"Recorridos", None))
        self.bt_ino.setText(QCoreApplication.translate("VentanaPrincipal", u"In-Orden", None))
        self.bt_preo.setText(QCoreApplication.translate("VentanaPrincipal", u"Pre-Orden", None))
        self.bt_posto.setText(QCoreApplication.translate("VentanaPrincipal", u"Post-Orden", None))
    # retranslateUi

