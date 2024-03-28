print('Aluguel de carro')
dias = int(input('Quantos dias de aluguel?'))
km = float(input('Quantos KM foram rodados?'))
aluguel = (dias * 60) + (km * 0.15)

print('Para o aluguel de {} dias com {} quilometros rodados será pago {} reais.'.format(dias, km, aluguel))


