# NESSE PROJETO VAMOS PUXAR AS INFORMAÇÕES DE UM SITE E ARMAZENA-LAS EM UM ARQ. .CSV !

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as ky
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)


navegador.get('https://www.gsuplementos.com.br/proteina')

try:
    time.sleep(5)

    main = WebDriverWait(navegador,10).until(
        EC.presence_of_element_located((By.TAG_NAME,'main'))
    )

    nome_produtos = []
    valor_produtos = []
    data = []

    local_nome_produto = main.find_elements(By.CLASS_NAME,'categoriaProdItem-nomeGrade')
    local_valor_produto = main.find_elements(By.CLASS_NAME,'flex-child-shrink')

    for produto in local_nome_produto:
        nome_prod = produto.find_element(By.TAG_NAME,'a')
        nome_produtos.append(nome_prod.text)

    for produto in local_valor_produto:
        valor_prod = produto.find_element(By.CLASS_NAME, 'vitrine-valor')
        valor_produtos.append(valor_prod.text)

    # ARMAZENANDO OS DADOS OBTIDOS

    file_name = "Base_de_dados.csv"
    header = ("Id","Nome_Produto","Preço",)
    
    for i in range(len(nome_produtos)):
    # Substituir o segundo índice pela string do nome do produto
        data.append((nome_produtos[i], valor_produtos[i]))

    def criar_arquivo(header,data,file_name):
        with open (file_name, "w", newline = "") as csvfile:
            movies = csv.writer(csvfile)
            movies.writerow(header)
            for data in data:
                movies.writerow(data)


    criar_arquivo(header, data, file_name)

    print('\033[32mPrograma finalizado!\033[0m')
    print('\033[32mA base de dados foi criada com sucesso!\033[0m')

finally:
    time.sleep(1.5)
    navegador.quit()
