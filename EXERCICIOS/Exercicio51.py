# Densevolva um programa que leia o 1o Termo e a Razao de uma PA.
# No Final, mostre o 10 primeiros termos dessa progressao.

primeiro = int(input('Digite o 1o Termo: '))
razao =  int(input('Indique a Razao: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{} + {}'.format(c,razao), end=' = ')
print('ACABOU')
