print('Custo da Viagem')
dist = float(input('Qual é a distancia da sua viagem?'))
precoc = dist * 0.5
precol = dist * 0.45

if dist <= 200:
    print('Voce está prestes a começar uma viagem de {}km.'.format(dist))
    print('E o preço da sua passagem será de R${:.2f}'.format(precoc))
else:
    print('Voce está prestes a começar uma viagem de {}km.'.format(dist))
    print('E o preço da sua passagem será de R${:.2f}'.format(precol))

