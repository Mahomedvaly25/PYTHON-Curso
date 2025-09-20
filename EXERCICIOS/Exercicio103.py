'''
Faca um programa que tenha uma funcao chamada ficha(), que receba 2 parametros opcionais: O nome de um jogador,
e quantos gols ele marcou.
O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.
'''
def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gols.')
n = str(input('Digite o Nome do Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
