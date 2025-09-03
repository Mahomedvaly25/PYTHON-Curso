'''Faca um programa que tenha uma funcao chamada contador(), que receba 3 parametros: inicio, fim e passo, e realize a contagem.
Seu programa deve realizar 3 contagens atraves da funcao criada:
a) De 1 a 10, de 1 em 1
b) De 10 ate 0, de 2 em 2
c) Uma contagem personalizada.
'''
from time import sleep


def contador(i,f,p):
    print('-=' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    cont = i
    if i < f:
        print(f'Contador de 1 ate 10 de 1 em 1')
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(1)
            cont += p
        print('FIM!')
    else:
        print(f'Contador de 10 ate 1 de 2 em 2')
        while cont >= f:
            print(f'{cont}', end=' ')
            cont = cont - p
        print('FIM!')
contador(1,10,1)
contador(10,1,2)
print('-=' * 30)
print('Agora e a sua vez de personalizar a contagem!')
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini,fim,pas)
