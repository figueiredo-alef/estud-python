print('=' * 5, 'EX_027', '=' * 5)
# primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Analisando seu nome...')
print('Seu primeiro nome é: {}.'.format(n[0]))
print('Seu último nome é: {}.'.format(n[len(n) - 1]))
