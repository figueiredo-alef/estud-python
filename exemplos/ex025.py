print('=' * 5, 'EX_025', '=' * 5)
# procurando uma string dentro de outra
nome = str(input('Digite seu nome completo: ')).strip()
print('{} >> Seu nome tem Silva!'.format('silva' in nome.lower()))
