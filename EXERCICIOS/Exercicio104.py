'''
Crie uma programa que tenha a funcao leiaInt(), que  vai funcionar de forma semelhante a funcao input() do python,
so que fazendo a validacao para aceitar apenas um valor numerico.
Ex:
n = leiaInt('Digite um numero:')
'''

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO: Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero: ')
print(f'O Numero que acabou de digitar e o numero {n}')