import numpy as np

#init_interval = 1000
#final_interval 1001


def bissection(init_interval, final_interval, error):
  # calcula o numero de interações
  iteracoes = (np.log(final_interval - init_interval) - np.log(error)) / np.log(2)

  # pega o prox inteiro
  iteracoes = np.ceil(iteracoes)
  i = 0
  print('-=' * 20)
  print('Valor das iterações')
  print('-=' * 20)

  while i < iteracoes:
    # condição de Bolzano
    if f(init_interval) * f(final_interval) > 0:
      print('Não é possível descobrir a raiz desse intervalo')
    else:
      # fazer a media
      media = (init_interval + final_interval) / 2
      media = round(media, 6)

      if f(init_interval) * f(media) < 0:
        final_interval = media
      else:
        init_interval = media
    print(f'valor de x{i+1} = {media}')
    i+=1
  print()
  return print(f'O valor da raiz é aproximadamente {media}')


# definir a função aqui
def f(x):
  y = x ** 3 - 9 * x + 3
  return y

# chama o metodo passando intervalo e erro
bissection(0, 1, 10 ** -2)