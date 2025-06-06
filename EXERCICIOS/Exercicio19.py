#Um professor quer sortear um dos seus alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = input('Digite o 1o nome: ')
aluno2 = input('Digite o 2o nome: ')
aluno3 = input('Digite o 3o nome: ')
aluno4 = input('Digite o 4o nome: ')

print('='*50)
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido =  random.choice(lista)
print('O aluno escolhido foi = {}'.format(escolhido))
print('='*50)

#Tambem poderia IMPORTAR somente o choice dentro de RANDOM:

#from random import choice