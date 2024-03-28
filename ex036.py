casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento?'))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será R$ {:.2f}'.format(casa, anos, prestaçao))
if prestaçao <= minimo:
    print('Emprestimo concedido!!!')
else:
    print('Emprestimo negado!!!')

