# Faca um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor de peso lidos.
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}a pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(' A Pessoa com maior Peso foi {} Kg e menor foi {} Kg)'.format(maior,menor))