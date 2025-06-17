# Faca um programa que leia uma frase qualquer e diga se ela e um palindromo, disconsiderando os espacos.
# Nota: PALINDROMO sao frases que se leem da esquerda para direita e vice-versa.
# ExemploL
# - Apos a Sopa
# - A Sacada da casa
# - A Torre da Derrota
# - O Lobo ama bolo
# - Anotaram a data da Maradona

frase = str(input('Digite uma frase quanquer para verificar se é um PALINDROMO: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''
for letra in range(len(juncao) -1, -1, -1):
    inverso = inverso + juncao[letra]
    print(juncao[letra], end=' ')
if inverso == juncao:
    print('\nTEMOS UM PALINDROMO')
else:
    print('\nA Frase digitada NAO é um PALINDROMO')
