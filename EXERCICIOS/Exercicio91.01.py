from random import randint
from operator import itemgetter
from time import sleep
jogo = {}
jogo = {'JOGADOR01': randint(1,6),
        'JOGADOR02': randint(1,6),
        'JOGADOR03': randint(1,6),
        'JOGADOR04': randint(1,6)}
print('_' * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k,v in jogo.items():
        print(f'{k} = {v}')
        sleep(2)
print('_' * 40)
for i,v in enumerate(ranking):
        print(f'{i+1} Lugar: {v[0]} com {v[1]} Pontos')
        sleep(1)