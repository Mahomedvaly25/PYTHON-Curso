'''
Faca um mini-sistema que utilize o interactive help do Python.
O Usuario vai digitar o comondo e o manual vai aparecer. Quando o usuario digitar a palavra 'FIM', o programa se encerrara.
OBS: use cores.
'''

c = ('\033[m',         #Sem cor
       '\033[0;30;41m',  # 01 Cor Vermelha
       '\033[0;30;42m]', # 02 Cor Verde
       '\033[0;30;43m',  # 03 Cor Amarelo
       '\033[0;30;44m',  # 04 Cor Azul
       '\033[0;30;45m',  # 05 Cor Roxo
       '\033[7;30m'      # 06 Cor Branco
       )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[5], end=' ')
    help(com)
    print(c[0], end=' ')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')

comando = ' '
while True:
    titulo('  SISTEMA DE AJUDA PyHELP',2)
    comando = str(input('Funcao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  Ate Logo', 1)
