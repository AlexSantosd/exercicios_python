from math import sin, cos, tan, radians  #import math
print('Calculo seno, cosseno e tangente')
angulo = float(input('Digite um angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seno de {} é {:.2f} '.format(angulo, sen))
print('O cosseno de {} é {:.2f} '.format(angulo, cos))
print('A tangente de {} é {:.2f} '.format(angulo, tan))


