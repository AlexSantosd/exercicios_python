print('Aumento salário')
sal = float(input('Qual seu salário?'))
if sal > 1250:
    aumento = sal + (sal * 0.1)
else:
    aumento = sal + (sal * 0.15)
print('Quem ganhava R${} passa a ganhar R${}'.format(sal, aumento))
