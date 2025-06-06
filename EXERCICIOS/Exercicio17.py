#Faca um programa que leia o catete oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.

#   Resolucao de uso da Biblioteca math

'''Cateto_Oposto = float(input('Digite o valor do Cateto Oposto: '))
Cateto_Adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = ( Cateto_Oposto ** 2 + Cateto_Adjacente ** 2 ) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(hipotenusa))'''

#  Usando a biblioteca math

from math import hypot
Cateto_Oposto = float(input('Digite o  valor do Cateto Oposto: '))
Cateto_Adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = hypot(Cateto_Oposto, Cateto_Adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))