# Faca um programa que ajude jogadores da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serao gerados e vai gerar 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.

lista = list()
listaP = list()
totalrep = 0
cont = 0
from random import randint

repeticoes = int(input('Quantas vezes quer: '))

while totalrep < repeticoes:
    cont = 0

    while True:
        sorteio = randint(1,60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break

    listaP.append(lista[:])
    lista.clear()
    totalrep += 1

for i, l in enumerate(listaP):
    print(f'Jogo {i+1}: {l}')

