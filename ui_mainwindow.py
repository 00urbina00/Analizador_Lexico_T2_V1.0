# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from plaintext import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1340, 885)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.frame_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"color: rgb(0, 0, 255);")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pte_codigo = PlainTextEdit(self.groupBox_2)
        self.pte_codigo.setObjectName(u"pte_codigo")
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setPointSize(12)
        self.pte_codigo.setFont(font1)
        self.pte_codigo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 255);")

        self.gridLayout_8.addWidget(self.pte_codigo, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(180, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.btn_analizar = QPushButton(self.frame_5)
        self.btn_analizar.setObjectName(u"btn_analizar")
        self.btn_analizar.setFont(font)
        self.btn_analizar.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(211, 211, 211);\n"
"	\n"
"	\n"
"\n"
"}")

        self.gridLayout_7.addWidget(self.btn_analizar, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(500, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(500, 16777215))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pte2 = QPlainTextEdit(self.groupBox_3)
        self.pte2.setObjectName(u"pte2")
        self.pte2.setMaximumSize(QSize(500, 16777215))
        self.pte2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.pte2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 0, 2, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 350))
        self.frame_3.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.frame_3)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tw_componentes = QTableWidget(self.groupBox)
        if (self.tw_componentes.columnCount() < 3):
            self.tw_componentes.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_componentes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_componentes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_componentes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tw_componentes.rowCount() < 1):
            self.tw_componentes.setRowCount(1)
        self.tw_componentes.setObjectName(u"tw_componentes")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        self.tw_componentes.setFont(font2)
        self.tw_componentes.setStyleSheet(u"QTableWidget {\n"
"       \n"
"	background-color: rgb(255, 255, 255);\n"
"    }\n"
"    \n"
"    QHeaderView::section {\n"
"        \n"
"	\n"
"	background-color: rgb(180, 180, 180);\n"
"   \n"
"	color: rgb(0, 85, 255);\n"
"    }\n"
"    \n"
"    QTableWidget::item {\n"
"        \n"
"	background-color: rgb(200, 200, 200);\n"
"    \n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"    }")
        self.tw_componentes.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tw_componentes.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_componentes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tw_componentes.setDragDropOverwriteMode(False)
        self.tw_componentes.setAlternatingRowColors(False)
        self.tw_componentes.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tw_componentes.setTextElideMode(Qt.ElideMiddle)
        self.tw_componentes.setSortingEnabled(False)
        self.tw_componentes.setRowCount(1)
        self.tw_componentes.horizontalHeader().setVisible(True)
        self.tw_componentes.horizontalHeader().setMinimumSectionSize(400)
        self.tw_componentes.horizontalHeader().setDefaultSectionSize(420)
        self.tw_componentes.horizontalHeader().setHighlightSections(True)
        self.tw_componentes.horizontalHeader().setProperty("showSortIndicator", False)
        self.tw_componentes.horizontalHeader().setStretchLastSection(False)
        self.tw_componentes.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tw_componentes, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1340, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Analizador Lexico", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.pte_codigo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"int void(){while(true){if(true)return;}}", None))
        self.btn_analizar.setText(QCoreApplication.translate("MainWindow", u"Analizar", None))
        self.groupBox_3.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Componentes", None))
        ___qtablewidgetitem = self.tw_componentes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Lexema", None));
        ___qtablewidgetitem1 = self.tw_componentes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Token", None));
        ___qtablewidgetitem2 = self.tw_componentes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"#", None));
    # retranslateUi

