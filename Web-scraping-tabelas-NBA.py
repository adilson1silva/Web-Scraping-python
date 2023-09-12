# 1. Pegar o conteúdo HTML a partir do URL
# 2. Parsear o conteúdo HTML - beautifulSoup
# 3. Estruturar conteúdos em um Data Frame - Pandas
# 4. Transformar os dados em um Dicionário de dados próprios
# 5. Converter e salvar em um arquivo JSON
#---------------------------------------------------------------

# Importar as bibliotecas
from cgitb import html
from ntpath import join
import time
from xml.dom.minidom import Element
import requests
import pandas as pd
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# 1. Pegar o conteúdo HTML a partir do URL
url = 'https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1'

option = Options
option.headless = True # fazer tudo em backgraund
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

#driver.find_element_by_xpath('//div[@class="nba-stat-table"]//table//thead//tr//th[@data-field="PTS"]').click()

Element = driver.find_element_by_xpath('//div[@class="nba-stat-table"]//table')
html_content = Element.get_attribute('outerHTML')
#print(html_content)

# 2. Parsear o conteúdo HTML - beautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar conteúdos em um Data Frame - Pandas

df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)

# 4. Transformar os dados em um Dicionário de dados próprios
top10ranking = {}
top10ranking['points'] = df.to_dict('records')

driver.quit()

# 5. Converter e salvar em um arquivo JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()

