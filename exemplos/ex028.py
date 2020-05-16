from random import randint
from time import sleep
print('=' * 5, 'EX_028', '=' * 5)
# jogo da advinhação versão 1
compu = randint(0, 5) # Faz o computador sortear
print('-=-' * 20)
print('Vou sortear um número entre 0 e 5. Tente advinhar!')
print('-=-' * 20)
jogador = int(input('Qual o número foi sorteado pelo computador?\n')) # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == compu:
    print('PARABÉNS! Você venceu.')
else:
    print('GANHEI! Pensei no número {} e não no {}!'.format(compu, jogador))
