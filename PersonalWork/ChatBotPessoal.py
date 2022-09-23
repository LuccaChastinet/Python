import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib 
import time
enviado = False
while True:
  tempo = time.ctime()
  tempo = tempo.split()
  horario = tempo[3]
  
  if horario[0:2] == "05" and enviado == False:
    
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:9222")
    numero = "**********"
    mensagem = urllib.parse.quote("********")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador = webdriver.Chrome(chrome_options=opt)

    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side")) < 1: # Esperando o Whats-App conectar
      time.sleep(1)

  #while len(navegador.find_element(By.XPATH,"x")) < 1:
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)
  #time.sleep(300)
    enviado = True
  else:
    if enviado == True:
      time.sleep(86400)
      enviado = False
    
    

