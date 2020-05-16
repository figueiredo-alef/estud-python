print('=' * 5, 'EX_011', '=' * 5)
# pintando parede
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print('Sua parede é de {}x{} e sua área é de {:.2f}m².'.format(lar, alt, area))
lit = area / 2
print('Serão necessários {:.2f}l de tinta para pintar essa parede.'.format(lit))
