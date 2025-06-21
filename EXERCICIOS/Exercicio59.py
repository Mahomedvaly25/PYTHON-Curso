# Crie um programa que leia 2 valores e mostre um meno na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# Seu programa devera realizar a operacao solicitada em cada caso.
from time import sleep
n1 = int(input('Digite o 1o Numero: '))
n2 = int(input('Digite o 2o numero: '))
opcao = 0
print('-='*15)
while opcao != 5:
    print('''    [1] SOMA
    [2] MULTIPLICACAO
    [3] MAIOR NUMERO
    [4] DIGITE NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    print('-='*15)
    opcao = int(input('Escolhe uma Opcao: '))
    if opcao == 1:
        soma = n1 + n2
        print('A Soma entre os numero {} + {} = {}'.format(n1,n2,soma) )
    elif opcao == 2:
        multip = n1 * n2
        print('Multiplicando os numeros {} x {} = {}'.format(n1,n2,multip))
    elif opcao == 3:
        if n1 < n2:
            maior = n2
            print('O Maior numero e {}'.format(maior))
        else:
            maior = n1
            print('O Maior numero e {}'.format(maior))
    elif opcao == 4:
        n1 = int(input('Digite o 1o Numero: '))
        n2 = int(input('Digite o 2o Numero: '))
    elif opcao == 5:
        print('FINALIZANDO.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('\nObrigado por Participar, volte SEMPRE.')
    else:
        print('Opcao invalida, tente novamente: ')
    print('-='*10)
    sleep(4)