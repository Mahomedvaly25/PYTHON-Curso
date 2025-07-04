# Desenvolve um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posicao foi digitado o 1o valor 3.
# c) Quais foram os numeros Pares.

valor = (int(input('Digite um numero: ')),int(input('Digite um numero: '))
             ,int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print(f'Os valores digitados sao {valor}')
print(f'O Valor 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O Valor 3 apareceu na {valor.index(3)+1}a posicao')
else:
    print('O Valor 3 nao foi digitado em nenhuma posicao')
print('Os Valores pares digitados foram ',end=' ')
for n in valor:
    if  n % 2 == 0:
        print(n, end=' ')