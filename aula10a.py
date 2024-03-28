nome = str(input('Qual é o seu nome? '))
if nome == 'Alex':
    print('Que nome lindo você tem!!!')
else:
    print('Seu nome é tão normal')
print('Bom dia {}.'.format(nome))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f} '.format(m))
if m >= 7:
    print('Parabéns {} você foi aprovado'.format(nome))
else:
    print('Estude mais {} , você foi reprovado'.format(nome))

