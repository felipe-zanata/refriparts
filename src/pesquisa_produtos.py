from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as condicaoEsperada
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from utils.auxiliar import FuncaoAux

class PesquisaPrecos:
    def __init__(self, pesquisa: bool = True) -> None:
        self.headless=pesquisa

        # self.produto = input(Fore.BLUE + 'Nome do Produto: ')
        self.tela_pesquisa = 'https://shopping.google.com/?nord=1'

    def carrega_pagina_web(self) -> None:
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if self.headless:
            options.add_argument("--headless")
        try:
            # service = Service(executable_path=r'src\chromedriver.exe')
            # self.driver = webdriver.Chrome(service=service, options=options)
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.wait = WebDriverWait(self.driver, 5)
            self.wait2 = WebDriverWait(self.driver, 120)
            self.wait3 = WebDriverWait(self.driver, 10800)
            self.driver.get(self.tela_pesquisa)
            self.driver.minimize_window()
        except Exception as e:
            print('Não foi possivel abrir a pagina web.')
            print(e)
            raise Exception(e)

    def buscar_valores(self, nome_do_produto: str, tipo: str): # nome_do_produto
        lNomeProduto: str = '//*[@class="tAxDx"]'
        lValor: str = '//*[@class="a8Pemb OFFNJ"]'
        lNomeLoja: str = '//*[@class="aULzUe IuHnof"]'
        lHref: str = '//*[@class="shntl"][1]'
        lPesquisarProduto: str = '//*[@class="r7gAOb yyJm8b"]'
        lEsperarCaptcha: str = '//*[@class="i0X6df"]'

        try:
            pesquisar_produto = self.wait2.until(
                condicaoEsperada.presence_of_element_located((By.XPATH, lPesquisarProduto)))
            pesquisar_produto.send_keys(nome_do_produto) # nome_do_produto
            pesquisar_produto.send_keys(Keys.ENTER)
            sleep(5)          
        except:
            print('Produto não encontrado.')

        while True:
            try:
                esperar_captcha = self.wait3.until(
                    condicaoEsperada.presence_of_element_located((By.XPATH, lEsperarCaptcha)))
                break
            except TimeoutException:
                continue

        try:
            nome_produto = self.driver.find_elements(By.XPATH, lNomeProduto)
        except:
            print('Não encontrou o nome do produto.')

        try:
            valor_items = self.driver.find_elements(By.XPATH, lValor)
        except:
            print('Não encontrou o preço do item.')          

        try:  
            nome_loja = self.driver.find_elements(By.XPATH, lNomeLoja)
        except:
            print('Não encontrou o nome da loja')

        try:
            href = self.driver.find_elements(By.XPATH, lHref)
        except:
            print('Não encontrou o HREF do produto')

        nome_produto_lista = []
        nome_loja_lista = []
        valor_items_lista = []
        href_lista = []

        # nome_produto_lista.append(nome_do_produto)
        # nome_loja_lista.append(empresa)
        # valor_items_lista.append(preco_formatado)
        # href_lista.append(link)

        aux = FuncaoAux()

        for produto_nome, loja_nome, items_valor, link in zip(nome_produto, nome_loja, valor_items, href):
            items_valor_convertido = items_valor.text.replace(",", "t").replace(".", ",").replace("t", ".") if tipo == "Massiva" else items_valor.text
            nome_produto_lista.append(produto_nome.text)
            nome_loja_lista.append(loja_nome.text)
            valor_items_lista.append(items_valor_convertido)
            href_lista.append(link.get_attribute('href'))
            
            # print(f'Produto: {produto_nome.text}\nValor:9 {items_valor.text}')      
            
            aux.cadastro_pesquisado(dados=(None, nome_do_produto, produto_nome.text, loja_nome.text, items_valor_convertido, link.get_attribute('href'), None))

        infos_coletadas = {
            'Produto': nome_produto_lista,  
            'Loja': nome_loja_lista,
            'Valor': valor_items_lista,
            'Links': href_lista
        }

        df_infos_coletadas = pd.DataFrame(infos_coletadas)
        # print(infos_coletadas)
        return df_infos_coletadas

if __name__ == '__main__':
    executa = PesquisaPrecos()
    executa.carrega_pagina_web()
    executa.buscar_valores()