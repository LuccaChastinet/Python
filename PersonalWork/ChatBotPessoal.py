import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib 
import time

enviado = False
while True: # Rodar Infinitamente
  tempo = time.ctime()
  tempo = tempo.split()
  horario = tempo[3] # Para saber que horas são no momento atual
  
  if horario[0:2] == "05" and enviado == False: # Selecionar horário que quer enviar a mensagem
    
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:9222") # Foi utilizado isso para não abrir vários chromes, e sim reutilizar um só, evitando a necessidade de colocar o QR code do Whats-app todo dia
    numero = "**********" # Inserir número
    mensagem = urllib.parse.quote("********") # Inserir Mensagem
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador = webdriver.Chrome(chrome_options=opt) # Abrir/Reutilizar navegador

    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side")) < 1: # Esperando o Whats-App conectar
      time.sleep(1)

  #----------------> while len(navegador.find_element(By.XPATH,"x")) < 1: <--------------- A SER ADICIONADO
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER) # Enviando mensagem
  #----------------> time.sleep(300) <--------------- A SER ADICIONADO
    enviado = True
  else:
    if enviado == True:
      time.sleep(86400) # Esperando 24 horas pra enviar
      enviado = False
    
    

