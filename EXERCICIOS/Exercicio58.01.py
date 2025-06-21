from random import randint
computador = randint(0,10)
print('O Algoritimo gerou um numero aleatorio entre 0 e 10')
print('Sera que VOCE consegui advinhar qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Tente mais uma vez: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente Mais alto!!!')
        else:
            print('Tente Numero abaixo!!!')
print('Acertou com {} tentativas!!!'.format(tentativas))