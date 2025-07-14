# Faca um programa que ajude jogadores da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serao gerados e vai gerar 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.

vezes = 0
from random import randint
vezes = int(input('Quantos jogos para sortear? '))
for choice in range(1,(vezes):
    num = randint(1,60)