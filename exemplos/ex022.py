print('=' * 5, 'EX_022', '=' * 5)
# analisador de texto
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'. format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
divide = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(divide[0], len(divide[0])))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
