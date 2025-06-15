# Crie um programa que faca o computador jogar JOKENPO com voce (pedra, papel e tesoura).

from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('\033[36mOPCOES\033[m')
print('''
[0] Pedra
[1] Papel
[2] Tesoura''')
jogada = int(input('Escolhe a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogada != 0 or jogada != 1 or jogada != 2:
    print('Jogada Invalida')
else:
    print('O Computador jogou {}'.format(itens[computador]))
    print('A Sua Jogada foi {}'.format(itens[jogada]))

    if computador == 0:
        if jogada == 0:
            print('EMPATE')
        elif jogada == 1:
            print('JOGADOR VENCE')
        elif jogada == 2:
            print('COMPUTADOR VENCE')
        else:
            print('Jogada Invalida')
    elif computador == 1:
        if jogada == 0:
            print('COMPUTADOR VENCE')
        elif jogada == 1:
            print('EMPATE')
        elif jogada == 2:
            print('JOGADOR VENCE')
        else:
            print('Jogada Invalida')
    elif computador == 2:
        if jogada == 0:
            print('JOGADOR VENCE')
        elif jogada == 1:
            print('COMPUTADOR VENCE')
        elif jogada == 2:
            print('EMPATE')
        else:
            print('JOGADA INVALIDA')

