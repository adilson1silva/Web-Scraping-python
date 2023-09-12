from bs4 import BeautifulSoup
import requests

url = 'https://www.net-empregos.com/emprego-lisboa.asp'
html_content = requests.get(url).text
#print(html_content)

#-------------------------------------------------------------------------------
soup = BeautifulSoup(html_content, 'lxml')
elements = soup.find_all('div', class_= 'media-body align-self-center')
#print(elements)





print('-------------------------------------------------Ver Todas as ofertas ------------------------------------------------')
for index, element in enumerate(elements):
    elemtnt_name = element.h2.a.text.strip()
    datas_publi = element.find('div', class_='job-ad-item').ul
    more_information = element.div.a['href'].strip()

    with open(f'dados_tabela_emprego/{index}.txt', 'w') as f:
        f.write(f'Nome do emprego: {elemtnt_name}\n')
        for a in datas_publi.find_all('li'):
            f.write(f'{a.text.strip()}\n')
        f.write(f'URL para mais informação: {more_information}\n')
    
        print('='*40)
        print(f'ficheiro {index} salvo com sucesso')
    


