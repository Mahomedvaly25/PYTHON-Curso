#Refaca o Defasio 09, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando lacos for
n = int(input('Digite um numero para ver sua tabuada de 10:  '))
for c in range(1, 11):
    print('{} x {} = {}'.format(c,n,c * n))