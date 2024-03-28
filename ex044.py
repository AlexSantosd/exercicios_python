print('{:=^40}'.format('LOJA do ALEX'))
compra = float(input('Preço das compras: R$'))
print('''Forma de Pagamento
[1] à vista
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é o opção?'))
if opção == 1:
    total = compra - (compra * 10 / 100)
elif opção == 2:
    total = compra - (compra * 5 / 100)
elif opção == 3:
    total = compra
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${} sem juros'.format(parcela))
elif opção == 4:
    total = compra + (compra * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = compra
    print('Opção invalida de pagamento')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(compra, total))


