import os

os.system('cls')

dia = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))


print('\nTotal por {} dias de aluguel R${:.2f}\nTotal por {} Km rodados R${:.2f}\nTotal geral R${:.2f}'.format(dia, dia*60, km, km*0.15, (dia*60) + (km*0.15)), '\n')

# dia 60 km 0,15