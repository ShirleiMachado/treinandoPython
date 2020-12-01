import random

amigos = ['Shirlei', 'Silmara', 'Tairone', 'Mariangela', 'Mariana', 'Eduardo', 'Marcio', 'Jussara']
random.shuffle(amigos)

for index in range(len(amigos)):
  compra = index
  recebe = index + 1
  try:
    print(f"{amigos[compra]:>8} -- tirou --> {amigos[recebe]}")
  except IndexError:
    print(f"{amigos[compra]:>8} -- tirou --> {amigos[0]}")