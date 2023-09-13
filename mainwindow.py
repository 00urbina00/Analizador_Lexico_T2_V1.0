from PySide2.QtWidgets import QMainWindow, QPushButton, QPlainTextEdit, QTableWidget, QTableWidgetItem, QHeaderView
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Qt

from componente import Componente


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.elementos = []
        self.componentes = []

        # Definir los widgets

        # Boton
        self.btn_analizar = self.findChild(QPushButton, "btn_analizar")
        # PlainTextEdit
        self.pte_codigo = self.findChild(QPlainTextEdit, "pte_codigo")
        self.pte2 = self.findChild(QPushButton, "pte2")
        # Tabla
        self.tw_componentes = self.findChild(QTableWidget, "tw_componentes")
        self.tw_componentes.verticalHeader().setVisible(False)
        # Eventos
        self.btn_analizar.clicked.connect(self.mostrar_elementos)
        
        self.ui.centralwidget.resizeEvent = lambda event: self.resize_table()

    # Funciones
    # -----------------------------------------------------------------------------------
    def resize_table(self):
        self.tw_componentes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    
    def analizar(self):
        cadena = self.pte_codigo.toPlainText()
        self.componentes = []
        indice = 0
        estado = 0
        while indice <= (len(cadena) - 1) and estado == 0:
            lexema = ''
            token = 'error'
            while (indice <= (
                    len(cadena) - 1) and estado != 20):  # Mientras la cadena no termine y el estado no sea 20:
                if estado == 0:  # Si el estado actual es 0: (inicial) --------------------------------------------
                    if cadena[indice].isspace():  # El caracter es \t o \n o espacio
                        estado = 0  # Estado se mantiene en 0
                    elif cadena[indice].isalpha() or cadena[indice] == '_':  # Car, es letra o '_'
                        estado = 4  # Estado se actualiza a 4
                        lexema += cadena[indice]  # Se agrega el caracter al lexema
                        token = 'id'  # El lexema es de tipo Identificador
                    elif cadena[indice] == '$':  # El caracter es '$'
                        estado = 20  # Estado se actualiza a 20 (final)
                        lexema += cadena[indice]  # Se agrega el caracter al lexema
                        token = 'pesos'  # El lexema es de tipo pesos
                    elif cadena[indice].isdigit():  # El caracter es dígito
                        estado = 19  # Estado se actualiza a 20 (final)
                        lexema += cadena[indice]  # Se agrega el caracter al lexema
                        token = 'constante'  # El lexema es de tipo constante
                    elif cadena[indice] == '!':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'opNot'
                    elif cadena[indice] == '(':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'parIzq'
                    elif cadena[indice] == ')':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'parDer'
                    elif cadena[indice] == '{':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'llaveIzq'
                    elif cadena[indice] == '}':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'llaveDer'
                    elif cadena[indice] == ';':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'puntoYComa'
                    elif cadena[indice] == ':':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'dosPuntos'
                    elif (cadena[indice] == '+' or cadena[indice] == '-' or cadena[indice] == '*' or
                          cadena[indice] == '/'):
                        estado = 20
                        lexema += cadena[indice]
                        token = 'opAritmetico'
                    elif cadena[indice] == '.':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'punto'
                    elif cadena[indice] == ',':
                        estado = 20
                        lexema += cadena[indice]
                        token = 'coma'
                    elif cadena[indice] == '=':
                        lexema += cadena[indice]  # Se agrega el caracter al lexema
                        token = 'asignación'  # El lexema es de tipo asignacion
                        estado = 5  # Estado se actualiza a 5
                    else:  # El caracter es de algún otro tipo
                        estado = 20  # Estado se actualiza a 20 (final)
                        token = 'error'  # El lexema es de tipo Error
                        lexema = cadena[indice]  # El lexema, se vuelve el caracter que dio error
                    indice += 1  # Se terminó de leer el caracter, se incrementa el índice
                elif estado == 4:  # Si el estado actual es 4: ------------------------------------------------
                    if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice] == '_':
                        estado = 4  # Si el caracter es dígito, letra o '_' y estamos en estado 4, nos quedamos
                        lexema += cadena[indice]  # Se agrega el caracter a lexema
                        token = 'id'  # El lexema es de tipo Identificador
                        indice += 1  # Se incrementa el indice de la cadena
                    else:  # No se cumplio alguna condición
                        estado = 20  # El estado se vuelve 20 (final)
                elif estado == 5:  # Si el estado actual es 5: ------------------------------------------------
                    if cadena[indice] != '=':  # y el caracter es diferente de '=':
                        estado = 20  # El estado actual se vuelve 20 (final)
                    else:  # Si el caracter es '=':
                        estado = 20  # El estado se vuelve 20 (final)
                        lexema += cadena[indice]  # Se agrega el caracter a lexema
                        token = 'opRelacional'  # El tipo de lexema es OpRelacional
                        indice += 1  # Se incrementa el indice
                elif estado == 19:
                    if cadena[indice].isdigit():
                        lexema += cadena[indice]  # Se agrega el caracter a lexema
                        token = 'constante'
                        indice += 1  # Se incrementa el indice
                    else:
                        estado = 20
            estado = 0
            componente = Componente(lexema, token)  # Se crea un nuevo componente con los elementos creados
            self.componentes.append(componente)  # Se agrega el componente creado a la lista de componentes

    def mostrar_elementos(self):
        self.analizar()
        self.tw_componentes.setRowCount(len(self.componentes))
        for fila, componente in enumerate(self.componentes):
            self.tw_componentes.setItem(fila, 0, QTableWidgetItem(componente.get_lexema()))
            self.tw_componentes.setItem(fila, 1, QTableWidgetItem(componente.get_token()))
            self.tw_componentes.setItem(fila, 2, QTableWidgetItem(str(componente.get_id())))

            self.tw_componentes.item(fila, 0).setTextAlignment(Qt.AlignCenter)
            self.tw_componentes.item(fila, 1).setTextAlignment(Qt.AlignCenter)
            self.tw_componentes.item(fila, 2).setTextAlignment(Qt.AlignCenter)

        self.tw_componentes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

