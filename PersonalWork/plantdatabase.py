import csv
from tkinter import filedialog
import pandas as pd


arquivofeito = list()
nomedoarquivo = list()
cabeçalhos = list()

def nome_e_cabeçalhos(): # Pede o nome do arquivo e o número de cabeçalhos pra ser analisado 
  nomedoarquivo.append(input("Digite o nome do arquivo: ") + ".csv")
  numerodecabeçalhos = int(input("Digite o número de cabeçalhos: "))
  contador = 0
  while numerodecabeçalhos > contador: # Vê quantidade de cabeçalhos e o nome deles
    cabeçalho = input("Digite o cabeçalho " + str(contador+1) + ": ")
    cabeçalho = cabeçalho.title()
    cabeçalhos.append(cabeçalho)
    contador += 1
  

def cria_arquivo(): # Cria arquivo csv se necessário
  with open(nomedoarquivo[0],"w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=cabeçalhos)
    writer.writeheader()
  arquivofeito.append("Feito")
  print(type(nomedoarquivo[0]))
  introdução()

def escolhe_arquivo2(): # Escolhe o arquivo csv a ser usado
  x = filedialog.askopenfilename()  
  nomedoarquivo.append(x)
  arquivofeito.append("Feito")
  df = pd.read_csv(nomedoarquivo[0])
  lista = list(df.columns)
  for i in lista:
    cabeçalhos.append(i)
  introdução()


def adiciona_planta(): # Função que adiciona a planta e suas características
  planta = []
  atributos = []
  dicionario = {}
  numcabeçalhos = len(cabeçalhos)
  contador = 0
  while contador < numcabeçalhos:
    x = input("Escreva o/a " + cabeçalhos[contador].lower() + " da planta: ")
    x = x.title()
    atributos.append(x)
    dicionario.update({cabeçalhos[contador]: atributos[contador]})
    contador += 1
  planta.append(dicionario)
  with open(nomedoarquivo[0],"a") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=cabeçalhos)
    writer.writerows(planta)
  introdução()

def remove_planta(): # Função que remove a planta pelo seu nome
  plantaremovida = input("Digite o nome da planta a ser removida: ")
  plantaremovida = plantaremovida.title()
  contador = 0
  with open(nomedoarquivo[0],mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for planta in data:
      if planta["Nome"] == plantaremovida:
        planta.clear()
        data.pop(contador)
        with open(nomedoarquivo[0],mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cabeçalhos)
            writer.writeheader()
            writer.writerows(data)
      else:
        contador += 1
  introdução()

def mostra_banco(): # Função que mostra o banco de dados
  df = pd.read_csv(nomedoarquivo[0])
  print(" ")
  print(df)
  print(" ")
  introdução()


def introdução(): # Função que faz o usuário escolher as opções e navegar pelo programa
    print(" ")
    print ("Escolha a opção:")
    print(" ")
    if len(arquivofeito) == 0:
      print("1 - Criar banco de dados")
      print("2 - Escolher banco de dados")
      print("3 - Fechar programa ")
      print(" ")
      opcao = int(input())
      while opcao != 1 and opcao != 2 and opcao != 3:
        print("Digite uma opção válida")
        opcao = int(input())
      if opcao == 1:
        nome_e_cabeçalhos()
        cria_arquivo()
      if opcao == 2:
        escolhe_arquivo2()
      if opcao == 3:
        quit()
      

    else:
      print(" -- Banco de dados já criado/escolhido --")
      print("1 - Adicionar item ao banco de dados")
      print("2 - Remover item do banco de dados")
      print("3 - Exibir banco de dados")
      print("4 - Fechar programa ")
      opcao = int(input())
      while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print("Digite uma opção válida")
        opcao = int(input())
      if opcao == 1:
        adiciona_planta()
      if opcao == 2:
        remove_planta()
      if opcao == 3:
        mostra_banco()
      if opcao == 4:
        quit()

      
introdução()

