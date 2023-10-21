from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
url = "https://www.linkedin.com/"
driver.get(url)
sleep(3)

driver.maximize_window
title = driver.title

if 'LinkedIn' in title:
    print(f'Foi confimado de que estamos dentro da app')
else:
    print('Não conseguiu entra na app, tente novamente')


email = driver.find_element(By.ID, 'session_key')
email.send_keys("kapacidade265@gmail.com")
sleep(2)

password = driver.find_element(By.ID, "session_password")
password.send_keys('kapacidade')
sleep(2)

into = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
into.send_keys(Keys.ENTER)
sleep(2)

#procurar três trabalho de python Por dia 

search_job = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
search_job.send_keys('Python Selenium')
search_job.send_keys(Keys.ENTER)
sleep(2)

vagas = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
vagas.click()
sleep(2)
print('Agora estas pronto para procuras as vagas de emprego de que pretendes')


