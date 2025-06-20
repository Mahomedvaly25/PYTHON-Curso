#Escreva um programa que leia um valor em metros e o exiba convertido em centimentros a milimetros

print('\033[33m='*70,'\033[m')
Mt = float(input('Digite um valor em metros para ver a conversao em CENTIMETROS E MILIMETROS:  '))
Cm = Mt * 100
mm = Mt * 1000
print('\033[33m='*70,'\033[m')
print('{} mt = {} cm'.format(Mt,Cm))
print('{} mt = {} mm'.format(Mt,mm))
