'''Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteia() e somaPar(). A Primeira Funcao
vai sortear 20 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostra a soma entre todos os valores PARES
sorteados pela funcao anterior.'''

from random import randint
from time  import sleep

def sorteio(lista):
    print(f'Sorteando 5 Valores para a lista: ', end=' ')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('PRONTO')

def somaPar(lista):
    soma = 0
    for valor in numero:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores Pares da lista {numero} = {soma}')

numero = []
sorteio(numero)
somaPar(numero)