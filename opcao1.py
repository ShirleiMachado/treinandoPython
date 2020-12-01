''' Esse código foi criado para fazer um sorteio de amigo secreto'''

from random import randint, choice

familia = ['Shirlei', 'Tairone', 'Silmara', 'Mariangela', 'Eduardo', 'Márcio', 'Mariana', 'Jussara']
sorteados = []
i = 0
while len(sorteados) < len(familia):
  a = choice(familia)
  if (familia[i] != a) and (a not in sorteados):
    print(f"{familia [i]} tirou {a}")
    sorteados.append(a)
    i += 1
  else:
    continue