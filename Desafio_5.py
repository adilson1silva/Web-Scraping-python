from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = r"C:/Users/adimende/OneDrive - Capgemini/Documents/minhas pastas/VS Code/VS_Code/Web-Scraping-python/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

driver.get("https://www.leyaonline.com/pt/")

driver.implicitly_wait(5)

script = 'document.body.style.backgroundColor = "black";'
driver.execute_script(script)

driver.implicitly_wait(3)

input("Verifique visualmente o site. Pressione Enter para continuar.")
driver.quit()
