print('=' * 5, 'EX_014', '=' * 5)
# conversor de temperaturas
temp = float(input('Qual a temperatura em ºC? '))
far = (temp * 9 / 5) + 32
kel = temp + 273.15
print('A temperatura {:.2f}C corresponde a {:.2f}F e a {:.2f}K'.format(temp, far, kel))
