# Crie um programa que leia varios numeros inteiros pelo teclado. No Final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
from idlelib.colorizer import prog_group_name_to_tag

media = repeticao = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um Numero: '))
    soma += n
    repeticao += 1
    if repeticao == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / 2
print('A Media dos numeros digitados e {}'.format(media))
print('O Maior numero digitado foi {} e o menor e {}'.format(maior, menor))