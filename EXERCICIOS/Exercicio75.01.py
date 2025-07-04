# Desenvolve um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) Quantas vezes apareceu o valor 9
# b) Em que posicao foi digitado o 1o valor 3.
# c) Quais foram os numeros Pares.

valor = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),int(input('Digite ultimo valor: ')))
print('Os Valores digitados foram ', end=' ')
for valores in valor:
    print(valores, end=' ')
print(f'\nO Valor 9 apareceu {valor.count(9)} vezes.')
if 3 in valor:
    print(f'O Primeiro valor 3 foi digitado na {valor.index(3)+1}ª posicao')
else:
    print('O Valor 3 nao foi digitado em nenhuma posicao.')
print('Os valores pares digitados foram ', end=' ')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ; ')
print('\n')
print('OBRIGADO')
