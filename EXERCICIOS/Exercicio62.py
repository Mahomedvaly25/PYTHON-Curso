# Melhore o desafio 061, perguntando para o usuario se ele que mostrar mais alguns termos. O programa encerra quando ele disser que quer mostra 0 termos.

print('-='* 30)
print('{:^60}'.format('GERADOR DE PA',))
print('-='*30)
primeirotermo = int(input('Introduz o 1o Termo: '))
razao = int(input('Indique a Razao: '))
cont = 0
mais = 10
total = 0
print('-='*30)
while mais != 0:
    total += mais
    while cont <= total:
        print(primeirotermo, end=" ")
        print(' - 'if cont < 9 else ' ', end=' ')
        primeirotermo = primeirotermo + razao
        cont += 1
    print('\n')
    print('-='*30,)
    mais = int(input('Quantos Termos Voce quer mostrar mais? '))
print('Progrecao finalizada com {} termos mostrados.'.format(total))
