# Faca um programa que jogue par ou impar com o computador, o jogo so sera interropido quando o jogador PERDER.
# No final mostrando o total de victorias consecutivas que ele conquistou no final do jogo.

from random import randint
resultado = vitorias = 0

print('VAMOS JOGAR PAR OU IMPAR')

while True:
    numerojogador = int(input('Digite um Valor: '))
    computador = randint(1, 10)
    resultado = computador + numerojogador
    parOUimpar = ' '
    while parOUimpar not in 'PI':
        parOUimpar = str(input('Par ou Impar: [P/I] ')).strip().upper()[0]
    if parOUimpar == 'P':
        if resultado % 2 == 0:
            parOUimpar = 'PAR'
            print(f'{f"DEU {parOUimpar}!!!\nVOCE VENCEU":*^60}')
            vitorias += 1
        else:
            parOUimpar = 'IMPAR'
            print(f'DEU {parOUimpar:*^10}!!!\nVOCE PERDEU!')
            break
    elif parOUimpar == 'I':
        if resultado % 2 == 1:
            parOUimpar = 'IMPAR'
            print(f'DEU {parOUimpar:*^10}!!!\nVOCE VENCEU')
            vitorias += 1
        else:
            parOUimpar = 'PAR'
            print(f'DEU {parOUimpar:*^10}!!!\nVOCE PERDEU')
            break
    print(f'Voce jogou {numerojogador} e o computador {computador}. Total deu {resultado}', end=' ')
    print(f'que corresponde a {vitorias} vitorias.' if vitorias > 1 else f'que corresponde a {vitorias} vitoria ate agora.')
print(' ')
print(f'GAME OVER! Voce venceu {vitorias} vezes.')