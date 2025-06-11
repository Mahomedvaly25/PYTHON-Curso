#Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e o seu antecessor
n = int(input('Digite um numero: '))
print('O seu sucessor do numero', n, 'e: \033[31m{}\033[m'.format(n + 1))
print('E o seu antecessor e: \033[35m{}\033[m'.format(n - 1))
