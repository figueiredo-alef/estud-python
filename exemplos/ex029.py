print('=' * 5, 'EX_029', '=' * 5)
# radar aletrônico
vel = float(input('Qual a velocidade do carro?\n'))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h.')
    multa = (vel - 80) * 7
    print('Você pagará uma multa no valor de R${:.2f}!'.format(multa))
print('Tenha um bom dia. Dirija com segurança.')
