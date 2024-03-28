from random import choice  # import random
print('Escolha aleatória do aluno')
n1 = str('Paulo')
n2 = str('Ana')
n3 = str('Pedro')
n4 = str('Maria')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido para apagar o quadro é {}'.format(escolhido))
