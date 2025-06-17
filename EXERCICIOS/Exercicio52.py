# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

numero = int(input('Digite um numero para verificar se ele é Numero PRIMO: '))
tot = 0
for cont in range(1, numero + 1):
    if numero % cont == 0:
        print('\033[36m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(cont), end=' ')
print('\n\033[mO Numero {} foi divisivel {} VEZES!!!'.format(numero,tot))
if tot == 2:
    print('E por isso que ele é Numero PRIMO')
else:
    print('E por isso que ele nao é Numero PRIMO')