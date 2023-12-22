"""
Descrição do problema

- Entre no site "https://www.leyaonline.com/pt/"
- Procura pelo livro "1984"
- valida que o Autor é "George Orwell"
- Confirma que o ISBN é "9789722071550"
- Verifique que o ebook tem 344 páginas
- Certifica que o ebook tem as seguintes dimenção "235*157*23mm"
"""

#importar bibliotecas 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
from time import sleep

#dicionario
dados_completo = {}
# Listas
lista_titulo = []
autor_ebook = []
descrição = []

#Variaveis
nome_ebook = "1984"
nome_autor = "George Orwell"
isbn_desejado = '9789722071550'
paginas_desejadas = '344'

# Abrir o Browser (Chrome)
drive = webdriver.Chrome()
url = 'https://www.leyaonline.com/pt/'
drive.get(url)
drive.maximize_window()

#Aceitar os termos 
aceitar = drive.find_element(By.XPATH, '//*[@id="cookiescript_accept"]').click()

# encontrar o elemento da barra de pesquisa e pesquisar por "1984"
search = drive.find_element(By.XPATH, '//*[@id="searchbar-large"]')
search.click()
search.send_keys(nome_ebook)
sleep(5)
search.send_keys(Keys.ENTER)
sleep(5)


nova_url = drive.current_url
res = requests.get(nova_url)
soup = BeautifulSoup(res.text, 'html.parser')

elements = soup.find_all('a', class_ = 'second')

#print(elements)
for element in elements:
    element_author = element.find('div', class_ = 'book-author').text.strip()
    if element_author == 'GEORGE ORWELL':
        autor_ebook.append(element_author)
        element_name = element.h6.text.strip()
        lista_titulo.append(element_name)
        link = element.get('href')
        descrição.append(link)
print(f'\033[032m{autor_ebook}\033[m')
print(f'\033[032m{lista_titulo}\033[m')
print(f'\033[032m{descrição}\033[m')


#confirmar dados finais
lista_final  = []
for c in range(0, len(descrição)):
    print(f'\033[033m URL a ser analizada - {descrição[c]} \033[m')
    drive.get(descrição[c])
    sleep(5)
    res= requests.get(descrição[c])
    soup = BeautifulSoup(res.text, 'html.parser')
    detalhes = soup.find('div', class_ = '_sinpose-address').ul.text.strip()
    
    lista_final.append(detalhes)
    #print (f'\033[032m{lista_final}\033[m')

    padrao_isbn = r'ISBN: (\d+)'
    padrao_paginas = r'Páginas: (\d+)'

    # Variáveis para armazenar os resultados
    isbn_encontrado = None
    paginas_encontradas = None

    # Iterar sobre a lista e procurar os padrões
    for item in lista_final:
        match_isbn = re.search(padrao_isbn, item)
        match_paginas = re.search(padrao_paginas, item)

        if match_isbn:
            isbn_encontrado = match_isbn.group(1)

        if match_paginas:
            paginas_encontradas = match_paginas.group(1)

    # Comparar com os valores desejados
    if isbn_encontrado == isbn_desejado:
        print(f"\033[032mO ISBN encontrado: {isbn_encontrado} é igual ao ISBN desejado.\033[m")
    else:
        print(f"\033[031mO ISBN encontrado: {isbn_encontrado} é diferente ao ISBN desejado.\033[m")

    if paginas_encontradas == paginas_desejadas:
        print(f"\033[032mO número de páginas encontrado: {paginas_encontradas} é igual ao número de páginas desejado.\033[m")

        #Desafio 4
        comprar = drive.find_element(By.XPATH, '//*[@id="pjax-container"]/section[1]/div/div[1]/div[2]/div/div[4]/div/div[2]/div/a').click()
        #Confirm that the number of items in the basket is "1."
        sleep(10)
        new_page_source = drive.page_source
        soup = BeautifulSoup(new_page_source, 'html.parser')
        card = soup.find('div', 'header-content')
        final = card.find('div', class_ = 'add-to-cart dropdown').a
        valor_data_tag = final.get('data-tag')
        print("O número de livros que foi adicionado ao carinho:", valor_data_tag)
    else:
        print(f"\033[031mO número de páginas encontrado: {paginas_encontradas} é diferente ao número de páginas desejado.\033[m")

    
print('Volte sempre')
    
    
