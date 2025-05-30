#Desenvolva um programa que leia dua notas de alono. Calcule e mostre a sua media.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)**1/2
print('O Aluno com as notas {} e {} teve uma media final de {}'.format(n1, n2, m))
