# cores no terminal
# ANSI (escape sequence) > \033[m
print('=' * 5, '\033[1;32mAULA_011\033[m', '=' * 5)
print('\033[1;36;40mOlá, pequeno gafanhoto!\033[m')

a = 5
b = 3
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))

nome = 'Alef Figueiredo'
print('Olá, {}{}{} !'.format('\033[4;34;40m', nome, '\033[m'))
