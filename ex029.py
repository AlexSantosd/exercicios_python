print('Radar Eletronico')
veloa = int(input('Qual a velocidade atual do carro?'))
velop = int(80)
multa = (veloa - velop)*7
if veloa <= velop:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Você excedeu o limite de {} Km/h'.format(velop))
    print('Você deve pagar uma multa de R${:.2f}! '.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
