from data.dataBase import Database

class FuncaoAux:
    def __init__(self) -> None:
        pass

    def cadastro_pesquisado(self, dados:tuple):
        db = Database()
        sql = """
        INSERT INTO tb_prod_pesquisados(
        id,
        nome_do_produto,
        produto_pesquisado, 
        loja_pesquisado,
        preco_pesquisado,
        link_pesquisado,
        Link_Curto
        ) VALUES(?,?,?,?,?,?,?)"""

        db.insert_dados(sql, [dados])

        db.adicionar_links()