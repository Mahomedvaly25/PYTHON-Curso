'''Faca um programa que ajude jogadores da mega sena a criar palpites.
O programa vai perguntar quantos jogos serao gerados e vai gerar 6 numeros entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint

lista = []
listaprincipal = []
cont = totalrepeticoes = 0

repeticoes = int(input('Quantos sorteios pretende sortear? : '))

while totalrepeticoes < repeticoes:
    cont = 0

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    listaprincipal.append(lista[:])
    lista.clear()
    totalrepeticoes += 1

for i, l in enumerate(listaprincipal):
    print(f'JOGO {i+1}: {l}')

