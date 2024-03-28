print('=' * 20)
print('10 termos de uma PA')
print('=' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Qual é a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou')