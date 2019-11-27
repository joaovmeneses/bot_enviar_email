# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from gtts import gTTS
from playsound import playsound
import csv

# [*] Objetivo :
# Recebe uma lista com emails, uma com as senhas e n paginas
# Faz o levantamento de todos os emails do inbox
# Gravando todos os emails em um csv para usos posteriores
# Após isso, abre esse csv, retira as duplicatas 
# E começa a função de enviar o email de propaganda
# Para TODOS os emails da lista

def fazerLogin(login, senha):
    url = "http://webmail.omnicontract.kinghost.net"
    browser = webdriver.Firefox()
    browser.get(url)

    #setar email e senha nos inputs
    browser.find_element_by_id("login_username").send_keys(str(login))
    browser.find_element_by_id("secretkey").send_keys(str(senha))
    browser.find_element_by_id("submit").click()
    return browser

def getRemetentes(browser ,pages):

    emails = []

    for i in range(pages):
        
        print("PÁGINA " + str(i))
        time.sleep(2)
        #pegar código fonte da página atual
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        #Pegar remetente
        remetentes = soup.select(".rcmContactAddress")
        for r in remetentes:
            print("[*]Remetente: " + r.get("title"))
            print("--------------------------------------------------------------")
            emails.append(r.get("title"))
        #clicar no botão para a prox página
        browser.find_element_by_id("rcmbtn129").click()
        time.sleep(6)
    
    return emails

def logout(browser):
    browser.find_element_by_id("rcmbtn101").click()

def criarCSV(lista):
    l = tirarDuplicatas(lista)
    c = csv.writer(open("emails_crn.csv", "wb"))
    for remetente in l:
        c.writerow([remetente])

def tirarDuplicatas(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def clickCriarEmail(browser):
    browser.find_element_by_id().click()

logins = ['joao.victor']
senhas = ['victor.joao']
send_email = ['','']
#pages = [35]
# /\ habilitar após teste com a crnbio
for l, s in zip(logins, senhas):
    #Entrar no site
    browser = fazerLogin(l, s)
    remetentes = getRemetentes(browser, 35)
    criarCSV(remetentes)
    logout(browser)

browser = fazerLogin(send_email[0], send_email[1])
