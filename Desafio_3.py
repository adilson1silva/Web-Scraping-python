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
nome_ebook_2 = "A Quinta dos Animais"

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
####
####
####
####
####

search = drive.find_element(By.XPATH, '//*[@id="searchbar-large"]')
search.click()
search.send_keys(nome_ebook_2)
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
        print(f'\033[032mOs dois livros pertencem ao mesmo autor!\033[m')
        element_name = element.h6.text.strip()
        lista_titulo.append(element_name)
        link = element.get('href')
        descrição.append(link)
print(f'\033[032m{autor_ebook}\033[m')
print(f'\033[032m{lista_titulo}\033[m')
print(f'\033[032mVolte sempre\033[m')