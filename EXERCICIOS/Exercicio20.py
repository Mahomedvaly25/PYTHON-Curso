#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Digite o 1o nome: '))
n2 = str(input('Digite o 2o nome: '))
n3 = str(input('Digite o 3o nome: '))
n4 =  str(input('Digite o 4o nome: '))
print('='*50)
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A Ordem de apresentacao sera {}'.format(lista))