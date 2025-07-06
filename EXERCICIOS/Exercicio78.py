# Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final mostre qual maior e o menor digitado e as suas respetivas posicoes na lista.
maior = 0
menor = 0
valores = []
for cont in range(0,5):
    valores.append(int(input(f'Digite qualquer numero para a posicao {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('='*50)
print(f'Os Valores digitados foram: {valores}')
print(f'O Maior valor digitado for {maior}')
print(f'O menor valor digitado foi {menor}')
