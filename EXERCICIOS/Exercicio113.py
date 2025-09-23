'''
Reescreva a funcao leiaInt() que fizemos no Exercicio 104, incluido agora a possibilidade de digitalizacao de um
numero de tipo Invalido.
Aproveite e crie tambem um funcao leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite um numero inteiro valido!\033[m')
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados Interropida pelo usuario!\033[m')
            return 0
        else:
            return n

def leiaFoat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO: Por favor digite um numero Inteiro valido!\033[m')
        except(KeyboardInterrupt):
            print(f'O Programa foi Interropido pelo Usuario.')
            return 0
        else:
            return n

n1 = leiaInt('Digite um numero: ')
n2 = leiaFoat('Digite um numero: ')
print(f'O Numero inteiro digitado foi {n1} e o Numero Real foi {n2}')