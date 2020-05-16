print('=' * 5, 'EX_031', '=' * 5)
distancia = float(input('Qual a distância da sua viagem?\n'))
print('Ok. Sua viagem é de {:.2f}km. Veja o custo abaixo:'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('R${:.2f} conforme distância informada.'.format(preco))
