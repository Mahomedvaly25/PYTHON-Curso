#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros a milimetros

print('='*70)
Mt = float(input('Digite um valor em metros para ver a conversao em CENTIMETROS E MILIMETROS:  '))
Cm = Mt * 100
mm = Mt * 1000
print('='*70)
print('{} mt = {} cm'.format(Mt,Cm))
print('{} mt = {} mm'.format(Mt,mm))
