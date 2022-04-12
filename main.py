import math
import numpy as np
import matplotlib.pyplot as plt
#from math import e 
from numpy import e

lista_raizes = list()
lista_intervalo = list()

#def getExp(x):
#  return e**x

def funcao(x):
    #func = math.exp(e)**x - 2 * x - 1
    func = np.exp(e)**x - 2 * x - 1
    return func

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
