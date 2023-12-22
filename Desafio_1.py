"""
Description:
This is an automation challenge with Python (selenium) and also webscraping (BeautifulSoup).
The challenge contains a few points to complete: 
 - enter the website "https://www.leyaonline.com/pt/"
 - Search for "Jorge"
 - Check that the book "O Triunfo dos Porcos" appears in the list.
 - Confirm that the description of the book contains the words "Quinta Manor".

Return: 
 Answers with the correct information from the challenge.

Code created by:
Adilson Silva
"""

#Importar bibliotecas 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from time import sleep

#Listas
lista_titulo = []
lista_descrição = []

#Variaveis
titilo_procurado = 'O Triunfo dos Porcos'
frase = 'Quinta Manor'
nome_do_autor = 'George'


# Abrir o Browser (Chrome)
drive = webdriver.Chrome()
url = 'https://www.leyaonline.com/pt/'
drive.get(url)
drive.maximize_window()

#Aceitar os termos 
aceitar = drive.find_element(By.XPATH, '//*[@id="cookiescript_accept"]').click()

#Encontrar o elemento da barra de pesquisa e pesquisar por "George"
search = drive.find_element(By.XPATH, '//*[@id="searchbar-large"]')
search.click()
search.send_keys(nome_do_autor)
sleep(5)
search.send_keys(Keys.ENTER)
sleep(5)

#Procurar pelo título "O Triunfo dos Porcos"
nova_url = drive.current_url
res = requests.get(nova_url)
soup = BeautifulSoup(res.text, 'html.parser')

#Adicionar todos os títulos presentes dentro e uma lista 
titulos = soup.find_all('h6', class_ = 'book-title')

for index, titulo in enumerate(titulos):
    lista_titulo.append(titulo.text.strip())

#Procurar o título na lista
if titilo_procurado in lista_titulo:
    print(f'\033[32m------------Encontrei o titúlo desejado -  "{titilo_procurado}"--------------\033[m')

    #Fazer a pesquisa do Ebook desejado
    search = drive.find_element(By.XPATH, '//*[@id="searchbar-large"]')
    search.click()
    search.send_keys(titilo_procurado)
    sleep(5)
    search.send_keys(Keys.ENTER)
    sleep(2)
    abrir_O_T_D_P  = drive.find_element(By.XPATH, '//*[@id="bookcard_83457"]/a[1]/div[1]/div/img').click()
    sleep(5)
else:
    print(f'\033[31m------------Não encontrei o titúlo desejado -  "{titilo_procurado}"--------------\033[m')

nova_url = drive.current_url
res = requests.get(nova_url)
soup = BeautifulSoup(res.text, 'html.parser')
descricão = soup.find('div', class_ = 'margin-bottom-2')
lista_descrição.append(descricão.text.strip().lower())

#print(lista_descrição)
for c in lista_descrição:
    if frase.lower() in c:
        print(f'\033[32m------------Encontrei "{frase}" na descrição--------------\033[m')
    else:
        print(f'\033[31m------------Não encontrei "{frase}" na descrição\033--------------[m')
print(f'Obrigado! Volte Sempre.')