# Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem indique o maior e o menor valor que estao na tupla.
from random import randint
computador = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)
print('Os Valores sorteados foram: ',end=' ')
for n in computador:
    print(f'{n} ',end='')
print(f'\nO Maior valor e {max(computador)}')
print(f'O Menor valor e {min(computador)}')