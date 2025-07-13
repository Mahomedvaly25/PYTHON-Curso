# Minha solucao
# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valoes Pares e Impares.
# No final mostre os valores pares e impares em ordem crescente.

par = []
impar = []
num = []
leitor = 0
for cont in range(0,7):
    leitor = int(input(f'Digite o {cont+1}ª Numero: '))
    if leitor % 2 == 0:
        par.append(leitor)
    else:
        impar.append(leitor)
num.append(par)
num.append(impar)
par.sort(reverse=False)
impar.sort(reverse=False)
print('-='*30)
print(f'Valores pares sao: {par}')
print(f'Valores Impares sao: {impar}')
print('-'*50)
print(f'O Total de Numeros digitados: {num}')
