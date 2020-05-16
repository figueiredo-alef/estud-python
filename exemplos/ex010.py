print('=' * 5, 'EX_010', '=' * 5)
# conversor de moedas
real = float(input('Quantos Reais você tem? R$'))
dolar = real / 5.15 # dólar em 19/03/2020
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
