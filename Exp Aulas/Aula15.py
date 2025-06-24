# USANDO O COMANDO BREAK PARA INTERROPCCAO.
soma = n = 0
while True:
    soma += n
    n = int(input('''Escolha um Numero...
Para SAIR Digite [999]:  '''))
    if n == 999:
        break
print('A Soma de todos os numeros = {}'.format(soma))