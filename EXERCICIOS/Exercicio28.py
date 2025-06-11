# CONDICOES EM PYTHON
# Escreva um programa que faca o computador ªpensarª em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O Programa devera escrever na tela se o usuario venceu ou perdeu

from random import randint
from time import sleep

numero = randint(0,5)
numeroE = int(input('Escolhe um numero entre 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if numero == numeroE:
    print('ACERTOU, o Numero Gerado foi {} PARABENS'.format(numero))
else:
    print('ERROU, o Numero Gerado foi {}, Tente Novamente.'.format(numero))