from tkinter import *
import tkinter.messagebox
import math

class Infix:
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

raiz_de = Infix(lambda x,y : x**(1.0/y))

janela = Tk()
janela.title("Calculadora em Python")
texto = Label(master=janela,text= "Feito por Lucca Maia Chastinet",bg="purple3")
texto.pack(side = BOTTOM,expand=True,fill=BOTH)
frame = Frame(master=janela,bg= "purple3",padx=5)
frame.pack(side=LEFT,expand=True,fill=BOTH)
entrada = Entry(master=frame,relief=SUNKEN, borderwidth=3,width= 30)
entrada.grid(row=0,column=0,columnspan=3,padx=2,ipady=6,pady=2)
cientifica = Frame(master=janela,bg="purple3",padx=10)
expandiu = False
memoria = ""

def click(num):
  entrada.insert(END,num)

def igual():
  try:
    y=str(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,y)
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def limpar():
  entrada.delete(0,END)

def porcentagem():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(y/100))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def expandir():
  global expandiu
  if expandiu == False:
    cientifica.pack(side=LEFT,expand=True,fill=BOTH)
    expandiu = True
  else:
    cientifica.pack_forget()
    expandiu = False

def potenciacao_2():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(y**2))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def raiz_2():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.sqrt(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def sin():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.sin(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def cos():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.cos(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def tan():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.tan(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def sinh():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.sinh(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def cosh():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.cosh(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def tanh():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.tanh(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def log():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.log(y,10)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def ln():
  try:
    y=float(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.log(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def fatorial():
  try:
    y=int(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(math.factorial(y)))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def M_plus():
  try:
    global memoria
    memoria = float(eval(entrada.get()))
  except:
    tkinter.messagebox.showinfo("Error","Caixa vazia")

def MRC():
  try:
    global memoria
    entrada.delete(0,END)
    entrada.insert(0,memoria)
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

def apagar_memoria():
    global memoria
    memoria = ""

def M_minus():
  try:
    global memoria
    minus = float(eval(entrada.get()))
    memoria = memoria-minus
  except:
    tkinter.messagebox.showinfo("Error","Caixa vazia/Memória não existe")

# Números

botao1 = Button(master=frame,text="1",padx=15,pady=5,width=3,command=lambda:click(1))
botao1.grid(row=2, column=0,pady=2)
botao2 = Button(master=frame,text="2",padx=15,pady=5,width=3,command=lambda:click(2))
botao2.grid(row=2, column=1,pady=2)
botao3 = Button(master=frame,text="3",padx=15,pady=5,width=3,command=lambda:click(3))
botao3.grid(row=2, column=2,pady=2)
botao4 = Button(master=frame,text="4",padx=15,pady=5,width=3,command=lambda:click(4))
botao4.grid(row=3, column=0,pady=2)
botao5 = Button(master=frame,text="5",padx=15,pady=5,width=3,command=lambda:click(5))
botao5.grid(row=3, column=1,pady=2)
botao6 = Button(master=frame,text="6",padx=15,pady=5,width=3,command=lambda:click(6))
botao6.grid(row=3, column=2,pady=2)
botao7 = Button(master=frame,text="7",padx=15,pady=5,width=3,command=lambda:click(7))
botao7.grid(row=4, column=0,pady=2)
botao8 = Button(master=frame,text="8",padx=15,pady=5,width=3,command=lambda:click(8))
botao8.grid(row=4, column=1,pady=2)
botao9 = Button(master=frame,text="9",padx=15,pady=5,width=3,command=lambda:click(9))
botao9.grid(row=4, column=2,pady=2)
botao0 = Button(master=frame,text="0",padx=15,pady=5,width=3,command=lambda:click(0))
botao0.grid(row=5, column=1,pady=2)

# Operações

botao_soma = Button(master=frame, text="+",padx=15,pady=5,width=3,command=lambda: click('+'))
botao_soma.grid(row=4,column=3,pady=2)
botao_sub = Button(master=frame, text="-",padx=15,pady=5,width=3,command=lambda: click('-'))
botao_sub.grid(row=3,column=3,pady=2)
botao_mult = Button(master=frame, text="*",padx=15,pady=5,width=3,command=lambda: click('*'))
botao_mult.grid(row=2,column=3,pady=2)
botao_div = Button(master=frame, text="/",padx=15,pady=5,width=3,command=lambda: click('/'))
botao_div.grid(row=1,column=3,pady=2)
botao_porcentagem = Button(master=frame, text="%",padx=15,pady=5,width=3,command=porcentagem)
botao_porcentagem.grid(row=1,column=2,pady=2)
botao_ao_2 = Button(master=cientifica,text="x²",padx=15,pady=5,width=3,command=potenciacao_2)
botao_ao_2.grid(row=1,column=0,pady=2)
botao_ao_x = Button(master=cientifica,text="x*",padx=15,pady=5,width=3,command=lambda: click('**'))
botao_ao_x.grid(row=1,column=1,pady=2)
botao_raiz_2 = Button(master=cientifica,text="²√",padx=15,pady=5,width=3,command=raiz_2)
botao_raiz_2.grid(row=2,column=0,pady=2)
botao_raiz_x = Button(master=cientifica,text="*√",padx=15,pady=5,width=3,command=lambda: click(' |raiz_de| '))
botao_raiz_x.grid(row=2,column=1,pady=2)
botao_sin = Button(master=cientifica,text="Sin",padx=15,pady=5,width=3,command=sin)
botao_sin.grid(row=3,column=0,pady=2)
botao_cos = Button(master=cientifica,text="Cos",padx=15,pady=5,width=3,command=cos)
botao_cos.grid(row=3,column=1,pady=2)
botao_tan = Button(master=cientifica,text="Tan",padx=15,pady=5,width=3,command=tan)
botao_tan.grid(row=3,column=2,pady=2)
botao_sinh = Button(master=cientifica,text="Sinh",padx=15,pady=5,width=3,command=sinh)
botao_sinh.grid(row=4,column=0,pady=2)
botao_cosh = Button(master=cientifica,text="Cosh",padx=15,pady=5,width=3,command=cosh)
botao_cosh.grid(row=4,column=1,pady=2)
botao_tanh = Button(master=cientifica,text="Tanh",padx=15,pady=5,width=3,command=tanh)
botao_tanh.grid(row=4,column=2,pady=2)
botao_log = Button(master=cientifica,text="Log",padx=15,pady=5,width=3,command=log)
botao_log.grid(row=0,column=2,pady=2)
botao_ln = Button(master=cientifica,text="ln",padx=15,pady=5,width=3,command=ln)
botao_ln.grid(row=1,column=2,pady=2)
botao_fatorial = Button(master=cientifica,text="x!",padx=15,pady=5,width=3,command=fatorial)
botao_fatorial.grid(row=2,column=2,pady=2)


# Utilidades e símbolos

botao_limpar = Button(master=frame, text="Limpar",padx=15,pady=5,width=12,command=limpar)
botao_limpar.grid(row=1,column=0,columnspan=2,pady=2)
botao_igual = Button(master=frame, text="=",padx=15,pady=5,width=3,command=igual)
botao_igual.grid(row=5,column=3,columnspan=1,pady=2)
botao_ponto = Button(master=frame,text=".",padx=15,pady=5,width=3,command=lambda:click('.'))
botao_ponto.grid(row=5,column=2,pady=2)
botao_parenteses_1 = Button(master=cientifica,text="(",padx=15,pady=5,width=3,command=lambda: click('('))
botao_parenteses_1.grid(row=0,column=0,pady=2)
botao_parenteses_2 = Button(master=cientifica,text=")",padx=15,pady=5,width=3,command=lambda: click(')'))
botao_parenteses_2.grid(row=0,column=1,pady=2)
botao_expandir = Button(master=frame, text="Expandir",padx=15,pady=5,width=3,command=expandir)
botao_expandir.grid(row=5,column=0,pady=2)
botao_M_plus = Button(master=cientifica, text="M+",padx=15,pady=5,width=3,command=M_plus)
botao_M_plus.grid(row=6,column=1,pady=2)
botao_M_minus = Button(master=cientifica, text="M-",padx=15,pady=5,width=3,command=M_minus)
botao_M_minus.grid(row=6,column=2,pady=2)
botao_MRC = Button(master=cientifica, text="MRC",padx=15,pady=5,width=3,command=MRC)
botao_MRC.grid(row=6,column=0,pady=2)
botao_apaga_memoria = Button(master=cientifica, text="Apagar Memória",padx=15,pady=5,width=12,command=apagar_memoria)
botao_apaga_memoria.grid(row=7,column=0,columnspan=3,pady=2)
botao_pi = Button(master=frame, text="π",padx=15,pady=5,width=3,command=lambda: click(math.pi))
botao_pi.grid(row=0,column=3,padx=2,pady=2)

janela.mainloop()