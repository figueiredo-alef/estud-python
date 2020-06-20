# Índice de massa corporal (adaptado)

print('=' * 5, 'EX_043', '=' * 5)

massa = float(input('Qual é a sua massa? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = massa / (altura ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Está na faixa adequada de peso.')
elif 25 <= imc < 30:
    print('Está em sobrepeso.')
elif 30 <= imc < 40:
    print('Está em obesidade.')
elif imc >= 40:
    print('Está em obesidade morbida.')
