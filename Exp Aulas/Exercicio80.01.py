# Crie um programa onde o usuario possa digitar 5 valores numericos, e cadastre-os em uma lista.
# Valores ja na posicao correta de insercao (sem usar o sort())
# No Final mostre a lista ordenada na tela.

valores = []
for cont in range(0,5):
    num = int(input('Digite um Numero: '))
    if cont == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1

print(valores)