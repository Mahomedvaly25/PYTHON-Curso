''' Crie um programa que gere o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou, depois vai ler a quantidade de golos feito em cada partida.
No final, tudo isso ira ser guardado em um dicionario, incluindo a quantidade de gols feito durante o campeonato.
'''

cadastro = dict()
gols = []
cadastro['Nome'] = str(input('Nome do Jogador:  '))
NumPartidas = int(input(f'Quantas partidas {cadastro["Nome"]} jogou ?  '))
for c in range(0,NumPartidas):
    gols.append(int(input(f'Quantos gols na {c + 1}a partida:  ')))
cadastro['GOLS MARCADOS'] = gols[:]
cadastro['TOTAL GOLS'] = sum(gols)
print('-=' * 30)
cadastro['GOLS MARCADOS'] = gols
print(cadastro)
print('-=' * 30)
for k,v in cadastro.items():
    print(f'{k} = {v}')
print('-=' * 30)
print(f'O Jogador {cadastro["Nome"]} jogou {NumPartidas} partidas!!!')
for i, g in enumerate(gols):
    print(f'   => Na {i+1}a Partida fez {g} Gols.')
print(f'Foi um total de {cadastro["TOTAL GOLS"]} GOLS!!!')
