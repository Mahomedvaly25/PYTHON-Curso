# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma menssagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Nao existe o valor maior, os dois sao iguais

primeiro = float(input('Digite o 1o Valor: '))
segundo = float(input('Digite o 2o Valor: '))

if primeiro > segundo:
    print('O PRIMEIRO valor {} é o MAIOR'.format(primeiro))
elif segundo > primeiro:
    print('O SEGUNDO valor {} é o MAIOR'.format(segundo))
else:
    print('Nao EXISTE um valor MAIOR, os 2 sao IGUAIS.')

