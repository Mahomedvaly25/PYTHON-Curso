'''Faca um programa que tenha uma funcao chamada maior(), que receba varios parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles e o maior.
'''

def maior( * num ):
    print(f'Analisando os Valores Passados...')
    maiornum = 0
    for valor in num:
        print(f'{valor}', end=' ')
        if valor == 0:
            maiornum = valor
        if maiornum <= valor:
            maiornum = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maiornum}')
    print(f'-=' * 30)
maior(9,4,2,5,1,7,5)
maior(4,8,1,3,2,4,)
maior(2,7,5,)
maior(1,6)
maior(4)
maior()