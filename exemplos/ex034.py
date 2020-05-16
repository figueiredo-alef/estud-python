print('=' * 5, 'EX_034', '=' * 5)
# aumentos múltiplos
salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('O funcionário recebia R${:.2f} e passa a receber R${:.2f}'.format(salario, aumento))
