print('Jokenpô')
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções?
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('Pô')
sleep(0.5)
print('-=' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print('\033[33m Empatou!')
    elif jogador == 1:
        print('Computador \033[31m venceu!')
    elif jogador == 2:
        print('Você \033[34m venceu!')
    else:
        print('Jogada invalida')
elif computador == 1: # computador jogou papel
    if jogador == 0:
        print('Computador \033[31m venceu!')
    elif jogador == 1:
        print('\033[33m Empatou!')
    elif jogador == 2:
        print('Você \033[34m venceu')
    else:
        print('Jogada invalida')
elif computador == 2: # computador jogou tesoura
    if jogador == 0:
        print('Você \033[34m venceu!')
    elif jogador == 1:
        print('Computador \033[31m venceu!')
    elif jogador == 2:
        print('\033[33m Empatou!')
    else:
        print('Jogada invalida')