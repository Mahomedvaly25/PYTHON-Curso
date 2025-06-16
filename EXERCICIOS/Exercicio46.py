# Faca um programa que mostre na tela a contagem regressiva para estouros de fogo de artificio, indo de 10 ate O, com uma pausa de 1 seg. entre elas.

from time import sleep
import emoji

for c in range(10,0,-1):
    print(c)
    sleep(1)
print(emoji.emojize(':party_popper::party_popper:'))
