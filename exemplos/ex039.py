# alistamento militar

from datetime import date

print('=' * 5, 'EX_039', '=' * 5)

anoatual = date.today().year

print('''Qual o seu gênero?
[ 1 ] Masculino
[ 2 ] Feminino''')

gen = int(input('Digite o número correpondente: '))

if gen == 1:

    nasc = int(input('Ano de nascimento: '))

    idade = anoatual - nasc

    print('Você tem {} anos.'.format(idade))

    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE.')

    elif idade < 18:
        saldo = 18 - idade
        print('Faltam {} anos para o alistamento.'.format(saldo))
        alist = anoatual + saldo
        print('Seu alistamento será em {}.'.format(alist))

    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos.'.format(saldo))
        alist = anoatual - saldo
        print('Seu alistamento foi em {}.'.format(alist))

elif gen == 2:
    print('Você não precisa fazer o alistamento.')

else:
    print('Opção inválida.')
