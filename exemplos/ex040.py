# Aquele clássico da Média

print('=' * 5, 'EX_040', '=' * 5)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

med = (n1 + n2 + n3) / 3

if med >= 7.3:
    print('Média {:.2f}, APROVADO!'.format(med))
elif med <= 6:
    print('Média {:.2f}, REPROVADO!'.format(med))
elif 6 < med < 7.3:
    print('Média {:.2f}, RECUPERAÇÃO!'.format(med))
