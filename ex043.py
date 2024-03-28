print('Cauculo de IMC')
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual sua altura?'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.0f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Parabéns você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está sobre peso do peso ideal')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade morbida,\033[31m Cuidado')


