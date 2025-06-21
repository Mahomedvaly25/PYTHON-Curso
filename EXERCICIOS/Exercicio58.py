# Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10.
# Agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint
computador = randint(0,10)
print('Sou o Computador, acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador  =  int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco Mais...')
        else:
            print('Um pouco Menos...')
print('Parabens!!!! ACERTOU com {} tentativas.'.format(tentativas))
