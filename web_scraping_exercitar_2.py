from selenium import webdriver
from selenium.webdriver.common.keys import Keys # key  - serve para ter mais funcionalidades do teclado como RETURN, F1, ALT, ect.
from selenium.webdriver.common.by import By # - By serve para localizar elementos dentro de um documento 

driver = webdriver.Chrome()

driver.get("http://www.python.org") # driver.get - Serve para navegar até a página que queremos


assert "Python" in driver.title # esta linha serve para confirmar se "Python" é o titulo da página
                                
elem = driver.find_element(By.NAME, "q") # rpocurar elementos atraves de nomes

elem.clear() # antes de tudo começar a limpar, para ter uma garantia de que não vai ter dados para atrapalhar
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source # Para garantir que são encontrados alguns resultados, faça uma afirmação

driver.close() # fechar o browser

#---------------------------------------------------------------
#Encontrar um elemento dentro de uma pagina html

#    <input type="text" name="passwd" id="passwd-id" />

element = driver.find_element(By.ID, "passwd-id")
element = driver.find_element(By.NAME, "passwd")
element = driver.find_element(By.XPATH, "ver xpaph")
element  = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

# Portanto, tem um elemento. O que se pode fazer com ele? Antes de mais, pode querer introduzir algum texto num campo de texto:

element.send_keys("testo")

# Pode simular premir as teclas de setas utilizando a classe "Keys":

element.send_keys("and same", Keys.ARROW_DOWN)

#------------------------------------------------------------------
# Outra forma de chamar um elemento e escrever no campo de testo

element = driver.find_element(By.XPATH, "//select[@name='name']")
all_option = element.find_elements(By.TAG_NAME, "option")
for option in all_option:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()