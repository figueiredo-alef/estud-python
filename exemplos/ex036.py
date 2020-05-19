# aprovando empréstimos

print('=' * 5, 'EX_036', '=' * 5)

casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o seu salário atual? R$'))
ano = float(input('Em quantos anos pretende pagar? '))

parcela = ano * 12

valorparcela = casa / parcela
limite = salario * (30 / 100)

if limite >= valorparcela:
    print('EMPRÉSTIMO APROVADO!\n{} parcelas de R${:.2f}.'.format(parcela, valorparcela))
else:
    print('EMPRÉSTIMO NEGADO!')
