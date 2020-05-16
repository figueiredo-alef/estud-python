print('=' * 5, 'EX_033', '=' * 5)
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior
maior = a
if b > a and b > c:
    b = maior
if c > a and c > b:
    c = maior
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
