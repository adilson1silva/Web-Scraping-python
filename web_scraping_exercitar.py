"""
from selenium import webdriver
from bs4 import BeautifulSoup
#from selenium.webdriver.chrome.options import Options  
from time import sleep


chrome_options = Options()  
chrome_options.add_argument("--headless") 





navegador = webdriver.Chrome()
navegador.maximize_window()
sleep(2)

url = 'https://www.airbnb.com/'
page = navegador.get(url)
sleep(2)


place = navegador.find_element_by_xpath('//*[@id="bigsearch-query-location-input"]')
place.send_keys('Madrid')
sleep(2)
search_check_in = navegador.find_element_by_xpath('//*[@id="search-tabpanel"]/div/div[3]/div[1]/div/div').click()
sleep(2)
data_in = navegador.find_element_by_xpath('//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[2]/div/div/div').click()
sleep(2)
data_out = navegador.find_element_by_xpath('//*[@id="panel--tabs--0"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]/div/div/div').click()
sleep(2)
add_guest = navegador.find_element_by_xpath('//*[@id="search-tabpanel"]/div/div[5]/div[1]/div').click()
sleep(2)
add = navegador.find_element_by_xpath('//*[@id="stepper-adults"]/button[2]').click()
sleep(5)
search = navegador.find_element_by_xpath('//*[@id="search-tabpanel"]/div/div[5]/div[3]/button/span[1]/span').click()
sleep(4)



all_content = navegador.page_source

soup = BeautifulSoup(all_content, 'html.parser')

hospedagem = soup.find('div', attrs={'itemprop':'itemListElement'})
print(hospedagem.prettify())
nome_hospedagem = hospedagem.find('meta', attrs={'itemprop': 'name'})
print(nome_hospedagem['content'])

url_hospedagem = hospedagem.find('meta', attrs={'itemprop': 'url'})
print(url_hospedagem.prettify)

hospedagem_detalhes = hospedagem.find('div', attrs={'style': '--margin-bottom:var(--h-x-sf-jw);'}).next_element
print(hospedagem_detalhes.prettify())
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/stats/players/'

dados = requests.get(url)
print(dados)

soup = BeautifulSoup(dados.content, 'html.parser')
#print(soup.prettify())

# pegar a tabela 

dados_tab = soup.find('div', attrs={'class': 'nba-stat-table__overlay'}).contents
print(dados)
