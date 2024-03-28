print('Quantidade de tinta ')

largura = float(input('Quanto de largura tem essa parede?:'))
altura = float(input('Quanto de altura tem essa parede?:'))
area = largura * altura
tinta = area / 2

print('Para pintar uma parede de {} largura com {} de altura seria necessário {} litros de tinta' .format(largura, altura, tinta),end='')
print(' para cobrir a área de {} metros quadrados' .format(area))


