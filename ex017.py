from math import hypot   #import math
print('Calculo da hipotenusa')
catetooposto = float(input('Digite o valor da cateto oposto: '))
catetoadjacente = float(input('Digite o valor do cateto adjacente: '))
#hipotenusa = ((catetooposto ** 2 + catetoadjacente ** 2))**(0.5)
hipotenusa = hypot(catetooposto, catetoadjacente)
print('O valor da hipotenusa é {:.2f}.'.format(hipotenusa))




