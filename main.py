import numpy as np
import matplotlib.pyplot as plt

lista_raizes = list()
lista_intervalo = list()

def funcao(x):
    func = x ** 3 - 9 * x + 3
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
    lista_intervalo.append(f'[{contador}, {contador + 1}]')
    lista_raizes.append(raiz)
  contador += 1

print(lista_intervalo)
print(lista_raizes)
