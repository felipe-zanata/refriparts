import os
import sqlite3 as slt
from tkinter import messagebox


class Database:

    def __init__(self) -> None:
        dir_data = os.path.join(os.getcwd(),'data\\')
        self.dbLocal = dir_data + 'dataBase.db'
        # self.dbLocal = r"C:\Users\2103896595\Desktop\arquivos\banco de dados\dataBase_mht.db"

    def connect_bd(self):
        """Estabelece conexão com o banco de dados"""
        self.conn = slt.connect(self.dbLocal)
        self.cursor = self.conn.cursor()

    def cria_tabelas(self):
        """cria serie de tabelas pré-definidas"""
        try:
            self.connect_bd()
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS tb_produtos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_do_produto   TEXT,
                sku       TEXT,
                preco     TEXT,
                link      TEXT,
                imagem   TEXT
            )""")

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS tb_prod_pesquisados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_do_produto      TEXT,
                produto_pesquisado   TEXT,
                loja_pesquisado      TEXT,
                preco_pesquisado     TEXT,
                link_pesquisado      TEXT,
                link_Curto           TEXT
            )""")

            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro Consulta', 'Não foi possivel Criar as tabelas.\n{}'.format(e))
        finally:
            self.conn.close()

    def insert_dados(self, string_sql, dados):
        """realiza a inserção de dados dentro do banco"""
        try:
            self.connect_bd()
            self.cursor.executemany(string_sql, dados)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro Consulta', 'Não foi possivel Inserir os dados.\n{}'.format(e))
        finally:
            self.conn.close()

    def update_dados(self, string_sql):
        """atualiza um registro dentro do banco de dados"""
        try:
            self.connect_bd()
            self.cursor.execute(string_sql)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro Consulta', 'Não foi possivel Atualizar os dados.\n{}'.format(e))
        finally:
            self.conn.close()

    def delete_dados(self, string_sql):
        """remove um registro dentro do banco de dados"""
        try:
            self.connect_bd()
            self.cursor.execute(string_sql)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro Consulta', 'Não foi possivel Deletar os dados.\n{}'.format(e))
        finally:
            self.conn.close()

    def select_dados(self, string_sql) -> list:  # type: ignore
        """seleciona os dados apartir de uma consulta"""
        try:
            self.connect_bd()
            self.cursor.execute(string_sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            messagebox.showerror('Erro Consulta', 'Não foi possivel Selecionar os dados.\n{}'.format(e))
        finally:
            self.conn.close()

    def adicionar_links(self):
        try:
            self.connect_bd()

            # sql_create_column = "ALTER TABLE tb_prod_pesquisados ADD COLUMN Link_Curto TEXT"
            # self.cursor.execute(sql_create_column)

            # sql_update_links = "UPDATE tb_prod_pesquisados SET Link_Curto = 'https://link-produto/' || Id"
            sql_update_links = """
                UPDATE tb_prod_pesquisados
                SET Link_Curto = CASE
                    WHEN Link_Curto IS NULL OR Link_Curto = '' THEN 'https://link-produto/' || Id
                    ELSE Link_Curto
                END
            """
            self.cursor.execute(sql_update_links)

            self.conn.commit()
        except Exception as e:
            messagebox.showerror('Erro ao adicionar links', 'Não foi possível adicionar os links.\n{}'.format(e))
        finally:
            self.conn.close()
        
    def obter_link_pesquisado_por_link_curto(self, link_curto):
        try:
            self.connect_bd()
            
            # Consulte o valor do campo "link_pesquisado" com base no "Link_Curto"
            sql = "SELECT link_pesquisado FROM tb_prod_pesquisados WHERE link_Curto = ?"
            self.cursor.execute(sql, (link_curto,))
            result = self.cursor.fetchone()

            if result:
                return result[0]  # Retorna o valor de "link_pesquisado"
            else:
                return None  # Se não for encontrado

        except Exception as e:
            messagebox.showerror('Erro na consulta', 'Não foi possível obter o link_pesquisado.\n{}'.format(e))
        finally:
            self.conn.close()

if __name__ == '__main__':
    data = Database()
    data.cria_tabelas()
    # data.insert_dados(f"INSERT INTO tb_filial VALUES(?,?,?, ?);", lista)