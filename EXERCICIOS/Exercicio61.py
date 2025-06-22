# Refaca o desafio 051 , lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while.
print('-='* 30)
print('{:^60}'.format('GERADOR DE PA',))
print('-='*30)
primeirotermo = int(input('Introduz o 1o Termo: '))
razao = int(input('Indique a Razao: '))
cont = 0
print('-='*30)
while cont <= 9:
    print(primeirotermo, end=" ")
    print(' - 'if cont < 9 else ' ', end=' ')
    primeirotermo = primeirotermo + razao
    cont += 1
print('\n')
print('-='*30,)
