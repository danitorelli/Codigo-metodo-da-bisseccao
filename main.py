import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


funcao = (input("Digite a função: "))
Nint = (input("Digite o número de interações desejada: "))
ep = (input("Digite o epsilon da sua função: "))
intrvalo_a = -100000
intervalo_b = 100000

def bissec(intervalo_a, intervalo_b, ep):
  # calcula o numero de interações
  Nint = (np.log(intervalo_b - intervalo_a) - np.log(ep)) / np.log(2)

  # pega o prox inteiro
  Nint = np.ceil(Nint)
  i = 0
  print('-=' * 15)
  print('Valor das iterações')
  print('-=' * 15)

  while i < Nint:
    # condição de Bolzano
    if f(intervalo_a) * f(intervalo_b) > 0:
      print('Não é possível descobrir a raiz desse intervalo')
    else:
      # fazer a media
      media = (intervalo_a + intervalo_b) / 2
      media = round(media, 6)

      if f(intervalo_a) * f(media) < 0:
        intervalo_b = media
      else:
        intervalo_a = media
    print(f'valor de x{i+1} = {media}')
    i+=1
  print()
  return print(f'O valor da raiz é aproximadamente {media}')


## definir a função aqui
#def f(x):
#  y = x ** 3 - 9 * x + 3
#  return y
#
## chama o metodo passando intervalo e erro
#bissec(0, 1, 10 ** -2)



#%matplotlib inline
#import matplotlib.pyplot as plt
#plt.figure(figsize=(10, 10))
#plt.style.use('fivethirtyeight')
#plt.plot(x,y, '-b', color='green')
#plt.show()