#importar bibliotecas 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import re
from time import sleep


# Abrir o Browser (Chrome)
drive = webdriver.Chrome()
url = 'https://www.leyaonline.com/pt/livros/romance/1984/'
drive.get(url)
drive.maximize_window()
sleep(10)


# Listas
lista_titulo = []
autor_ebook = []
descrição = []
comprar = drive.find_element(By.XPATH, '//*[@id="pjax-container"]/section[1]/div/div[1]/div[2]/div/div[4]/div/div[2]/div/a').click()
nova_url = drive.current_url
res = requests.get(nova_url)
soup = BeautifulSoup(res.text, 'html.parser')



sleep(10)
elements = soup.find_all('a', class_ = 'add-to-cart  dropdown')
print(elements)
