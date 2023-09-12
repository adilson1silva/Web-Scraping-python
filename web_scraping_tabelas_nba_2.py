from bs4 import BeautifulSoup
import requests
import re

html_text = requests.get("https://www.nba.com/").text
with open(f'dados.html', 'w') as f:
    f.write(f'{html_text[:86865]}')

soup = BeautifulSoup(html_text, 'lxml')
elements = soup.find_all('div', class_='ArticleTile_tileMain__cXeUE')


for index, element in enumerate(elements):
    publi_data = element.find('div', class_ = 'ArticleTile_tileMeta__D6w6A').text
    if "hours" in publi_data:
        titulo = element.find('h3', class_='Text_text__I2GnQ ArticleTile_tileTitle__aA8g7').text
        resumo = element.find('p', class_ = 'Text_text__I2GnQ ArticleTile_tileSub__kiMA0').text
        more_info = element.div.a['href']

        with open(f'dados/{index}.txt', 'w') as f:
            f.write(f'Titulo: {titulo}\n')
            f.write(f'Resumo: {resumo}\n')
            f.write(f'Data de publicação: {publi_data}\n')
            f.write(f'Mais informação: {more_info}\n')    
                
        print(f'Ficheiro salvo: {index}')

