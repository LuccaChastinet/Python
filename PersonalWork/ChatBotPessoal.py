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
  
  if horario[0:2] == "21" and enviado == False: # Selecionar horário que quer enviar a mensagem
    
    opt=Options()
    opt.add_experimental_option("debuggerAddress","localhost:9222") # Foi utilizado isso para não abrir vários chromes, e sim reutilizar um só, evitando a necessidade de colocar o QR code do Whats-app todo dia
    numero = "INSIRA_NUMERO_DO_CELULAR" # Inserir número
    mensagem = urllib.parse.quote("INSIRA_MENSAGEM_A_SER_ENVIADA") # Inserir Mensagem
    link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"
    navegador = webdriver.Chrome(chrome_options=opt) # Abrir/Reutilizar navegador

    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side")) < 1: # Esperando o Whats-App conectar
      time.sleep(1)
    while len(navegador.find_elements(By.XPATH,"//*[contains(text(),'INSIRA_MENSAGEM_QUE_QUEIRA_DETECTAR_AQUI')]")) < 1: # Detectando pra ver se a mensagem de parada do alerta está na conversa
      navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER) # Enviando mensagem
      time.sleep(5)
      navegador.get(link)
      time.sleep(300)
    enviado = True
  else:
    if enviado == False:
      time.sleep(120) # Se não enviar(Não deu horário) esperar 2 minutos para não sobrecarregar e ficar infinitamente tentando ver se é o horário
    if enviado == True:
      navegador.get("https://web.whatsapp.com/") # Voltar pra página principal do Whats-app, e não ficar "Digitando..."
      tempoqueenviou = time.ctime()
      tempoqueenviou = tempoqueenviou.split()
      horarioqueenviou = tempo[3]
      minutos = horarioqueenviou[3:5] 
      segundos = int(minutos)*60
      time.sleep(86400-segundos) # Esperando 24 horas - a quantidade de minutos de atraso pra enviar
      enviado = False
    
    

