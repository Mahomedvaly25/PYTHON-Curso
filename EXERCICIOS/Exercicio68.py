# Faca um programa que jogue par ou impar com o computador, o jogo so sera interropido quando o jogador PERDER.
# No final mostrando o total de victorias consecutivas que ele conquistou no final do jogo.

from random import randint


resultado = vitorias = 0
print('Vamos Jogar Par ou Impar')

while True:
    numerojogador = int(input('Digite um Valor: '))
    computador = randint(1, 10)
    resultado = computador + numerojogador
    parOUimpar = ' '
    while parOUimpar not in 'PI':
        parOUimpar = str(input('Par ou Impar: [P/I] ')).strip().upper()[0]
    if parOUimpar == 'P':
        if resultado % 2 == 0:
            resultado = 'P'
            print('VOCE VENCEU')
            vitorias += 1
        else:
            print('VOCE PERDEU!')
            break
    elif resultado % 2 == 1:
        if resultado == 'I':
            print('VOCE VENCEU')
            vitorias += 1
        else:
            print('VOCE PERDEU')
            break
    print(f'Voce jogou {numerojogador} e o computador {computador}. Total deu {resultado} que corresponde a {vitorias} vitorias ate agora.')
print(f'GAME OVER! Voce venceu {vitorias} vezes.')