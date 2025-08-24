''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario.
No Final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.'''

from random import randint
from operator import itemgetter
from time import sleep

jogo = {}
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = []
for k, v in jogo.items():
    print(f'{k} = {v}')
    sleep(2)
print('-=' * 20)
print('        == RANKING DO JOGO == ')
print('-=' * 20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'    {k+1}o. lugar: {v[0]} com {v[1]} pontos')
    sleep(1)

