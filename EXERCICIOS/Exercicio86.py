# Crie um programa que crie uma matriz de dimensao 3 x 3 e preencha os valores lidos pelo teclado.
#        |        |
#   ----------------------
#        |        |
#   ----------------------
#        |        |
# No final mostre a Matriz na tela, Com a formatacao correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um Numero na posicao [{l},{c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print(pares)