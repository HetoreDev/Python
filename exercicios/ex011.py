import os

os.system('cls')

altura = float(input('Insira a altura da parede: '))
largura = float(input('Insira a lagura da parede: '))

area = altura * largura
tinta = area / float(2)

print('A sua parede tem uma área de {:.2f}m², e para tanto precisa de {:.2f}l de tinta'.format(area, tinta))