#Crie um programa que leie um numero real qualquer pelo teclado e mostre na tela a sua posicao inteira.
#Exemplo: Digite um numero:   6.127
#         O numero 6.127 tem a parte inteira 6.

'''import math
num = float(input('Digite um valor: '))
print('O Numero Digitado foi {}, e a parte inteira {}'.format(num, math.trunc(num)))'''


#Podera tambem fazer o exercicio importando somente o parametro trunc da biblioteca math, por exemplo:

'''from math import trunc
num =  float(input('Digite um numero: '))
print('O Numero Digitado foi {} e a parte inteira e de {}'.format(num, trunc(num)))'''

#Fazendo o exercicio sem usar ou importar a biblioteca math

num = float(input('Digite um numero: '))
print('O Numero digitado foi {} e a sua parte inteira e {}'.format(num, int(num)))

