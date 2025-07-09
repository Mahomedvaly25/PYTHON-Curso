# Crie um programa onde o usuario possa digitar 5 valores numericos, e cadastre-os em uma lista.
# Valores ja na posicao correta de insercao (sem usar o sort())
# No Final mostre a lista ordenada na tela.

lista = []
for c in range(0,5):
    n = int(input('Digite um Numero: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1

print(lista)