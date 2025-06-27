# Crie um programa que simule o funcionamento do caixa electronico.
# No inicio pergunte ao usuario qual sera o valor a ser sacado (numeros inteiros).
# No final vai informar quantas cedulas de cada valor serao entregues.
# Obs: Considere que o caixa possui cedulas de 50.00 Eur, 20.00 Eur, 10.00 Eur e 1.00 Eur

print('-'*20)
print('CAIXA ELECTRONICO')
print('-'*20)

montante = int(input('O Valor pretende sacar: '))
print('='*20)
nota = 50
totmontante = montante
quantitnota = 0

while True:
    if totmontante >= nota:
        totmontante -= nota
        quantitnota += 1
    else:
        if quantitnota > 0:
                print(f'Sao {quantitnota} Notas de {nota} Euros')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        if totmontante == 0:
            break
        quantitnota = 0
print('*'*20)
print('OBRIGADO!!!')