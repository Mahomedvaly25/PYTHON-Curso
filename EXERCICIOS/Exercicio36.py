# Escreva um programa para aprovar o projeto bancario para a compra de uma casa. O Programa vai perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

casa = float(input('Indique o valor da casa em venda: EU'))
salario = float(input('Qual o valor do salario: EU'))
anos = int(input('Em quantos Anos pretende pagar pela casa: '))

prestacao = casa / (anos * 12)

print('Para Comprar uma CASA de \033[4;36mEUR{:.2f}\033[m em \033[4;36m{}Anos\033[m, a prestacao sera de \033[4;34mEUR{:.2f}\033[m'.format(casa,anos,prestacao))
if prestacao <= salario * ( 30 / 100 ):
    print('O Emprestimo pode ser \033[1;;42mCONSEDIDO\033[m')
else:
    print('O Emprestimo sera \033[1;41mRECUSADO\033[m')
