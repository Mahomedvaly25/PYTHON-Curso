# Faca um programa que leia um numero qualquer e mostre o seu Factorial.
# Ex:
#    5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um numero: '))
f = 1
c = n
print('CALCULANDO... {}! = '.format(n), end=' ')
while c > 0:
    print(c, end=' ')
    print('x' if c > 1 else '=', end=' ')
    f = f * c
    c = c - 1
print(f)