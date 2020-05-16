from math import radians, sin, cos, tan
print('=' * 5, 'EX_018', '=' * 5)
# seno, cosseno, tangente
ang = float(input('Digite o angulo desejado: '))
seno = sin(radians(ang))
print('O angulo de {} tem SENO de {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print('O angulo de {} tem COSSENO de {:.2f}'.format(ang, coss))
tang = tan(radians(ang))
print('O angulo de {} tem TANGENTE de {:.2f}'.format(ang, tang))
