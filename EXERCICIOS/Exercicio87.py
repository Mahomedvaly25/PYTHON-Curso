# Aprimore o Exercicio anterior (Exerc86), mostrando no final:
# - A Soma de todos os valores pares digitados.
# - A Soma dos valores da terceira coluna.
# - O Maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somacoluna = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor na posicao [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print('+' * 35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print('+' * 32)

print(f'A Soma dos valores PARES = {soma}')
for l in range(0,3):
    somacoluna += matriz[l][2]
print(f'A soma da terceira coluna = {somacoluna}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O Maior valor da 2a linha = {maior}')
print('+' * 32)
