# Crie um programa que tenha uma tupla unica com nomes de produtos e seu respectivo preco, na sequencia.
# No final mostre uma listagem de preco organizando os dados em forma tabular

produtos = ('Toyota', 1400,'Mazda',2390,'Nissan',1200,'Mercedes',6540,'VW',7400, 'Tata', 90, 'Motos', 1100,'Renalt',5300)
print('-'*45)
for cada in range(0,len(produtos)):
    if cada % 2 == 0:
        print(f'{produtos[cada]:.<30}',end=' ')
    else:
        print(f'${produtos[cada]:9.2f}')
print('-'*45)