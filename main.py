import numpy as np
import math

def funcao(x):
    func = x ** 3 - 9 * x + 3
    return func

def met_bissec(inicial, final, precisao):
    iteracao = (np.log(final - inicial) - np.log(precisao)) / np.log(2)
    iteracao = np.ceil(iteracao)
    i=0
    print("VALORES DAS INTERAÇÕES")

    while i < iteracao:
        if funcao(inicial) * funcao(final) > 0:
            print("Não há raiz nesse intervalo!")
        else:
            med = (inicial + final) / 2
            med = round(med, 6)
            
            if funcao(inicial) * funcao(med) < 0:
                final = med
            else:
                inicial = med
        print(f'Valor de x{i + 1} = { med }')
        i+=1
    print()
    return print(f'O valor da raiz é aproximadamente: { med }')

    return met_bissec;

precisao = float(input('Digite o valor da precisao: '))
met_bissec(-100000, 100000, precisao ** -2)