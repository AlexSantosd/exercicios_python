nome = str(input('qual o seu nome?'))
if nome =='Alex':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Claúdia Ana Paula Jéssica':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))
