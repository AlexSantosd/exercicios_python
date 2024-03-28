r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segunfo segmento:'))
r3 = float(input('terceiro segmento:'))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('Os segmentos podem formar um tringulo!')
else:
    print('Os segmentos não podem formar um triangulo!')

