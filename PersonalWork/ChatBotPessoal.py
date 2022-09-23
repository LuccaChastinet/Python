import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pessoa = "Amanda"
numero = "******"
mensagem = "Anti-baby"

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1: # Esperando o Whats-App conectar
  time.sleep(1)

# Já conectado, continua

link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}"


