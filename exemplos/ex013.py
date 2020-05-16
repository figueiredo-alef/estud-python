print('=' * 5, 'EX_013', '=' * 5)
sal = float(input('Salário atual: R$'))
novo = sal + (sal * 15 / 100)
print('Você receberá R${:.2f} (R${:.2f} + 15%)'.format(novo, sal))
