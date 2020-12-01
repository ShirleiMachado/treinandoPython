''' Esse código foi criado para fazer um sorteio de amigo secreto'''

from random import randint, choice

familia = ['Shirlei', 'Tairone', 'Silmara', 'Mariangela', 'Eduardo', 'Márcio', 'Mariana', 'Jussara']
sorteados = []
i = 0
while len(sorteados) < len(familia):
  raffle = choice(familia)
  if (familia[i] != raffle) and (raffle not in sorteados):
    print(f"{familia [i]} tirou {raffle}")
    sorteados.append(raffle)
    i += 1
  else:
    continue