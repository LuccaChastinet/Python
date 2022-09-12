import csv
from tkinter import filedialog
import pandas as pd


arquivofeito = list() # Se tiver algo dentro da lista, o arquivo já foi feito ou escolhido
nomedoarquivo = list() # Para ter o nome do arquivo, primeiro e único elemento da lista é o nome do arquivo
cabeçalhos = list() # Lista de cabeçalhos

def nome_e_cabeçalhos(): # Para quando criado um novo banco de dados, saber o nome do arquivo e quantidade de cabeçalhos
  nomedoarquivo.append(input("Digite o nome do arquivo: ") + ".csv")
  numerodecabeçalhos = int(input("Digite o número de cabeçalhos: "))
  contador = 0
  while numerodecabeçalhos > contador: # Vê a quantidade de cabeçalhos para os dar nomes
    cabeçalho = input("Digite o cabeçalho " + str(contador+1) + ": ")
    cabeçalho = cabeçalho.title()
    cabeçalhos.append(cabeçalho)
    contador += 1
  

def cria_arquivo():
  with open(nomedoarquivo[0],"w") as csv_file: # Cria o arquivo 
    writer = csv.DictWriter(csv_file, fieldnames=cabeçalhos)
    writer.writeheader()
  arquivofeito.append("Feito") # Simboliza que o arquivo está feito
  introdução()
def escolhearquivo():
  x = filedialog.askopenfilename()  
  nomedoarquivo.append(x)
  arquivofeito.append("Feito") # Simboliza que o arquivo está escolhido
  df = pd.read_csv(nomedoarquivo[0])
  lista = list(df.columns) # Artifício para pegar o nome das colunas e adicionar a minha própria lista ("cabeçalhos")
  for i in lista:
    cabeçalhos.append(i)
  introdução()


def adiciona_planta(): # Função para adicionar uma planta ao banco de dados
  planta = []
  atributos = []
  dicionario = {}
  numcabeçalhos = len(cabeçalhos)
  contador = 0
  while contador < numcabeçalhos: # Adicionando cada característica da planta, utilizando os nomes dos cabeçalhos
    x = input("Escreva o/a " + cabeçalhos[contador].lower() + " da planta: ")
    x = x.title()
    atributos.append(x)
    dicionario.update({cabeçalhos[contador]: atributos[contador]}) # Fazendo a relação do cabeçalho com a característica da planta
    contador += 1
  planta.append(dicionario)
  with open(nomedoarquivo[0],"a") as by_department: # Abrir o arquivo para adicionar a planta em questão
    writer = csv.DictWriter(by_department, fieldnames=cabeçalhos)
    writer.writerows(planta)
  introdução()

def remove_planta(): # Função para remover uma planta
  plantaremovida = input("Digite o nome da planta a ser removida: ")
  plantaremovida = plantaremovida.title()
  contador = 0
  with open(nomedoarquivo[0],mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)
    for planta in data: # Procurando planta em questão
      if planta["Nome"] == plantaremovida: # Comparando nomes e se achar, remove-la
        planta.clear()
        data.pop(contador)
        with open(nomedoarquivo[0],mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cabeçalhos)
            writer.writeheader()
            writer.writerows(data)
      else:
        contador += 1
  introdução()

def mostra_banco(): # Função pra mostrar no console o banco de dados atual
  df = pd.read_csv(nomedoarquivo[0])
  print(" ")
  print(df)
  print(" ")
  introdução()


def introdução(): # Função para ter um menu inicial
    print(" ")
    print ("Escolha a opção:")
    print(" ")
    if len(arquivofeito) == 0: # Se o arquivo não foi feito/escolhido: 
      print("1 - Criar banco de dados")
      print("2 - Escolher banco de dados")
      print("3 - Fechar programa ")
      print(" ")
      opcao = int(input())
      while opcao != 1 and opcao != 2 and opcao != 3: # Checando para erro do usuário
        print("Digite uma opção válida") 
        opcao = int(input())
      if opcao == 1:
        nome_e_cabeçalhos()
        cria_arquivo()
      if opcao == 2:
        escolhearquivo()
      if opcao == 3:
        quit()
      

    else: # Se o arquivo já foi feito/escolhido: 
      print(" -- Banco de dados já criado/escolhido --")
      print("1 - Adicionar item ao banco de dados")
      print("2 - Remover item do banco de dados")
      print("3 - Exibir banco de dados")
      print("4 - Fechar programa ")
      opcao = int(input())
      while opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4: # Checando para erro do usuário
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

