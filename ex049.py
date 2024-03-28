print('Tabuada com for')

n = int(input('Digite um número:'))
for c in range(1, 11):
    resultado = (n * c)
    print('{} x {:2} = {}'.format(n, c, resultado))