print('Desconto de 5%')

produto = float(input('Qual o valor do produto? '))
desconto = (produto*5)/100
precofinal = produto-desconto

print('Ao comprar um produto de valor {}, com desconto de 5% você pagará {:.2f} reais '.format(produto, precofinal))
