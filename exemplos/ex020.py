from random import shuffle
print('=' * 5, 'EX_020', '=' * 5)
# sorteando uma ordem na lista
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação é:\n{}'.format(lista))
