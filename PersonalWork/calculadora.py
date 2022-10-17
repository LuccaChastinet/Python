from tkinter import *
import tkinter.messagebox

janela = Tk()
janela.title("Calculadora em Python")
frame = Frame(master=janela,bg= "purple3",padx=10)
frame.pack()
entrada = Entry(master=frame,relief=SUNKEN, borderwidth=3,width= 30)
entrada.grid(row=0,column=0,columnspan=3,ipady=2,pady=2)

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
    y=int(eval(entrada.get()))
    entrada.delete(0,END)
    entrada.insert(0,(y/100))
  except:
    tkinter.messagebox.showinfo("Error","Syntax Error")

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

botao_ponto = Button(master=frame,text=".",padx=15,pady=5,width=3,command=lambda:click('.'))
botao_ponto.grid(row=5,column=2,pady=2)

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

botao_limpar = Button(master=frame, text="Limpar",padx=15,pady=5,width=12,command=limpar)
botao_limpar.grid(row=1,column=0,columnspan=2,pady=2)
botao_igual = Button(master=frame, text="=",padx=15,pady=5,width=3,command=igual)
botao_igual.grid(row=5,column=3,columnspan=1,pady=2)


janela.mainloop()