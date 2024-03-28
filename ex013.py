print('Aumento de salário de 15%')
salario = float(input('Qual é o seu salário?'))
aumento = (salario*15)/100
salariof = salario+aumento

print('O seu salário é de {}, com o reajuste ele passará a ser {:.2f} reais '.format(salario, salariof))
