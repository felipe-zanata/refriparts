# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1088, 648)
        MainWindow.setStyleSheet(u"background-color: rgb(244, 250, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ContainerEsq = QFrame(self.centralwidget)
        self.ContainerEsq.setObjectName(u"ContainerEsq")
        self.ContainerEsq.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ContainerEsq.sizePolicy().hasHeightForWidth())
        self.ContainerEsq.setSizePolicy(sizePolicy)
        self.ContainerEsq.setMinimumSize(QSize(0, 560))
        self.ContainerEsq.setMaximumSize(QSize(0, 560))
        self.ContainerEsq.setFrameShape(QFrame.StyledPanel)
        self.ContainerEsq.setFrameShadow(QFrame.Raised)
        self.ContainerEsq.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.ContainerEsq)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_2 = QFrame(self.ContainerEsq)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color :rgb(244, 250, 255);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"	text-align: left;\n"
"		background-color: rgb(244, 250, 255);\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 4px;\n"
"\n"
"	background-color: rgb(228, 243, 255)\n"
"\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(172, 213, 241);\n"
"	 border-top-left-radius: 8px;\n"
"	 border-bottom-left-radius: 8px\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	Color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 150, 485))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy1)
        self.page.setMinimumSize(QSize(0, 200))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_home = QPushButton(self.page)
        self.bt_home.setObjectName(u"bt_home")
        self.bt_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.bt_home.setFont(font1)
        self.bt_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home.setCheckable(False)
        self.bt_home.setChecked(False)
        self.bt_home.setAutoRepeat(False)
        self.bt_home.setAutoExclusive(False)
        self.bt_home.setAutoDefault(False)
        self.bt_home.setFlat(False)

        self.verticalLayout_4.addWidget(self.bt_home)

        self.bt_Cadastrar = QPushButton(self.page)
        self.bt_Cadastrar.setObjectName(u"bt_Cadastrar")
        self.bt_Cadastrar.setMinimumSize(QSize(0, 30))
        self.bt_Cadastrar.setFont(font1)
        self.bt_Cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bt_Cadastrar)

        self.bt_CompararValores = QPushButton(self.page)
        self.bt_CompararValores.setObjectName(u"bt_CompararValores")
        self.bt_CompararValores.setMinimumSize(QSize(0, 30))
        self.bt_CompararValores.setFont(font1)
        self.bt_CompararValores.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bt_CompararValores)

        self.bt_Valores = QPushButton(self.page)
        self.bt_Valores.setObjectName(u"bt_Valores")
        self.bt_Valores.setMinimumSize(QSize(0, 30))
        self.bt_Valores.setFont(font1)

        self.verticalLayout_4.addWidget(self.bt_Valores)

        self.bt_Sobre = QPushButton(self.page)
        self.bt_Sobre.setObjectName(u"bt_Sobre")
        self.bt_Sobre.setMinimumSize(QSize(0, 30))
        self.bt_Sobre.setSizeIncrement(QSize(0, 0))
        self.bt_Sobre.setFont(font1)
        self.bt_Sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.bt_Sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout.addWidget(self.ContainerEsq, 0, 0, 1, 1)

        self.ContainerPrincipal = QFrame(self.centralwidget)
        self.ContainerPrincipal.setObjectName(u"ContainerPrincipal")
        self.ContainerPrincipal.setFrameShape(QFrame.StyledPanel)
        self.ContainerPrincipal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ContainerPrincipal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 9, 9)
        self.FrameCabecalho = QFrame(self.ContainerPrincipal)
        self.FrameCabecalho.setObjectName(u"FrameCabecalho")
        self.FrameCabecalho.setStyleSheet(u"")
        self.FrameCabecalho.setFrameShape(QFrame.StyledPanel)
        self.FrameCabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameCabecalho)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_menu = QPushButton(self.FrameCabecalho)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icones/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.label = QLabel(self.FrameCabecalho)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.FrameCabecalho, 0, Qt.AlignTop)

        self.MainFrame = QFrame(self.ContainerPrincipal)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy2)
        self.MainFrame.setStyleSheet(u"background: rgb(228, 243, 255)\n"
"")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.MainFrame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.Logo = QLabel(self.pg_home)
        self.Logo.setObjectName(u"Logo")

        self.verticalLayout_6.addWidget(self.Logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_Cadastrar = QWidget()
        self.pg_Cadastrar.setObjectName(u"pg_Cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_Cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.pg_Cadastrar)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"height: 15px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Cadastro_label = QLabel(self.frame_3)
        self.Cadastro_label.setObjectName(u"Cadastro_label")
        self.Cadastro_label.setMinimumSize(QSize(300, 100))
        self.Cadastro_label.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_8.addWidget(self.Cadastro_label)

        self.txt_produto = QLineEdit(self.frame_3)
        self.txt_produto.setObjectName(u"txt_produto")
        self.txt_produto.setMinimumSize(QSize(0, 22))
        self.txt_produto.setAlignment(Qt.AlignCenter)
        self.txt_produto.setDragEnabled(False)
        self.txt_produto.setClearButtonEnabled(False)

        self.verticalLayout_8.addWidget(self.txt_produto)

        self.txt_sku = QLineEdit(self.frame_3)
        self.txt_sku.setObjectName(u"txt_sku")
        self.txt_sku.setMinimumSize(QSize(0, 22))
        self.txt_sku.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_sku)

        self.txt_preco = QLineEdit(self.frame_3)
        self.txt_preco.setObjectName(u"txt_preco")
        self.txt_preco.setMinimumSize(QSize(0, 22))
        self.txt_preco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_preco)

        self.txt_link = QLineEdit(self.frame_3)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setMinimumSize(QSize(0, 22))
        self.txt_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_link)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.bt_Cadastrar_2 = QPushButton(self.frame_3)
        self.bt_Cadastrar_2.setObjectName(u"bt_Cadastrar_2")
        sizePolicy.setHeightForWidth(self.bt_Cadastrar_2.sizePolicy().hasHeightForWidth())
        self.bt_Cadastrar_2.setSizePolicy(sizePolicy)
        self.bt_Cadastrar_2.setMinimumSize(QSize(14, 20))
        self.bt_Cadastrar_2.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.bt_Cadastrar_2.setFont(font2)
        self.bt_Cadastrar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Cadastrar_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #386641;\n"
"	 border-radius: 10px;\n"
"	  color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"		border-radius: 10px;\n"
"			background-color: rgb(243, 243, 243	);\n"
"}")
        self.bt_Cadastrar_2.setAutoDefault(False)
        self.bt_Cadastrar_2.setFlat(False)

        self.horizontalLayout_6.addWidget(self.bt_Cadastrar_2)

        self.bt_alterar = QPushButton(self.frame_3)
        self.bt_alterar.setObjectName(u"bt_alterar")
        sizePolicy.setHeightForWidth(self.bt_alterar.sizePolicy().hasHeightForWidth())
        self.bt_alterar.setSizePolicy(sizePolicy)
        self.bt_alterar.setMinimumSize(QSize(14, 20))
        self.bt_alterar.setMaximumSize(QSize(16777215, 40))
        self.bt_alterar.setFont(font2)
        self.bt_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #386641;\n"
"	 border-radius: 10px;\n"
"	  color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"		border-radius: 10px;\n"
"			background-color: rgb(243, 243, 243	);\n"
"}")
        self.bt_alterar.setAutoDefault(False)
        self.bt_alterar.setFlat(False)

        self.horizontalLayout_6.addWidget(self.bt_alterar)

        self.bt_deletar = QPushButton(self.frame_3)
        self.bt_deletar.setObjectName(u"bt_deletar")
        self.bt_deletar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bt_deletar.sizePolicy().hasHeightForWidth())
        self.bt_deletar.setSizePolicy(sizePolicy)
        self.bt_deletar.setMinimumSize(QSize(30, 20))
        self.bt_deletar.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.bt_deletar.setFont(font3)
        self.bt_deletar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_deletar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #780000;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton{\n"
"		border-radius: 10px;\n"
"			background-color: rgb(243, 243, 243);\n"
"}")

        self.horizontalLayout_6.addWidget(self.bt_deletar)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_produtos = QTableView(self.frame_6)
        self.tb_produtos.setObjectName(u"tb_produtos")

        self.horizontalLayout.addWidget(self.tb_produtos)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_7.addWidget(self.frame)

        self.Pages.addWidget(self.pg_Cadastrar)
        self.pg_comparar = QWidget()
        self.pg_comparar.setObjectName(u"pg_comparar")
        self.verticalLayout_16 = QVBoxLayout(self.pg_comparar)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_7 = QFrame(self.pg_comparar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 22))
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"height: 15px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_pesquisa_valores = QLabel(self.frame_8)
        self.label_pesquisa_valores.setObjectName(u"label_pesquisa_valores")
        self.label_pesquisa_valores.setMinimumSize(QSize(300, 100))
        self.label_pesquisa_valores.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);")

        self.verticalLayout_9.addWidget(self.label_pesquisa_valores)

        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy4)
        self.comboBox.setMinimumSize(QSize(0, 22))
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(10)
        self.comboBox.setFont(font4)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background: #fff\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.comboBox)

        self.bt_comparar_sku = QLineEdit(self.frame_8)
        self.bt_comparar_sku.setObjectName(u"bt_comparar_sku")
        self.bt_comparar_sku.setMinimumSize(QSize(0, 22))
        self.bt_comparar_sku.setAlignment(Qt.AlignCenter)
        self.bt_comparar_sku.setDragEnabled(False)
        self.bt_comparar_sku.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.bt_comparar_sku)

        self.txt_comparar_preco = QLineEdit(self.frame_8)
        self.txt_comparar_preco.setObjectName(u"txt_comparar_preco")
        self.txt_comparar_preco.setMinimumSize(QSize(0, 22))
        self.txt_comparar_preco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.txt_comparar_preco)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.bt_pesquisar = QPushButton(self.frame_8)
        self.bt_pesquisar.setObjectName(u"bt_pesquisar")
        sizePolicy.setHeightForWidth(self.bt_pesquisar.sizePolicy().hasHeightForWidth())
        self.bt_pesquisar.setSizePolicy(sizePolicy)
        self.bt_pesquisar.setMinimumSize(QSize(14, 20))
        self.bt_pesquisar.setMaximumSize(QSize(16777215, 40))
        self.bt_pesquisar.setFont(font2)
        self.bt_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pesquisar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #90a955;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"\n"
"}\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(243, 243, 243);	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #ffff;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")
        self.bt_pesquisar.setAutoDefault(False)
        self.bt_pesquisar.setFlat(False)

        self.horizontalLayout_7.addWidget(self.bt_pesquisar)

        self.bt_limpar = QPushButton(self.frame_8)
        self.bt_limpar.setObjectName(u"bt_limpar")
        self.bt_limpar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bt_limpar.sizePolicy().hasHeightForWidth())
        self.bt_limpar.setSizePolicy(sizePolicy)
        self.bt_limpar.setMinimumSize(QSize(30, 20))
        self.bt_limpar.setMaximumSize(QSize(16777215, 40))
        self.bt_limpar.setFont(font3)
        self.bt_limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_limpar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: #bf4342;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton{\n"
"		border-radius: 10px;\n"
"		background-color: rgb(243, 243, 243);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #ffff;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #ffff;\n"
"}")

        self.horizontalLayout_7.addWidget(self.bt_limpar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy3.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy3)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tb_concorrentes = QTableView(self.frame_9)
        self.tb_concorrentes.setObjectName(u"tb_concorrentes")

        self.horizontalLayout_5.addWidget(self.tb_concorrentes)


        self.verticalLayout_15.addWidget(self.frame_9)


        self.verticalLayout_16.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_comparar)
        self.pg_compararValores = QWidget()
        self.pg_compararValores.setObjectName(u"pg_compararValores")
        self.pg_compararValores.setStyleSheet(u"QLineEdit{\n"
"	background-color: #F7F8FF;\n"
"	border-radius: 5px;\n"
"	border-top: 1 solid gray;\n"
"	border-left: 1 solid gray;\n"
"	border-right: 1 solid gray;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: WHITE;\n"
"	border-radius: 3px\n"
"\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.pg_compararValores)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetMinimumSize)
        self.lineEdit_2 = QLineEdit(self.pg_compararValores)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy4)
        self.lineEdit_2.setMinimumSize(QSize(200, 30))

        self.verticalLayout_13.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.pg_compararValores)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 30))

        self.verticalLayout_13.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.pg_compararValores)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(200, 30))

        self.verticalLayout_13.addWidget(self.lineEdit_4)


        self.gridLayout_2.addLayout(self.verticalLayout_13, 2, 1, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_6 = QLabel(self.pg_compararValores)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.label_6)

        self.label_9 = QLabel(self.pg_compararValores)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_11 = QLabel(self.pg_compararValores)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.label_11)


        self.gridLayout_2.addLayout(self.verticalLayout_11, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 1, 0, 1, 3)

        self.label_5 = QLabel(self.pg_compararValores)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 50))

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.tableWidget = QTableWidget(self.pg_compararValores)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(731, 191))
        self.tableWidget.setMaximumSize(QSize(16777215, 10000))

        self.verticalLayout_14.addWidget(self.tableWidget)

        self.Pages.addWidget(self.pg_compararValores)
        self.pg_Sobre = QWidget()
        self.pg_Sobre.setObjectName(u"pg_Sobre")
        self.verticalLayout_12 = QVBoxLayout(self.pg_Sobre)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_7 = QLabel(self.pg_Sobre)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_12.addWidget(self.label_7)

        self.label_8 = QLabel(self.pg_Sobre)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_8)

        self.Pages.addWidget(self.pg_Sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.MainFrame)

        self.frame_5 = QFrame(self.ContainerPrincipal)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        self.label_2.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.ContainerPrincipal, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.bt_home.setDefault(False)
        self.Pages.setCurrentIndex(2)
        self.bt_Cadastrar_2.setDefault(False)
        self.bt_alterar.setDefault(False)
        self.bt_pesquisar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.bt_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produtos", None))
        self.bt_CompararValores.setText(QCoreApplication.translate("MainWindow", u"Comparar Valores", None))
        self.bt_Valores.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.bt_Sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
#if QT_CONFIG(whatsthis)
        self.bt_menu.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/menu.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.bt_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sistema de Cadastro</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Logo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://images.tcdn.com.br/files/1036166/themes/23/img/settings/site.png?de28e0d2545c0974ad4c74fbdb9ac502\"><span style=\" text-decoration: underline; color:#0000ff;\">Logo_Refriparts</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Logo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icones/Logo_Refriparts.webp\" /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/Logo_Refriparts.webp\"/></p></body></html>", None))
        self.Cadastro_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Produtos</span></p></body></html>", None))
        self.txt_produto.setText("")
        self.txt_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do produto", None))
        self.txt_sku.setText("")
        self.txt_sku.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SKU", None))
        self.txt_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.bt_Cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.bt_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.bt_deletar.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.label_pesquisa_valores.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Pesquisa de valores</span></p></body></html>", None))
        self.bt_comparar_sku.setText("")
        self.bt_comparar_sku.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SKU", None))
        self.txt_comparar_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.bt_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.bt_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">C\u00f3digo:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Nome:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Pre\u00e7o:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Comparar valores</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sobre</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt;\">Do Latim: Gutta non violenter, sed assidua lapsu in saxum fodit. </span></p><p align=\"justify\"><span style=\" font-size:11pt;\">Do Italiano: La goccia scava nella roccia non con violenza, ma con una caduta continua.</span></p><p align=\"justify\"><span style=\" font-size:11pt;\">Do Portug\u00eas: \u00c1gua mole em pedra dura tanto bate at\u00e9 que fura.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Refriparts</p></body></html>", None))
    # retranslateUi

