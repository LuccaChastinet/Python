import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pessoa = "Amanda"
número = "******"
mensagem = "Anti-baby"

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

