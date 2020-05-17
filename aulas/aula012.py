# Condições aninhadas
print('#' * 5, '\033[1;32mAULA_012\033[m', '#' * 5)
nome = str(input('Qual o seu nome?\n'))
if nome == 'Alef':
    print('Uau, que nome lindo!')
elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
