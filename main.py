from PySide6 import QtCore
# from PySide6.QtCore import Slot
from PySide6.QtCore import Qt, QUrl, QSize, QTimer,QEvent, Slot, Signal
from PySide6.QtGui import QIcon, QDesktopServices, QCursor, QBrush, QColor, QPalette
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QStyledItemDelegate, QTableWidgetItem, QHeaderView, QMessageBox, QTableView, QLabel)
from src.tableModel.table_model import ConstrucaoModeloTabela
from src.pesquisa_produtos import PesquisaPrecos
from tkinter.filedialog import askdirectory
from data.dataBase import Database
from cadastro import Ui_MainWindow
import pandas as pd
import webbrowser
import sys
import threading

class LinkDelegate(QStyledItemDelegate):

    def editorEvent(self, event, model, option, index):
        if event.type() == QEvent.MouseButtonRelease:
            # Pega o link associado ao preço
            link = model.data(index, Qt.DisplayRole)

            if link:
                db = Database()
                link_pesquisado = db.obter_link_pesquisado_por_link_curto(link)
                QDesktopServices.openUrl(QUrl(link_pesquisado))
                return True
        return super().editorEvent(event, model, option, index)

    def paint(self, painter, option, index):
        valor_cadastrado = index.model().data(index.model().index(index.row(), 1), Qt.DisplayRole)
        valor_concorrente = index.model().data(index.model().index(index.row(), 3), Qt.DisplayRole)

        if valor_cadastrado is not None and valor_concorrente is not None:
            valor_cadastrado = self.parse_valor(valor_cadastrado)
            valor_concorrente = self.parse_valor(valor_concorrente)

            diferenca = valor_cadastrado - valor_concorrente
            10 - 20
            option.displayAlignment = Qt.AlignCenter | Qt.AlignVCenter

            red_brush = QBrush(QColor(213, 0, 0))
            green_brush = QBrush(QColor(0, 180, 125))

            if index.column() == 1 and diferenca < 0:
                option.palette.setBrush(QPalette.Text, green_brush)
            
            if index.column() == 1 and diferenca > 0:
                option.palette.setBrush(QPalette.Text, red_brush)

            if index.column() == 3 and diferenca > 0:
                option.palette.setBrush(QPalette.Text, green_brush)
            
            if index.column() == 3 and diferenca < 0:
                option.palette.setBrush(QPalette.Text, red_brush)

        super().paint(painter, option, index)

    def parse_valor(self, valor_str):
        try:
            valor_limpo = ''.join(c for c in valor_str if c.isdigit() or c in '.')
            return float(valor_limpo)
        except ValueError:
            return None
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.empresa = "Refriparts"
        self.setWindowTitle("Sistema de Cadastro")
        appIcon = QIcon(u"icones\Refriparts_icon.png")
        self.setWindowIcon(appIcon)
        self.ContainerEsq.enterEvent = self.MenuEsq
        self.ContainerEsq.leaveEvent = self.MenuEsq
        self.label_loading = self.findChild(QLabel, "label_6")

        
        self.label_loading.hide()
        
        #   Botão menu
        # self.bt_menu2.clicked.connect(self.MenuEsq)
        self.bt_Cadastrar_2.clicked.connect(self.cadastro)
        self.bt_alterar.clicked.connect(self.atualizar_dados)
        self.bt_deletar.clicked.connect(self.deletar_produto)
        self.bt_limpar.clicked.connect(self.limpa_campos)
        self.carregar_valores_cad()        
        self.bt_pesquisar.clicked.connect(lambda:self.start_automation(self.pesquisar_valores))
        # self.comboBox.currentIndexChanged.connect(self.preencher_dados_comparar)
        self.comboBox.currentIndexChanged.connect(self.carregar_dados_pesquisados)
        self.tb_concorrentes.doubleClicked.connect(self.openWebPage)
        self.tb_concorrentes.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setEditable(True)
        centralizar = self.comboBox.lineEdit()
        centralizar.setAlignment(Qt.AlignCenter)            
        self.bt_exportar.clicked.connect(self.exportar_excel)
        self.bt_comparar_exportar.clicked.connect(self.gerar_excel)
        self.bt_link.clicked.connect(self.abrir_wpp)
        self.bt_pesquisa_massiva.clicked.connect(lambda:self.start_automation(self.pesquisa_massiva))

        # Definir um estilo CSS para centralizar o texto
        
        # =============== METODOS DE INICIALIZAÇÃO ===================
        self.carregar_dados_produtos()
        self.variaveis_sistema()
        self.tb_produtos.doubleClicked.connect(self.pegar_dados_linha_produto)
        
        #   Página do sistema
        self.bt_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home)) # /Home
        self.bt_Cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Cadastrar)) # /Cadastrar
        self.bt_PesquisarProdutos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_comparar)) #/Comparar Valores
        # self.bt_comparativo.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_comparativo)) #/Comparar Valores
        self.bt_Sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_Sobre)) # /Sobre
        self.Pages.setCurrentIndex(0)

        # Criar botão para rodar o thread, onde ativa a pesquisa dos valores
        # self.button = QPushButton("Iniciar Automação", self)
        # self.button.setGeometry(150, 80, 120, 40)
        # self.button.clicked.connect(self.start_automation)

    @Slot()
    def on_bt_comparativo_clicked(self):
        self.Pages.setCurrentWidget(self.pg_comparativo)
        self.carrega_df()
        self.formata_tabela_comparativo()

    def MenuEsq(self, event):
        
        width = self.ContainerEsq.width()
        iconeMenu = QIcon(r"icones\menu.png")

        if width == 47:
            NovoWidth = 200
            self.bt_menu2.setIcon(QIcon(r"icones\x.png"))
            self.bt_menu2.setIconSize(QSize(25,25))
        else:
            NovoWidth = 47
            self.bt_menu2.setIcon(QIcon(iconeMenu))
            self.bt_menu2.setIconSize(QSize(25, 25))

        self.animation = QtCore.QPropertyAnimation(self.ContainerEsq, b"maximumWidth")
        self.animation.setDuration(550)
        self.animation.setStartValue(width)
        self.animation.setEndValue(NovoWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def variaveis_sistema(self):
        self.id_produto = ''
        self.dados: list = []
        self.select_produtos = pd.DataFrame()
        self.resultado = pd.DataFrame()

    def cadastro(self):
        db = Database()
        sql = """
        INSERT INTO tb_produtos(
        id,
        nome_do_produto, 
        sku,
        preco,
        link,
        imagem
        ) VALUES(?,?,?,?,?,?)"""

        db.insert_dados(sql, [(
        None, 
        self.txt_produto.text(),
        self.txt_sku.text(),
        self.txt_preco.text(),
        self.txt_link.text(),
        "texto_imagem"
        )])
        self.carregar_dados_produtos()
        self.reseta_campos()
        self.carregar_valores_cad()

    def deletar_produto(self, tabela):
        """remove produto da lista"""
        if tabela:
            labelText = self.comboBox.currentText()
        else:
            labelText = self.txt_produto.text()
            tabela = 'tb_produtos'
        try:
            if tabela:
                bd = Database()
                sql = f"""DELETE FROM {tabela} WHERE nome_do_produto = '{labelText}'"""
                bd.delete_dados(sql)
                if tabela == 'tb_produtos':
                    self.carregar_dados_produtos()
                    self.reseta_campos()
                    self.carregar_valores_cad()      
        except Exception as e:
            raise Exception(F'Erro ao Deletar dados{e}')
        
    def atualizar_dados(self):
        """"""
        if self.id_produto:
            
            txt_produto = self.txt_produto.text()
            txt_sku = self.txt_sku.text()
            txt_preco = self.txt_preco.text()
            txt_link = self.txt_link.text()

            sql = f"""
                    UPDATE tb_produtos
                    SET
                        nome_do_produto = '{txt_produto}',
                        sku = '{txt_sku}',
                        preco = '{txt_preco}',
                        link = '{txt_link}',
                        imagem = '{'update imagem'}'
                    WHERE
                        id = {self.id_produto}
                  """
            bd = Database()
            bd.update_dados(sql)
            self.carregar_dados_produtos()
            self.reseta_campos()
            self.carregar_valores_cad()

    def carregar_dados_produtos(self):
        """carrega os dados de dentro do banco de dados"""
        try:
            bd = Database()
            sql = """SELECT * FROM tb_produtos"""
            df_base = pd.DataFrame(bd.select_dados(sql), columns=['ID','Descrição', 'Código','Valor','Url Produto','Link Imagem'])
            self.carregar_bd(df_base, self.tb_produtos)

        except Exception as e:
            raise Exception(F'Erro ao Carregar dados{e}')
        
    def carregar_valores_cad(self):
        """carrega os dados de  dentro do banco de dados"""
        try:
            bd = Database()
            sql = """SELECT * FROM tb_produtos"""
            df_base = pd.DataFrame(bd.select_dados(sql), columns=['ID','Descrição', 'Código','Valor','Url Produto','Link Imagem'])
            df_base.drop('ID', axis=1, inplace=True)
            descricao_dados = df_base['Descrição'].to_list()
            self.comboBox.clear()
            self.comboBox.addItems(descricao_dados)
            self.comboBox.setCurrentIndex(-1)

        except Exception as e:
            raise Exception(F'Erro ao Carregar dados{e}')
        
    def carregar_bd(self, df, table: QTableView):
        modelo = ConstrucaoModeloTabela(df)
        table.setModel(modelo)
        titulos = table.horizontalHeader()
        table.show()
        titulos.setSectionResizeMode(QHeaderView.Stretch)
        # oculta a coluna de id
        if table == self.tb_produtos: table.setColumnHidden(0, True)
        
    def carregar_dados_pesquisados(self):
        bd = Database()
        sql = f"""SELECT * FROM tb_prod_pesquisados WHERE nome_do_produto = '{self.comboBox.currentText()}'"""
        df_base = pd.DataFrame(bd.select_dados(sql), columns=['ID','Nome do Produto','Descrição', 'Código','Valor','Url Produto', 'Url'])
        self.preencher_dados_comparar(preencher=True)
        if not df_base.empty:
            df_base.drop('ID', axis=1, inplace=True)
            df_base.drop('Nome do Produto', axis=1, inplace=True)
            df_base.drop('Url Produto', axis=1, inplace=True)
            self.carregar_dados(df_base, self.tb_concorrentes)
        else:
            self.tb_concorrentes.setRowCount(0)
            self.tb_concorrentes.setColumnCount(0)

    def carregar_dados(self, df, table: QTableView):
        try:
            # Ordenar o DataFrame com base no valor
            coluna_temporaria = df[df.columns[2]].str.replace('R$', '').str.replace(',', '')
            df[df.columns[2]] = pd.to_numeric(coluna_temporaria, errors='coerce')
            df = df.sort_values(by=df.columns[2])

            df[df.columns[2]] = df[df.columns[2]].map('R$ {:,.2f}'.format)

            self.resultado = df
            # Configurar a tabela personalizada
            table.setRowCount(len(df.index))
            table.setColumnCount(len(df.columns))
            table.setHorizontalHeaderLabels(df.columns)

            # Encontre o valor da linha "refriparts" na terceira coluna
            refriparts_row = df[df.iloc[:, 1] == self.empresa]
            if not refriparts_row.empty:
                refriparts_valor_str = refriparts_row.iloc[0, 2]
                refriparts_valor = float(refriparts_valor_str.replace('R$', '').replace(',', '').strip())
            else:
                refriparts_valor = 0.0
 
            for row in range(len(df.index)):
                for col in range(len(df.columns)):
                    valor_str = df.iloc[row, col]
                    valor_str_refri = df.iloc[row, 1]
                    item = QTableWidgetItem(valor_str)

                    if col == 2:  # Coluna 2 (índice 2)
                        valor = float(valor_str.replace('R$', '').replace(',', '').strip())
                        if valor_str_refri == self.empresa:
                            icon = QIcon("icones/Refriparts.png")  # Substitua pelo seu caminho correto
                            item.setIcon(icon)
                        elif valor > refriparts_valor:
                            icon = QIcon("icones/Negativo2.png")  # Substitua pelo seu caminho correto
                            item.setIcon(icon)
                            item.setForeground(QBrush(QColor(183, 28, 28)))  # Vermelho
                        elif valor < refriparts_valor:
                            icon = QIcon("icones/Positivo2.png")  # Substitua pelo seu caminho correto
                            item.setIcon(icon)
                            item.setForeground(QBrush(QColor(0, 105, 92)))  # Verde
                        else:
                            icon = QIcon(r"icones\igual.png") # Substitua pelo seu caminho correto
                            item.setIcon(icon)
                            item.setForeground(QBrush(QColor(255, 111, 0)))   


                    table.setItem(row, col, item)

                    if col == 3 and valor_str_refri == self.empresa:
                        for c in range(table.columnCount()):
                            cell_item = table.item(row, c)
                            if cell_item:
                                font = cell_item.font()
                                font.setPointSize(font.pointSize() + 0)
                                cell_item.setFont(font)
                                cell_item.setBackground(QBrush(QColor(21, 101, 192)))
                                cell_item.setForeground(QBrush(Qt.white)) 

            #Coloquei para decidir se vai dar Stretch ou resize
            for col in range(4):
                if col in (0,1,2,3):
                    table.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)
                else:
                    table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        except Exception as e:
            print(f"Erro ao carregar dados: {str(e)}")

    def openWebPage(self, index):
            if index.column() == 3:
                url = index.data(Qt.DisplayRole)
                db = Database()
                link_pesquisado = db.obter_link_pesquisado_por_link_curto(url)
                QDesktopServices.openUrl(QUrl(link_pesquisado))

    def preencher_dados_comparar(self, preencher: bool = False):
        bd = Database()
        sql = f"""SELECT * FROM tb_produtos WHERE nome_do_produto = '{self.comboBox.currentText()}'"""
        df_base = pd.DataFrame(bd.select_dados(sql), columns=['ID','Descrição', 'Código','Valor','Url Produto','Link Imagem'])
        df_base.drop('ID', axis=1, inplace=True)
        if preencher:
            try:
                self.txt_comparar_sku.setText(df_base['Código'][0])
                self.txt_comparar_preco.setText(df_base['Valor'][0])
                # self.linkImagem = df_base['Link Imagem'][0]
            except:
                pass

    def pegar_dados_linha_produto(self, index):
        # Obtém as informações da linha correspondente ao índice clicado
        row = index.row()
        model = index.model()

        row_data = []
        self.id_produto = ''
        for col in range(model.columnCount()):
            cell_data = model.data(model.index(row, col), Qt.DisplayRole)
            row_data.append(cell_data)

        self.dados = row_data
        self.id_produto = row_data[0]
        self.txt_produto.setText(row_data[1])
        self.txt_sku.setText(row_data[2])        
        self.txt_preco.setText(row_data[3])     
        self.txt_link.setText(row_data[4]) 

    def reseta_campos(self):
        """limpa os campos"""
        self.id_produto = ''
        self.txt_produto.clear()
        self.txt_sku.clear()        
        self.txt_preco.clear()     
        self.txt_link.clear()

    def start_automation(self, funcao):
        self.bt_pesquisar.setEnabled(False)
        self.bt_limpar.setEnabled(False)
        self.bt_comparar_exportar.setEnabled(False)
        self.bt_pesquisa_massiva.setEnabled(False)
        
        self.label_loading.show()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Pesquisando")
        msg.setText("Aguarde enquanto a pesquisa está sendo realizada.")
        timer = QTimer()
        timer.timeout.connect(msg.accept)
        timer.start(5000)
        msg.exec()

        thread = threading.Thread(target=funcao)
        thread.start()

    def pesquisar_valores(self):
        labelEmpresa = self.empresa
        labelComboBox = self.comboBox.currentText()
        labelPreco = self.txt_comparar_preco.text()
        labelSku = self.txt_comparar_sku.text()
        tabela = "tb_prod_pesquisados"

        self.deletar_produto(tabela)
        
        automacao = PesquisaPrecos()
        automacao.carrega_pagina_web()
        self.resultado = automacao.buscar_valores(labelComboBox, "Unica")

        self.carregar_dados(self.resultado, self.tb_concorrentes)

        self.bt_pesquisar.setEnabled(True)
        self.bt_limpar.setEnabled(True)
        self.bt_comparar_exportar.setEnabled(True)
        self.bt_pesquisa_massiva.setEnabled(True)

        self.label_loading.hide()

    def pesquisa_massiva(self):
        bd = Database()
        sql = """SELECT nome_do_produto FROM tb_produtos"""
        df_base = pd.DataFrame(bd.select_dados(sql), columns=['Descrição'])

        automacao = PesquisaPrecos(pesquisa=False)

        # remove a listagem de produtos pequsados
        sql = """DELETE FROM tb_prod_pesquisados"""
        bd.delete_dados(sql)

        item_count = self.comboBox.count()
        self.call_count = 0 

        for produto in df_base['Descrição'].to_list():
            print(produto)
            self.call_count += 1  # Incrementa o contador
            self.label_6.setText(f"Pesquisando {self.call_count} / {item_count} produtos")
            QApplication.processEvents()
            self.label_6.setAlignment(Qt.AlignCenter)
            automacao.carrega_pagina_web()
            self.resultado = automacao.buscar_valores(produto, "Massiva")
         
        self.bt_pesquisar.setEnabled(True)
        self.bt_limpar.setEnabled(True)
        self.bt_comparar_exportar.setEnabled(True)
        self.bt_pesquisa_massiva.setEnabled(True)
        self.label_loading.hide()

    def limpa_campos(self):
        """limpa os campos"""
        self.comboBox.setCurrentIndex(-1)
        self.txt_comparar_preco.clear()
        self.txt_comparar_sku.clear()
        self.tb_concorrentes.setRowCount(0)
        self.tb_concorrentes.setColumnCount(0)

    def exportar_excel(self):
        arquivo = askdirectory()
        if arquivo:
            bd = Database()
            sql = """SELECT * FROM tb_produtos"""
            df_base = pd.DataFrame(bd.select_dados(sql), columns=['ID','Descrição', 'Código','Valor','Url Produto','Link Imagem'])
            df_base.drop('ID', axis=1, inplace=True)
            df_base.to_excel(arquivo + "\\Produtos.xlsx", sheet_name= 'Produtos', index=False)

        self.caixa_msg("Excel", "Exportação feita com sucesso.", QMessageBox.Information)

    def gerar_excel(self):   

        if not self.resultado.empty:
            arquivo = askdirectory()
            if arquivo: 
                self.resultado.to_excel(arquivo + "\\Concorrentes.xlsx", sheet_name= 'Concorrentes', index=False)
                self.caixa_msg("Excel", "Exportação feita com sucesso.", QMessageBox.Information)

    def abrir_wpp(self):
        try:
            link = 'https://wa.me/11952842140'
            webbrowser.open(link)
        except Exception as e:
            print(f"Erro ao carregar dados: {str(e)}")

    def carrega_df(self):
        try:
            bd = Database()
            sql = """
            SELECT p.nome_do_produto AS 'Produto cadastrado',
                p.preco AS 'Valor cadastrado',
                --p.link AS 'Url cadastro',
                cp.produto_pesquisado AS 'Produto Concorrente',
                cp.preco_pesquisado AS 'Valor concorrente',
                cp.link_Curto AS 'Url concorrente'
            FROM tb_produtos p
            INNER JOIN tb_prod_pesquisados cp ON p.nome_do_produto = cp.nome_do_produto;
            """
            df_base = pd.DataFrame(bd.select_dados(sql), columns=['Produto cadastrado','Valor cadastrado',
                                                                    'Produto Concorrente','Valor concorrente','Link Concorrente'])
            
            coluna_temporaria = df_base[df_base.columns[3]].str.replace('R$', '').str.replace(',', '')
            df_base[df_base.columns[1]] = pd.to_numeric(df_base[df_base.columns[1]], errors='coerce')
            df_base[df_base.columns[3]] = pd.to_numeric(coluna_temporaria, errors='coerce')
            idx_menor_valor = df_base.groupby('Produto cadastrado')['Valor concorrente'].idxmin()
            df_menor_valor = df_base.loc[idx_menor_valor]

            df_menor_valor[df_menor_valor.columns[1]] = df_menor_valor[df_menor_valor.columns[1]].map('R$ {:,.2f}'.format)
            df_menor_valor[df_menor_valor.columns[3]] = df_menor_valor[df_menor_valor.columns[3]].map('R$ {:,.2f}'.format)
            df_menor_valor.reset_index(drop=True, inplace=True)
            self.carregar_bd(df_menor_valor, self.tb_comparativo)
        except Exception as e:
            print(e)
            raise Exception('Erro ao carregar dados para comparação de preços')

    def formata_tabela_comparativo(self):
        self.tb_comparativo.setShowGrid(True)
        self.tb_comparativo.setItemDelegate(LinkDelegate())
        # self.tb_comparativo.

        for row in range(4):
            self.tb_comparativo.setRowHeight(row, 80)

        # for col in range(4):
        #     self.tb_comparativo.horizontalHeader().setSectionResizeMode(col, QHeaderView.ResizeToContents)
        for col in range(5):
            if col in (1,3):
                self.tb_comparativo.setColumnWidth(col, 50)
            else:
                self.tb_comparativo.setColumnWidth(col, 200)
    
    def caixa_msg(self,titulo: str, texto: str, icone: QMessageBox):
        """retorna uma mensagem para o usuario"""
        try:
            msg = QMessageBox()
            msg.setIcon(icone)
            msg.setWindowTitle(titulo)
            msg.setText(texto)
            msg.exec()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()