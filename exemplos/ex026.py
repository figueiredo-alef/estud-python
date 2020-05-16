print('=' * 5, 'EX_026', '=' * 5)
# primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra [A] aparece {} vezes na frase informada.'.format(frase.count('a')))
print('A letra [A] aparece pela primeira vez na posição {}.'.format(frase.find('a') + 1))
print('A letra [A] aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))
