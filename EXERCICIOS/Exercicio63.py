# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
t1 = 0
t2 = 1
c = 3
print('{:^40}'.format('SEQUENCIA DE FIBONICCI'))
nx = int(input('Digite quantas sequencias quer ver: '))
print('-='*30)
print('{} - {}'.format(t1,t2), end=" ")
while c <= nx:
    t3 = t1 + t2
    print('-', t3, end=" ")
    t1 = t2
    t2 = t3
    c += 1
print('- Fim')