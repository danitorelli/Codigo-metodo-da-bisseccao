import numpy as np

sqrt_list = list()
interval_list = list()

def bisection(init_interval, final_interval, error):
  # calcula o numero de interações
  iterations = (np.log(final_interval - init_interval) - np.log(error)) / np.log(2)

  # o ceil pega o proximo valor inteiro
  iterations = np.ceil(iterations)
  i = 0

  while i < iterations:
    # condição de Bolzano
    if f(init_interval) * f(final_interval) > 0:
      return False
    else:
      # fazer a media
      avg = (init_interval + final_interval) / 2
      avg = round(avg, 6)

      if f(init_interval) * f(avg) < 0:
        final_interval = avg
      else:
        init_interval = avg
    i+=1

  return avg

def f(x):
  y = x ** 3 - 9 * x + 3
  return y

# chama o método passando intervalo e erro
count = -1000
[1, 2]
while count < 1000:
  raiz = bisection(count, count + 1, 10 ** -2)
  if isinstance(raiz, float):
    interval_list.append(f'[{count}, {count + 1}]')
    sqrt_list.append(raiz)
  count += 1

print(interval_list)
print(sqrt_list)