# Aprimore o Exercicio anterior (Exerc86), mostrando no final:
# - A Soma de todos os valores pares digitados.
# - A Soma dos valores da terceira coluna.
# - O Maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapares = soma3coluna = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um numero na posicao [{l}],[{c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()

print(f'A Soma dos numeros Pares sao {somapares}')

for l in range(0,3):
    soma3coluna += matriz[l][2]
print(f'A Soma da 3a Coluna sao: {soma3coluna}')

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'O maior numero da 2a linha e o numero {maior}')
