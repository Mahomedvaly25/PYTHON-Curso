# CONDICOES EM PYTHON
# Crie um programa que leia um numero inteiro e mostre na tela se ele e par ou impar.

numero = int(input('Digite um numero Inteiro: '))
if numero % 2 == 0:
    print('O numero {} e PAR'.format(numero))
else:
    print('O numero {} e IMPAR'.format(numero))