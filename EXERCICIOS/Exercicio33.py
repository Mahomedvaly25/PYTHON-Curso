# CONDICOES EM PYTHON
# Faca um programa que leia 3 numeros e mostre qual e o maior e qual e o menor.

n1 = int(input('Digite o 1o Numero: '))
n2 = int(input('Digite o 2o Numero: '))
n3 = int(input('Digite o 3o Numero: '))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor numero digitado foi {}'.format(menor))
print('O maior numero digitado foi {}'.format(maior))