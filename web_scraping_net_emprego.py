from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import pandas as pd

#------------------------------
html_content = requests.get("https://www.net-empregos.com/9423877/coordenador-de-area-m-f/?gclid=Cj0KCQjw8e-gBhD0ARIsAJiDsaVFZH5oMRHjDpn5O4NDdggC0pZbdOV_HykkdZVdXRzWoytBU-0aw0kaAlTUEALw_wcB").text
#print(html_content)

#-----------------------------------------------------

soup = BeautifulSoup(html_content, 'lxml')
elements = soup.find_all('div', class_='job-item media')

print('----'*20)

for element in elements:

    name_element = element.find('a', class_='oferta-link').text
    data_publication = element.find('div', class_='job-ad-item').text
    more_info = element.div.a['href']
    
    print(f'Nome: {name_element}')
    print(f'data: {data_publication}')
    print(f'URL para mais informação: {more_info}')
    print('----'*20)