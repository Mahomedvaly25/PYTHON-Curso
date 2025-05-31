#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preco a pagar, sabendo que o carro custa $60 por dia e $0.15 por km rodado.

dias = int(input('Quantos dias o Carro ficou alugado? : '))
km = float(input('Quantos kms percorreu: '))
custo = (dias * 60) + (km * 0.15)
print('O Custo total foi de ${}'.format(custo))