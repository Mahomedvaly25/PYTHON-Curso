''' Aprimore o desafio 93 para que ele funcione com varios jogadores, incluindo um sistema de visualizacao de detalhes do aproveitamento de cada jogador.
'''

cadastro = dict()
time = []
gols = []
while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Nome do Jogador:  '))
    NumPartidas = int(input(f'Quantas partidas {cadastro["Nome"]} jogou ?  '))
    for c in range(0,NumPartidas):
        gols.append(int(input(f'Quantos gols na {c + 1}a partida:  ')))
    cadastro['GOLS MARCADOS'] = gols[:]
    cadastro['TOTAL GOLS'] = sum(gols)
    gols.clear()
    time.append(cadastro.copy())
    while True:
        resp = str(input('Qeer Continuar? [S / N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('-=' * 20)
for i, v in enumerate(time):
    print(f'{i+1} ', end=' ')
    for d in v.values():
        print(f'{d}', end=' ')
