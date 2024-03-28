n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
soma = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2
divisao = n1/n2
divisaointeira = n1//n2
exponenciacao = n1**n2

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f},'.format(soma, multiplicacao, divisao), end='')
print('a divisão inteira é {}, e a exponenciação é {}'.format(divisaointeira, exponenciacao))

