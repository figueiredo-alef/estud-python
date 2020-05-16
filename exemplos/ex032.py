from datetime import date
print('=' * 5, 'EX_032', '=' * 5)
ano = int(input('Que ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
