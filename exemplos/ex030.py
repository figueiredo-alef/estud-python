print('=' * 5, 'EX_030', '=' * 5)
numero = int(input('Me diga um númeor qualquer: '))
result = numero % 2
# print('O resultado foi: {}'.format(result)) # teste para verificar se é par
if result == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))
