# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagameno:
# - A vista Dinheiro/Cheque: 10% de desconto.
# - A vista no cartao: 5% de desconto
# - Em ate 2x no cartao: Preco normal
# - 3x ou mais no cartao: 20% de juros

preco = float(input('Digite o Valor do Produto: '))
print('''Forma de Pagamento:
[1] a vista Dinheiro/Cheque: 10% de desconto.
[2] a vista cartao: 5% de desconto.
[3] em ate 2x no cartao: Preco Normal
[4] 3x ou mais no cartao: Pagamento com Juros de 20%''')
opcao = int(input('Escolhe uma das Opcoes: '))

if opcao == 1:
     precoFinal = preco - ( preco * 10 / 100 )
elif opcao == 2:
    precoFinal = preco - (preco * 5 / 100)
elif opcao == 3:
    precoFinal = preco
    parcela = precoFinal / 2
    print('A sua compra sera parcelada em 2x de {}, Sem JUROS'.format(parcela))
elif opcao == 4:
    totalParcelas = int(input('Em quantas parcelas que pagar: '))
    parcelas = preco / totalParcelas
    precoFinal = preco + ( preco * 20 / 100 )
    print('A Sua compra sera parcelada em {}x de EUR{:.2f}, com JUROS'.format(totalParcelas,parcelas))
else:
    precoFinal = preco
    print('OPCAO INVALIDA DE PAGAMENTO, tente novamente...')
print('As Compras de EUR{:.2f} no final ira custar EUR{:.2f}'.format(preco,precoFinal))
