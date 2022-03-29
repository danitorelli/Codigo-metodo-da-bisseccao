import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


funcao = (input("Digite a função: "))
N = (input("Digite o número de interações desejada: "))
ep = (input("Digite o epsilon da sua função: "))

def f(x):
    return funcao

intervalo = (-100000, 100000)

def numero_de_interacoes():
    return N

def epsilon ():
    return ep

x1, x2 = intervalo
f1 = f(x1);
f2 = f(x2);


#def bissecao(f, a, b, ATOL):
#    n = np.ceil(np.log2((a+b)/(2*ATOL)))
#    a_alg = a
#    b_alg = b
#    
#    for _ in range(int(n)):
#        p = (a_alg + b_alg) / 2
#        fp = f(p)
#        
#        if f(a_alg) * fp < 0: b_alg = p
#        else: a_alg = p   
#    
#    return p
#
#bissecao(np.sin, 2 * np.pi / 3, 7 * np.pi / 6, 1e-8)
