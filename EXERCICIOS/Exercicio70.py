# Crie um Programa que leia o nome e o preco de varios productos, devera pergunta se o utilizador quer continuar.
# No final mostre:
# - Qual e o total gasto na compra.
# - Quantos productos custam mais de 1000.00 Eur
# - Qual e o nome do produto mais barato.

totgasto = maisde1000 = precobarato = cont = 0
nomebarato = ' '
while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preco: EUR'))

    totgasto += preco

    if preco > 1000:
        maisde1000 += 1
    if cont == 1:
        precobarato = preco
        nomebarato = nome
    else:
        if preco < precobarato:
            precobarato = preco
            nomebarato = nome
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O Total gasto foi {totgasto:.2f} Eur')
print(f'O Total produto mais de 1000 Euros sao {maisde1000:.2f} produtos')
print(f'O produto mais barato foi {nomebarato} que custou {precobarato:.2f} Euros.')