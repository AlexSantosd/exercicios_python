print('Média da escola')

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
media = (n1 + n2) / 2

if media < 5:
    print('Tirando {} e {}, a média do aluno é {}.'.format(n1, n2, media))
    print('O aluno está \033[0:31m REPROVADO.')
elif media >= 7:
    print('Tirando {} e {}, a média do aluno é {}.'.format(n1, n2, media))
    print('O aluno está \033[0:34m APROVADO.')
else:
    print('Tirando {} e {}, a média do aluno é {}.'.format(n1, n2, media))
    print('O aluno está em \033[0:33m RECUPERAÇÃO.')

