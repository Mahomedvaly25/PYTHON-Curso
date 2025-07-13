# Faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:
# - Quantas pessoas foram cadastradas;
# - Uma listagem com as pessoas mais pesadas; (peso>)
# - Uma listagem com as pessoas menos pesadas.(peso<)
from pickletools import stringnl_noescape_pair

lista = []
regist =  []
maior = menor = 0
while True:
    regist.append(str(input('Nome: ')))
    regist.append(int(input('Peso: ')))

    if len(lista) == 0:
        maior = menor = regist[1]
    else:
        if regist[1] > maior:
            maior = regist[1]
        if regist[1] < menor:
            menor = regist[1]

    lista.append(regist[:])
    regist.clear()

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Foram cadastrada {len(lista)} pessoas.')
print(f'O maior peso foi {maior}Kg foi de ', end=' ')
for c in lista:
    if c[1] == maior:
        print(f'[{c[0]}]', end=' ')
print(f'\nO menor Peso foi {menor}Kg foi de ', end=' ')
for c in lista:
    if c[1] == menor:
        print(f'[{c[0]}]')
print('-='*30)