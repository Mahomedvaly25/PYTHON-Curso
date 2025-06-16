#Desenvolva um programa que leia 6 numeros inteiros e mostram a soma apenas daqueles que forem PAR, se o valor digitado for IMPAR, desconsidere-o.
soma = 0
cont = 0
for c  in range(1,7):
    n = int(input('Digite o {}o Numero: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('O Total de numeros PARES digitados foram {}, e a Soma dos Numeros PARES e {}'.format(cont,soma))