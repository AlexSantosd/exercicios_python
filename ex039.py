from datetime import date
print('Alistamento militar')
nasc = int(input('Qual o ano de nascimento?'))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} '.format(ano))
else:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} '.format(ano))

