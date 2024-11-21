from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Crear un layout principal para la ventana central
        main_layout = QtWidgets.QHBoxLayout(self.centralwidget)

        # Crear un layout para la parte izquierda
        left_layout = QtWidgets.QVBoxLayout()

        # Etiqueta "Matriz de Pesos >>"
        self.lblTtitulo_3 = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo_3.setStyleSheet("font: 70 14pt \"MS Shell Dlg 2\";\n"
                                        "color:rgb(0, 85, 255);")
        self.lblTtitulo_3.setObjectName("lblTtitulo_3")
        left_layout.addWidget(self.lblTtitulo_3)

        # Tabla para la matriz de pesos
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        left_layout.addWidget(self.tableWidget)

        # Botones para generar los grafos
        self.btnPintarGrafo = QtWidgets.QPushButton(self.centralwidget)
        self.btnPintarGrafo.setObjectName("btnPintarGrafo")
        left_layout.addWidget(self.btnPintarGrafo)

        self.btnGenerarK2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarK2.setObjectName("btnGenerarK2")
        left_layout.addWidget(self.btnGenerarK2)

        self.btnGenerarK3 = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerarK3.setObjectName("btnGenerarK3")
        left_layout.addWidget(self.btnGenerarK3)

        # Gráfica del grafo
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        left_layout.addWidget(self.graphicsView)

        # Crear un widget contenedor para los elementos a la izquierda
        left_widget = QtWidgets.QWidget()
        left_widget.setLayout(left_layout)

        # Añadir el contenedor izquierdo al layout principal
        main_layout.addWidget(left_widget)

        # Crear un layout para la parte derecha con las matrices
        right_layout = QtWidgets.QVBoxLayout()

        # Título principal
        self.lblTtitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTtitulo.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
                                      "color:rgb(0, 85, 255);")
        self.lblTtitulo.setObjectName("lblTtitulo")
        right_layout.addWidget(self.lblTtitulo)

        # Contenedor para las matrices y títulos
        self.widgetMatrices = QtWidgets.QWidget(self.centralwidget)
        self.widgetMatrices.setLayout(right_layout)

        # Matriz de Adyacencia (A) y título
        self.lblMatrizAdyacencia = QtWidgets.QLabel(self.widgetMatrices)
        self.lblMatrizAdyacencia.setText("Matriz de Adyacencia:")
        self.lblMatrizAdyacencia.setStyleSheet("font: 12pt; color: black;")
        right_layout.addWidget(self.lblMatrizAdyacencia)

        self.tableAdyacencia = QtWidgets.QTableWidget(self.widgetMatrices)
        self.tableAdyacencia.setRowCount(4)
        self.tableAdyacencia.setColumnCount(4)
        right_layout.addWidget(self.tableAdyacencia)

        # Matriz A^2 y título
        self.lblMatrizCuadrado = QtWidgets.QLabel(self.widgetMatrices)
        self.lblMatrizCuadrado.setText("Matriz K2:")
        self.lblMatrizCuadrado.setStyleSheet("font: 12pt; color: black;")
        right_layout.addWidget(self.lblMatrizCuadrado)

        self.tableCuadrado = QtWidgets.QTableWidget(self.widgetMatrices)
        self.tableCuadrado.setRowCount(4)
        self.tableCuadrado.setColumnCount(4)
        right_layout.addWidget(self.tableCuadrado)

        # Matriz A^3 y título
        self.lblMatrizCubo = QtWidgets.QLabel(self.widgetMatrices)
        self.lblMatrizCubo.setText("Matriz K3:")
        self.lblMatrizCubo.setStyleSheet("font: 12pt; color: black;")
        right_layout.addWidget(self.lblMatrizCubo)

        self.tableCubo = QtWidgets.QTableWidget(self.widgetMatrices)
        self.tableCubo.setRowCount(4)
        self.tableCubo.setColumnCount(4)
        right_layout.addWidget(self.tableCubo)

        # Crear una QScrollArea para contener el layout de matrices
        scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.widgetMatrices)

        # Aseguramos que siempre estén visibles las barras de desplazamiento
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        # Añadir el área de desplazamiento al layout principal
        main_layout.addWidget(scroll_area)

        # Establecer el layout principal para la ventana central
        MainWindow.setCentralWidget(self.centralwidget)

        # Barra de menú y barra de estado
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficador de Grafos"))
        self.btnPintarGrafo.setText(_translate("MainWindow", "Dibujar Grafo"))
        self.btnGenerarK2.setText(_translate("MainWindow", "Generar K2"))
        self.btnGenerarK3.setText(_translate("MainWindow", "Generar K3"))
        self.lblTtitulo.setText(_translate("MainWindow", "Grafos por Mariana Hincapie Henao"))
        self.lblTtitulo_3.setText(_translate("MainWindow", "Matriz de Pesos >>"))

if __name__ == "_main_":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())