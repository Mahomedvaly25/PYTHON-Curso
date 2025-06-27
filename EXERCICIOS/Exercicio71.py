# Crie um programa que simule o funcionamento do caixa electronico.
# No inicio pergunte ao usuario qual sera o valor a ser sacado (numeros inteiros).
# No final vai informar quantas cedulas de cada valor serao entregues.
# Obs: Considere que o caixa possui cedulas de 50.00 Eur, 20.00 Eur, 10.00 Eur e 1.00 Eur

print('='*20)
print('CAIXA ELECTRONICO')
print('='*20)

quantidadeNotas = totalnota = 0
nota = 50

valorlevantar = int(input('Qual valor deseja levantar: '))
totalnota = valorlevantar
while True:
    if totalnota >=  nota:
        totalnota -= nota
        quantidadeNotas += 1
    else:
        if quantidadeNotas > 0:
            print(f'Sao {quantidadeNotas} Notas de {nota} Euros.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        quantidadeNotas = 0
        if totalnota == 0:
            break
print('OBRIGADO')
