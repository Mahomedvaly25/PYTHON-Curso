#Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
rq = n**(1/2)
print('O dobro de {} e: {}, o triplo e {}, a raiz quadrada e {:.3}'.format(n,d,t,rq))
