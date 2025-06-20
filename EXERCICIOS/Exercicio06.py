#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
rq = n**(1/2)
print('O dobro de \033[32m{}\033[m e:\033[31m{}\033[m, o triplo e \033[31m{}\033[m, a raiz quadrada e \033[31m{:.3}\033[m'.format(n,d,t,rq))
