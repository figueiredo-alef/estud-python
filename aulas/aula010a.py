print('=' * 5, 'AULA_010a', '=' * 5)
tempo = int(input('Quantos anos tem seu carro?\n'))
if tempo <= 3:
    print('Carro novo!')
else:
    print('Carro velho!')
print('-- FIM --')
print('Abaixo uma maneira diferente de executar função similar do exemplo acimaS')
t = int(input('Quantos anos tem seu carro?\n'))
print('carro novo.'if t <= 3 else 'carro velho.')
print('-- FIM --')
