print('=' * 5, 'AULA_010b', '=' * 5)
p1 = float(input('Qual a nota da P1? '))
p2 = float(input('Qual a nota da P2? '))
p3 = float(input('Qual a nota da P3? '))
m = (p1 + p2 + p3) / 3
print('A sua média foi: {:.2f}'.format(m))
if m >= 7.0:
    print('Parabéns, você foi aprovado!')
else:
    print('Média insuficiente para aprovação!')
