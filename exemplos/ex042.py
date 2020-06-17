# Analisador de Triângulos v2.0

print('=' * 5, 'EX_042', '=' * 5)

print('-=' * 20)
print('Analisador de triangulos - v2.0')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triangulo!')
