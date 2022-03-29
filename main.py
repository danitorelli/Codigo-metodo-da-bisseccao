import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


funcao = (input("Digite a função: "))
N = (input("Digite o número de interações desejada: "))
ep = (input("Digite o epsilon da sua função: "))
a = -100000
b = 100000

def f(x):
    return funcao

def numero_de_interacoes():
    return N

def epsilon ():
    return ep

x1, x2 = intervalo
f1 = f(x1);
f2 = f(x2);



#def f(x):
#    return funcao
#def b(a,b):
#    c = b
#    n = 0
#    X = []
#    Y = []
#    while (f(c) > 10**-12) or (f(c) < -(10**-12)):
#        c = (a+b)/2
#        if f(c)*f(a) < 0:
#            b = c
#        elif f(c)*f(b) < 0:            
#            a = c
#        n += 1
#        X.append(n)
#        Y.append(c)
#    return c, n, X, Y
#a,n,x,y = b(-0.5,1)
#print(a,n)
#
#%matplotlib inline
#import matplotlib.pyplot as plt
#plt.figure(figsize=(10, 10))
#plt.style.use('fivethirtyeight')
#plt.plot(x,y, '-b', color='green')
#plt.show()
