#Desenvolva um programa que leia dua notas de alono. Calcule e mostre a sua media.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)**1/2
if m >= 10:
    print('O Aluno com as notas \033[32m{}\033[m e \033[32m{}\033[m teve uma media final de \033[32m{}\033[m'.format(n1, n2, m))
else:
    print('O Aluno com as notas \033[31m{}\033[m e \033[31m{}\033[m teve uma media final de \033[31m{}\033[m'.format(n1,n2,m))