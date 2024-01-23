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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 946)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(244, 250, 255);")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 12)
        self.ContainerEsq = QFrame(self.centralwidget)
        self.ContainerEsq.setObjectName(u"ContainerEsq")
        sizePolicy.setHeightForWidth(self.ContainerEsq.sizePolicy().hasHeightForWidth())
        self.ContainerEsq.setSizePolicy(sizePolicy)
        self.ContainerEsq.setMinimumSize(QSize(0, 0))
        self.ContainerEsq.setMaximumSize(QSize(47, 16777215))
        self.ContainerEsq.setStyleSheet(u"QFrame{\n"
"	background-color :rgb(244, 250, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(172, 213, 241);\n"
"	border-top-left-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(172, 213, 241);\n"
"	border-right: 1.5px solid gray;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	Color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"	padding: 5px;\n"
"}")
        self.ContainerEsq.setFrameShape(QFrame.StyledPanel)
        self.ContainerEsq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ContainerEsq)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.ContainerEsq)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(300, 16777215))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	background-color :rgb(244, 250, 255);\n"
"}\n"
"QToolBox{\n"
"  text-align: left;\n"
"	background-color: rgb(244, 250, 255);\n"
"}\n"
"QToolBox::tab{\n"
"	border-radius: 4px;\n"
"	background-color: rgb(228, 243, 255)\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_11)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 96, 53))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(48, 51))
        self.label_7.setMaximumSize(QSize(48, 51))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.layoutWidget1 = QWidget(self.frame_11)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1, 61, 229, 247))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bt_menu2 = QPushButton(self.layoutWidget1)
        self.bt_menu2.setObjectName(u"bt_menu2")
        self.bt_menu2.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        self.bt_menu2.setFont(font)
        self.bt_menu2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_menu2.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icones/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu2.setIcon(icon)
        self.bt_menu2.setIconSize(QSize(25, 25))
        self.bt_menu2.setCheckable(False)
        self.bt_menu2.setChecked(False)
        self.bt_menu2.setAutoRepeat(False)
        self.bt_menu2.setAutoExclusive(False)
        self.bt_menu2.setAutoDefault(False)
        self.bt_menu2.setFlat(False)

        self.verticalLayout_3.addWidget(self.bt_menu2)

        self.bt_home = QPushButton(self.layoutWidget1)
        self.bt_home.setObjectName(u"bt_home")
        self.bt_home.setMinimumSize(QSize(0, 30))
        self.bt_home.setFont(font)
        self.bt_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_home.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icones/home-_1_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_home.setIcon(icon1)
        self.bt_home.setIconSize(QSize(25, 25))
        self.bt_home.setCheckable(False)
        self.bt_home.setChecked(False)
        self.bt_home.setAutoRepeat(False)
        self.bt_home.setAutoExclusive(False)
        self.bt_home.setAutoDefault(False)
        self.bt_home.setFlat(False)

        self.verticalLayout_3.addWidget(self.bt_home)

        self.bt_Cadastrar = QPushButton(self.layoutWidget1)
        self.bt_Cadastrar.setObjectName(u"bt_Cadastrar")
        self.bt_Cadastrar.setMinimumSize(QSize(0, 30))
        self.bt_Cadastrar.setFont(font)
        self.bt_Cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Cadastrar.setStyleSheet(u"QPushButton{\n"
"text-align: left;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icones/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Cadastrar.setIcon(icon2)
        self.bt_Cadastrar.setIconSize(QSize(25, 25))
        self.bt_Cadastrar.setCheckable(False)
        self.bt_Cadastrar.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.bt_Cadastrar)

        self.bt_PesquisarProdutos = QPushButton(self.layoutWidget1)
        self.bt_PesquisarProdutos.setObjectName(u"bt_PesquisarProdutos")
        self.bt_PesquisarProdutos.setMinimumSize(QSize(0, 30))
        self.bt_PesquisarProdutos.setFont(font)
        self.bt_PesquisarProdutos.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_PesquisarProdutos.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icones/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_PesquisarProdutos.setIcon(icon3)
        self.bt_PesquisarProdutos.setIconSize(QSize(25, 25))
        self.bt_PesquisarProdutos.setCheckable(False)
        self.bt_PesquisarProdutos.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.bt_PesquisarProdutos)

        self.bt_comparativo = QPushButton(self.layoutWidget1)
        self.bt_comparativo.setObjectName(u"bt_comparativo")
        self.bt_comparativo.setMinimumSize(QSize(0, 30))
        self.bt_comparativo.setSizeIncrement(QSize(0, 0))
        self.bt_comparativo.setFont(font)
        self.bt_comparativo.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icones/dollar-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_comparativo.setIcon(icon4)
        self.bt_comparativo.setIconSize(QSize(25, 25))
        self.bt_comparativo.setCheckable(False)
        self.bt_comparativo.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.bt_comparativo)

        self.bt_Sobre = QPushButton(self.layoutWidget1)
        self.bt_Sobre.setObjectName(u"bt_Sobre")
        self.bt_Sobre.setMinimumSize(QSize(0, 30))
        self.bt_Sobre.setSizeIncrement(QSize(0, 0))
        self.bt_Sobre.setFont(font)
        self.bt_Sobre.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icones/help-circle-_1_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Sobre.setIcon(icon5)
        self.bt_Sobre.setIconSize(QSize(25, 25))
        self.bt_Sobre.setCheckable(False)
        self.bt_Sobre.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.bt_Sobre)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.horizontalLayout_12.addWidget(self.ContainerEsq)

        self.ContainerPrincipal = QFrame(self.centralwidget)
        self.ContainerPrincipal.setObjectName(u"ContainerPrincipal")
        sizePolicy.setHeightForWidth(self.ContainerPrincipal.sizePolicy().hasHeightForWidth())
        self.ContainerPrincipal.setSizePolicy(sizePolicy)
        self.ContainerPrincipal.setFrameShape(QFrame.StyledPanel)
        self.ContainerPrincipal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.ContainerPrincipal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 9, 0)
        self.FrameCabecalho = QFrame(self.ContainerPrincipal)
        self.FrameCabecalho.setObjectName(u"FrameCabecalho")
        self.FrameCabecalho.setStyleSheet(u"")
        self.FrameCabecalho.setFrameShape(QFrame.StyledPanel)
        self.FrameCabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameCabecalho)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.FrameCabecalho)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy3)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_14 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_14.setSpacing(4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(6, 6, 6, 6)
        self.Logo = QLabel(self.pg_home)
        self.Logo.setObjectName(u"Logo")

        self.horizontalLayout_14.addWidget(self.Logo)

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
        self.frame_4.setStyleSheet(u"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"padding:20;\n"
"color: rgb(0, 99, 148);\n"
"/*margin-top: 25px;\n"
"margin-bottom: 25px; *\\\n"
"")

        self.verticalLayout_10.addWidget(self.label_5)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 230))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"height: 15px;\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 3px;\n"
"	border: 2px solid transparent;\n"
"	background-color: rgb( 255, 255, 255);\n"
"	padding: 3px;\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"QLineEdit:hover {\n"
"	border-color: #9BB4D6;\n"
"}\n"
"/*QLineEdit{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"	padding: 5px;\n"
"	border-radius: 2px solid transparent;\n"
"} *\\\n"
"QLineEdit{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	padding: 5px;\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.txt_produto = QLineEdit(self.frame_3)
        self.txt_produto.setObjectName(u"txt_produto")
        self.txt_produto.setMinimumSize(QSize(0, 30))
        self.txt_produto.setStyleSheet(u"")
        self.txt_produto.setAlignment(Qt.AlignCenter)
        self.txt_produto.setDragEnabled(False)
        self.txt_produto.setClearButtonEnabled(False)

        self.verticalLayout_8.addWidget(self.txt_produto)

        self.txt_sku = QLineEdit(self.frame_3)
        self.txt_sku.setObjectName(u"txt_sku")
        self.txt_sku.setMinimumSize(QSize(0, 22))
        self.txt_sku.setStyleSheet(u"")
        self.txt_sku.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_sku)

        self.txt_preco = QLineEdit(self.frame_3)
        self.txt_preco.setObjectName(u"txt_preco")
        self.txt_preco.setMinimumSize(QSize(0, 22))
        self.txt_preco.setStyleSheet(u"")
        self.txt_preco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_preco)

        self.txt_link = QLineEdit(self.frame_3)
        self.txt_link.setObjectName(u"txt_link")
        self.txt_link.setMinimumSize(QSize(0, 22))
        self.txt_link.setStyleSheet(u"")
        self.txt_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.txt_link)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 2, -1, 5)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.bt_Cadastrar_2 = QPushButton(self.frame_3)
        self.bt_Cadastrar_2.setObjectName(u"bt_Cadastrar_2")
        sizePolicy.setHeightForWidth(self.bt_Cadastrar_2.sizePolicy().hasHeightForWidth())
        self.bt_Cadastrar_2.setSizePolicy(sizePolicy)
        self.bt_Cadastrar_2.setMinimumSize(QSize(14, 42))
        self.bt_Cadastrar_2.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.bt_Cadastrar_2.setFont(font1)
        self.bt_Cadastrar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_Cadastrar_2.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #81C784;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #66BB6A;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")
        self.bt_Cadastrar_2.setAutoDefault(False)
        self.bt_Cadastrar_2.setFlat(False)

        self.horizontalLayout_6.addWidget(self.bt_Cadastrar_2)

        self.bt_alterar = QPushButton(self.frame_3)
        self.bt_alterar.setObjectName(u"bt_alterar")
        sizePolicy.setHeightForWidth(self.bt_alterar.sizePolicy().hasHeightForWidth())
        self.bt_alterar.setSizePolicy(sizePolicy)
        self.bt_alterar.setMinimumSize(QSize(14, 42))
        self.bt_alterar.setMaximumSize(QSize(16777215, 40))
        self.bt_alterar.setFont(font1)
        self.bt_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #FFA726;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #FF9800;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")
        self.bt_alterar.setAutoDefault(False)
        self.bt_alterar.setFlat(False)

        self.horizontalLayout_6.addWidget(self.bt_alterar)

        self.bt_deletar = QPushButton(self.frame_3)
        self.bt_deletar.setObjectName(u"bt_deletar")
        self.bt_deletar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bt_deletar.sizePolicy().hasHeightForWidth())
        self.bt_deletar.setSizePolicy(sizePolicy)
        self.bt_deletar.setMinimumSize(QSize(30, 42))
        self.bt_deletar.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.bt_deletar.setFont(font2)
        self.bt_deletar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_deletar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #EF5350;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #F44336;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")

        self.horizontalLayout_6.addWidget(self.bt_deletar)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.bt_exportar = QPushButton(self.frame_3)
        self.bt_exportar.setObjectName(u"bt_exportar")
        self.bt_exportar.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bt_exportar.sizePolicy().hasHeightForWidth())
        self.bt_exportar.setSizePolicy(sizePolicy4)
        self.bt_exportar.setMinimumSize(QSize(10, 42))
        self.bt_exportar.setMaximumSize(QSize(16777215, 40))
        self.bt_exportar.setFont(font2)
        self.bt_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_exportar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton{\n"
"	background-color: #A5D6A7;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #81C784;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icones/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_exportar.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.bt_exportar)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.verticalLayout_15.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_produtos = QTableView(self.frame_6)
        self.tb_produtos.setObjectName(u"tb_produtos")
        self.tb_produtos.setMinimumSize(QSize(0, 400))
        self.tb_produtos.setMaximumSize(QSize(16777215, 400))
        self.tb_produtos.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.tb_produtos)


        self.verticalLayout_10.addWidget(self.frame_6)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_7.addWidget(self.frame)

        self.Pages.addWidget(self.pg_Cadastrar)
        self.pg_comparativo = QWidget()
        self.pg_comparativo.setObjectName(u"pg_comparativo")
        self.verticalLayout_2 = QVBoxLayout(self.pg_comparativo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_12 = QFrame(self.pg_comparativo)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, -1, -1, 0)
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"padding:20;\n"
"color: rgb(0, 99, 148);")

        self.horizontalLayout_13.addWidget(self.label_10)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.pg_comparativo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tb_comparativo = QTableView(self.frame_2)
        self.tb_comparativo.setObjectName(u"tb_comparativo")
        self.tb_comparativo.setStyleSheet(u"QTableView{\n"
"	font: 11pt;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #fff;\n"
"	color: #000;\n"
"	font: 12pt;	\n"
"	border-left: none;\n"
"    border-bottom: 0.5px solid transparent;\n"
"    border-top: none;\n"
"    border-right: none;\n"
"}\n"
"QTableView::item {\n"
"\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableView::item:alternate {\n"
"	background-color: #f2f2f2;\n"
"	background-color: #fff;\n"
"    }\n"
"")
        self.tb_comparativo.setAlternatingRowColors(True)
        self.tb_comparativo.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.tb_comparativo)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.Pages.addWidget(self.pg_comparativo)
        self.pg_comparar = QWidget()
        self.pg_comparar.setObjectName(u"pg_comparar")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_comparar)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_7 = QFrame(self.pg_comparar)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb( 255, 255, 255);\n"
"	font: 10pt \"MS Shell Dig 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"Background-color: rgb(231, 231, 231);\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"margin-top: 25px;\n"
"margin-bottom: 25px;")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_14.addWidget(self.label_4)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 22))
        self.frame_8.setStyleSheet(u"QPushButton{\n"
"	height: 15px;\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 3px;\n"
"	border: 2px solid transparent\n"
"}\n"
"\n"
"QComboBox{\n"
"	border-radius:3px;\n"
"	background-color: WHITE;\n"
"	border: 2px solid transparent\n"
"}\n"
"QLineEdit:hover {\n"
"	border-color: #9BB4D6;\n"
"}\n"
"QComboBox:hover{\n"
"	   border-color: #9BB4D6;\n"
"}\n"
"\n"
"/*QPushButton {\n"
"    background-color: #ecf0f1;\n"
"    border: 2px solid transparent;\n"
"    border-radius: 5px;\n"
"    color: #333;\n"
"    padding: 10px 20px;\n"
"    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #3498db;\n"
"}*\\\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy3.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy3)
        self.comboBox.setMinimumSize(QSize(0, 32))
        self.comboBox.setMaximumSize(QSize(16777215, 40))
        self.comboBox.setFont(font)

        self.verticalLayout_9.addWidget(self.comboBox)

        self.txt_comparar_sku = QLineEdit(self.frame_8)
        self.txt_comparar_sku.setObjectName(u"txt_comparar_sku")
        self.txt_comparar_sku.setMinimumSize(QSize(0, 32))
        self.txt_comparar_sku.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dig 2"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.txt_comparar_sku.setFont(font3)
        self.txt_comparar_sku.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.txt_comparar_sku)

        self.txt_comparar_preco = QLineEdit(self.frame_8)
        self.txt_comparar_preco.setObjectName(u"txt_comparar_preco")
        self.txt_comparar_preco.setMinimumSize(QSize(0, 32))
        self.txt_comparar_preco.setMaximumSize(QSize(16777215, 40))
        self.txt_comparar_preco.setFont(font3)
        self.txt_comparar_preco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.txt_comparar_preco)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.bt_pesquisa_massiva = QPushButton(self.frame_8)
        self.bt_pesquisa_massiva.setObjectName(u"bt_pesquisa_massiva")
        self.bt_pesquisa_massiva.setEnabled(True)
        sizePolicy.setHeightForWidth(self.bt_pesquisa_massiva.sizePolicy().hasHeightForWidth())
        self.bt_pesquisa_massiva.setSizePolicy(sizePolicy)
        self.bt_pesquisa_massiva.setMinimumSize(QSize(30, 42))
        self.bt_pesquisa_massiva.setMaximumSize(QSize(16777215, 40))
        self.bt_pesquisa_massiva.setFont(font2)
        self.bt_pesquisa_massiva.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pesquisa_massiva.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #81C784;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #66BB6A;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")

        self.horizontalLayout_7.addWidget(self.bt_pesquisa_massiva)

        self.bt_pesquisar = QPushButton(self.frame_8)
        self.bt_pesquisar.setObjectName(u"bt_pesquisar")
        sizePolicy.setHeightForWidth(self.bt_pesquisar.sizePolicy().hasHeightForWidth())
        self.bt_pesquisar.setSizePolicy(sizePolicy)
        self.bt_pesquisar.setMinimumSize(QSize(30, 42))
        self.bt_pesquisar.setMaximumSize(QSize(16777215, 40))
        self.bt_pesquisar.setFont(font1)
        self.bt_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pesquisar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #81C784;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #66BB6A;\n"
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
        self.bt_limpar.setMinimumSize(QSize(30, 42))
        self.bt_limpar.setMaximumSize(QSize(16777215, 40))
        self.bt_limpar.setFont(font2)
        self.bt_limpar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_limpar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #000;\n"
"}\n"
"QPushButton{\n"
"	background-color: #EF5350;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #F44336;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")

        self.horizontalLayout_7.addWidget(self.bt_limpar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.bt_comparar_exportar = QPushButton(self.frame_8)
        self.bt_comparar_exportar.setObjectName(u"bt_comparar_exportar")
        self.bt_comparar_exportar.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.bt_comparar_exportar.sizePolicy().hasHeightForWidth())
        self.bt_comparar_exportar.setSizePolicy(sizePolicy4)
        self.bt_comparar_exportar.setMinimumSize(QSize(10, 42))
        self.bt_comparar_exportar.setMaximumSize(QSize(16777215, 40))
        self.bt_comparar_exportar.setFont(font2)
        self.bt_comparar_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_comparar_exportar.setStyleSheet(u"QPushButton:hover{\n"
"	/*background-color: #90a955;*/\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"}\n"
"QPushButton{\n"
"	background-color: #A5D6A7;\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	color: #fff;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: #81C784;\n"
"	border-radius: 15px;\n"
"	border-bottom: 1.5px solid gray;\n"
"	border-right: 1.5px solid gray;\n"
"	color: #000;\n"
"}")
        self.bt_comparar_exportar.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.bt_comparar_exportar)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(35, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: black; /* Cor do texto normal */\n"
"    font-weight: bold;\n"
"}")
        self.label_6.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_11.addWidget(self.label_6)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(7, 7, 7, 7)
        self.tb_concorrentes = QTableWidget(self.frame_9)
        self.tb_concorrentes.setObjectName(u"tb_concorrentes")
        self.tb_concorrentes.setMinimumSize(QSize(0, 0))
        self.tb_concorrentes.setMaximumSize(QSize(16777215, 16777215))
        self.tb_concorrentes.setStyleSheet(u"background: white;")

        self.verticalLayout_16.addWidget(self.tb_concorrentes)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.verticalLayout_14.setStretch(2, 1)

        self.horizontalLayout_8.addWidget(self.frame_7)

        self.Pages.addWidget(self.pg_comparar)
        self.pg_Sobre = QWidget()
        self.pg_Sobre.setObjectName(u"pg_Sobre")
        self.gridLayout = QGridLayout(self.pg_Sobre)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_10 = QFrame(self.pg_Sobre)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_6 = QSpacerItem(20, 255, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_12.addWidget(self.label_3)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_12.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setLayoutDirection(Qt.RightToLeft)
        self.label_9.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.bt_link = QPushButton(self.frame_10)
        self.bt_link.setObjectName(u"bt_link")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bt_link.sizePolicy().hasHeightForWidth())
        self.bt_link.setSizePolicy(sizePolicy5)
        font4 = QFont()
        font4.setFamilies([u"MS Shell Dlg 2"])
        font4.setPointSize(14)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(True)
        self.bt_link.setFont(font4)
        self.bt_link.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_link.setLayoutDirection(Qt.LeftToRight)
        self.bt_link.setStyleSheet(u"QPushButton{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	text-decoration: underline;\n"
"	color: blue;\n"
"	margin-left: -30px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icones/whatsApp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_link.setIcon(icon7)
        self.bt_link.setIconSize(QSize(100, 100))
        self.bt_link.setFlat(False)

        self.horizontalLayout_9.addWidget(self.bt_link)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_5 = QSpacerItem(20, 255, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)

        self.Pages.addWidget(self.pg_Sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.MainFrame)

        self.frame_5 = QFrame(self.ContainerPrincipal)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(True)
        self.label_2.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_12.addWidget(self.ContainerPrincipal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bt_menu2.setDefault(False)
        self.bt_home.setDefault(False)
        self.Pages.setCurrentIndex(2)
        self.bt_Cadastrar_2.setDefault(False)
        self.bt_alterar.setDefault(False)
        self.bt_pesquisar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.ContainerEsq.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>QPushButton:hover{</p><p>	background-color: rgb(172, 213, 241);</p><p>	border-top-left-radius: 8px;</p><p>	border-bottom-left-radius: 8px;</p><p>}</p><p>QPushButton:pressed{</p><p>	background-color: rgb(172, 213, 241);</p><p>	border-right: 1.5px solid gray;</p><p>	border-bottom: 1.5px solid gray;</p><p>	border-bottom-right-radius: 8px;</p><p>}</p><p><br/></p><p><br/></p><p>QPushButton{</p><p>	Color: rgb(0, 0, 0);</p><p>	text-align: left;</p><p>	padding: 5px;</p><p>}</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icones/Refriparts 1.png\"/></p><p><br/></p></body></html>", None))
        self.bt_menu2.setText(QCoreApplication.translate("MainWindow", u"   Menu", None))
        self.bt_home.setText(QCoreApplication.translate("MainWindow", u"   Inicio", None))
        self.bt_Cadastrar.setText(QCoreApplication.translate("MainWindow", u"   Cadastrar Produtos", None))
        self.bt_PesquisarProdutos.setText(QCoreApplication.translate("MainWindow", u"   Pesquisar produtos", None))
        self.bt_comparativo.setText(QCoreApplication.translate("MainWindow", u"   Comparar Valores", None))
        self.bt_Sobre.setText(QCoreApplication.translate("MainWindow", u"   Sobre", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Sistema de Cadastro</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.Logo.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.Logo.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/icones/Logo_Refriparts.webp\" /></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.Logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icones/Logo_Refriparts.webp\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Produtos</span></p></body></html>", None))
        self.txt_produto.setText("")
        self.txt_produto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do produto", None))
        self.txt_sku.setText("")
        self.txt_sku.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SKU", None))
        self.txt_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.txt_link.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Link", None))
        self.bt_Cadastrar_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.bt_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.bt_deletar.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
#if QT_CONFIG(tooltip)
        self.bt_exportar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Exportar para excel</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bt_exportar.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Comparativo de Valores</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Pesquisa de valores</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Pesquisa de valores</span></p></body></html>", None))
        self.txt_comparar_sku.setText("")
        self.txt_comparar_sku.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SKU", None))
        self.txt_comparar_preco.setText("")
        self.txt_comparar_preco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o", None))
        self.bt_pesquisa_massiva.setText(QCoreApplication.translate("MainWindow", u"Pesquisa completa", None))
        self.bt_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.bt_limpar.setText(QCoreApplication.translate("MainWindow", u"Limpar", None))
        self.bt_comparar_exportar.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pesquisando...</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u00a9 2023 Professional Wise to Code.</span></p><p align=\"center\"><span style=\" font-size:14pt;\">Todos os direitos reservados.</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Suporte</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Geovanne:</span></p></body></html>", None))
        self.bt_link.setText(QCoreApplication.translate("MainWindow", u"(11) 95284-2140", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Refriparts \u00a9 2023 PW2C todos os direitos reservados.</span></p></body></html>", None))
    # retranslateUi

