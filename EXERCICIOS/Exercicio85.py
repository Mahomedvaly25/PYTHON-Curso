# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valoes Pares e Impares.
# No final mostre os valores pares e impares em ordem crescente.

lista = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}o Valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-='*25)
print(f'Os Valores pares digitados foram: {lista[0]}')
print(f'Os Valores Impares Digitados foram: {lista[1]}')