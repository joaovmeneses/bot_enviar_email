# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from gtts import gTTS
from playsound import playsound

def escrever_email(browser):

    #Mudar IFrame
    browser.switch_to_frame("composebody_ifr")

    #Corpo da Mensagem
    textbox = browser.find_element_by_xpath('/html/body/p')
    browser.execute_script('arguments[0].textContent = arguments[1]', textbox, 'Texto de teste')

    #Voltar para o primeiro Content
    browser.switch_to.default_content()



url = "http://webmail.omnicontract.kinghost.net"
browser = webdriver.Firefox()
browser.get(url)

#Setar email no input
browser.find_element_by_id('login_username').send_keys("joao.victor")

#Setar password no input
browser.find_element_by_id('secretkey').send_keys("victor.joao")

lista_emails = open("emails_consutec.csv")

#for ctt in lista_emails:
#    print(ctt)

#botão next
browser.find_element_by_id('submit').click()

time.sleep(5)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

#ir para "Criar Email"
browser.find_element_by_id('rcmbtn107').click()
time.sleep(3)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

#Remetentes
browser.find_element_by_id('_to').send_keys('joao.dvlp@gmail.com')

#Assunto
browser.find_element_by_id('compose-subject').send_keys('Assunto A')

escrever_email(browser)

time.sleep(2)

#Botão Enviar
browser.find_element_by_xpath('//*[@id="rcmbtn107"]').click()