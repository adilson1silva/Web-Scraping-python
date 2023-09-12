from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import re

count = 0

url = 'https://www.kabum.com.br/busca/livros-de-finan%C3%A7as'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
html_content = requests.get(url, headers=headers)
#print(html_content)


soup = BeautifulSoup(html_content.content, 'html.parser')

#----------------------------------------------------------------
#element = soup.find('div', id='listingCount').text.strip()
#espaço = element.find(' ')
#quant_product = element[:espaço]
#print(quant_product)

#------------------------------------------------------------
products = soup.find_all('div', class_= re.compile('productCard'))

for index, product in enumerate(products):
    name_product = product.find('h2').text.strip()
    metudo_pagamento = product.find('span', class_=re.compile('priceTextCard')).text.strip()
    botão_product = soup.find('div', class_= re.compile('productCard'))
    disponivel = botão_product.find('div', class_=re.compile('availableFooterCard')).text.strip()
    preço = product.find('span', class_=re.compile('priceCard')).text.strip()

    if '---' in preço:
        print(f'Produto {index + 1} não disponivel')
    else:

        with open(f'dadoss/{index + 1}.txt', 'w') as f:
            f.write(f'Nome: {name_product}\n')
            f.write(f'Preço: {preço}\n')
            f.write(f'Metudo de pagamento: {metudo_pagamento}\n')
            f.write(f'Disponível: {disponivel}\n')
            print('='*50)
            print(f'ficheiro {index + 1} foi salvo com sucesso!')
            count += 1
print(f'foram registados {count} livros disponiveis')
    


