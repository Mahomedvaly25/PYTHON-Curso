'''Faca um programa que tenha uma funcao chamada contador(), que receba 3 parametros: inicio, fim e passo, e realize a contagem.
Seu programa deve realizar 3 contagens atraves da funcao criada:
a) De 1 a 10, de 1 em 1
b) De 10 ate 0, de 2 em 2
c) Uma contagem personalizada.'''

def contador(i,f,p):
    cont = i
    if p < 0:
        p *= -1
    if p == 1:
        p = 1
    if i < f:
        while cont <= f:
            print(f'{cont}',end=' ')
            cont += p
        print('FIM!')
    else:
        while cont >= f:
            print(f'{cont}',end=' ')
            cont -= p
        print('FIM!')
print('-=' * 25)
print(f'Contador de 1 ate 10 de 1 em 1')
contador(1,10,1)
print(f'Contador de 10 ate 1 de 2 em 2')
contador(10,1,2)
print('-=' * 25)
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fim, pas)