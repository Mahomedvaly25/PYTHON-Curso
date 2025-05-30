#Faca um algoritimo que leia o preco de um produto e mostre o seu novo preco, com 5% de desconto.

print('='*50)
Pr = float(input('Qual o preco do produto que queira ver o desconto de 5%:  '))
Nv = Pr - (Pr * 5/100)
print('O Novo preco com 5% de desconto fica a {} EUR'.format(Nv))
