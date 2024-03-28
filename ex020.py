from random import shuffle
print('Ordem na lista')
n1 = str(input('Primeiro aluno:'))
n2 = str(input('DSegundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem da apresentação será')
print(lista)
