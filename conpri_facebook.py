from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep
import keyboard

num = randint(0, 1)
driver = webdriver.Chrome()


if num == 0 or num == 1:
    ulr = 'https://www.facebook.com/'
    page = driver.get(ulr)
    driver.maximize_window()
    sleep(2)

    for c in range(24):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    sleep(5)

    #email
    keyboard.press_and_release('tab')
    sleep(3)
    keyboard.write('email')



    sleep(2)
    #pass
    keyboard.press_and_release('tab')
    keyboard.write('pass')
    sleep(2)
    #enter
    entrar = driver.find_element(By.NAME, 'login').click()
    sleep(2)
    messenger_link = 'https://www.facebook.com/messages/t/'
    contato = 'AdilsonSilva'  # Substitua com o nome da pessoa que você deseja pesquisar
    driver.get(messenger_link + contato)
    sleep(5)

    for c in range(0, 3):
        keyboard.press_and_release('tab')
    keyboard.press_and_release('enter')
    

    messenger_link = 'https://www.messenger.com/t/'

    

    """
    https://www.messenger.com/t/tairinyciara    - Tairimy
    https://www.messenger.com/t/100055970653491 - Daniel
    https://www.messenger.com/t/100008159534755 - Vy
    https://www.messenger.com/t/100008740320256 - Nini
    https://www.messenger.com/t/100061426420649 - Mama
    https://www.messenger.com/t/100040261304523 - Niche
    """
    list_contact = ["https://www.messenger.com/t/tairinyciara", "https://www.messenger.com/t/100055970653491", "https://www.messenger.com/t/100008159534755"]

    count_contact = 0

    sleep(10)

    for contactar in range(0, len(list_contact)):
        contactar = driver.get(list_contact[count_contact])
        #Aceitar novos termos
        if count_contact == 0:
            for allow_all_cookies in range(24): 
                sleep(0.5)
                keyboard.press_and_release('tab')
            keyboard.press_and_release('enter')
        #-------------------------------------------
        # Continuar Com Adilson Silva
            sleep(10)
            keyboard.press_and_release('enter')
            keyboard.press_and_release('tab')
            sleep(2)
            keyboard.press_and_release('enter')
            sleep(10)
        contactar = driver.get(list_contact[count_contact])
        count_contact += 1
        mensagem = ["Bom dia, mode que bu sta, esta espera ma bu esta dreto, quel grande abraço", "Oi mode que bu esta, dja dura nu ca fala sdd bo, grande abraço"]
        num_mensagem = randint(0, 2)
        sleep(2)
        keyboard.write(mensagem[num_mensagem])
        sleep(2)
        keyboard.press_and_release('enter')
        sleep(15)           


