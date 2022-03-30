import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados da função")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.funcaoLabel = Label(self.segundoContainer,text="Função", font=self.fontePadrao)
        self.funcaoLabel.pack(side=LEFT)

        self.funcao = Entry(self.segundoContainer)
        self.funcao["width"] = 30
        self.funcao["font"] = self.fontePadrao
        self.funcao.pack(side=LEFT)

        self.tolLabel = Label(self.terceiroContainer, text="Valor de Epsilon", font=self.fontePadrao)
        self.tolLabel.pack(side=LEFT)

        self.tol = Entry(self.terceiroContainer)
        self.tol["width"] = 30
        self.tol["font"] = self.fontePadrao
        self.tol.pack(side=LEFT)

        self.calcular = Button(self.quartoContainer)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        #self.calcular["command"] = self.verificaSenha
        self.calcular.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


root = Tk()
Application(root)
root.mainloop()


lista_raizes = list()
lista_intervalo = list()

##Método verificar senha
    #def verificaSenha(self):
    #    usuario = self.nome.get()
    #    senha = self.senha.get()
    #    if usuario == "usuariodevmedia" and senha == "dev":
    #        self.mensagem["text"] = "Autenticado"
    #    else:
    #        self.mensagem["text"] = "Erro na autenticação

def funcao(self):
    fun = self.funcaoLabe1.get()
    return fun

def epsilon(self):
    ep = self.tolLabe1.get()
    return ep

def met_bissec(inicial, final, precisao):
    iteracao = (np.log(final - inicial) - np.log(precisao)) / np.log(2)
    
    iteracao = np.ceil(iteracao)
    i = 0

    while i < iteracao:
        if funcao(inicial) * funcao(final) > 0:
            return False
        else:
            med = (inicial + final) / 2
            med = round(med, 6)
            
            if funcao(inicial) * funcao(med) < 0:
                final = med
            else:
                inicial = med
        i+=1
    return med

contador = -100000
while contador < 100000:
  raiz = met_bissec(contador, contador + 1, 10 ** -2)
  if isinstance(raiz, float):
    lista_interna = list()
    lista_interna.append(contador)
    lista_interna.append(contador + 1)
    lista_intervalo.append(lista_interna)
    lista_raizes.append(raiz)
  contador += 1

print("Os intervalos são: \n \n" , lista_intervalo)
print("=" * 40)
print("O valor das Iterações é: \n \n" , lista_raizes)
print("=" * 40)

for i in enumerate(lista_intervalo):
    contador = 0
    x = 0
    y = 0
    for c in i:
        if contador == 0:
            x = c
        else:
            y = c
        contador += 1
    k = np.linspace(x, y)
    plt.title(f"Grafico: {x}, {y}")
    plt.plot(k, funcao(k))
    plt.show()
