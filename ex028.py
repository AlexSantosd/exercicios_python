from random import randint
from  time import sleep
print('Jogo da Advinhação')

print('-'*55)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('-'*55)

computador = randint(0, 5) # Faz o computador pensar
jogador = int(input('Em que número pensei?')) # faz o jogador adivinhar
print('Processando...')
sleep(1)
if jogador == computador:
    print('Parabéns você conseguiu me ganhar!!!!')
else:
    print('Ganhei, Eu pensei no número {} e nao no {} '.format(computador, jogador))



