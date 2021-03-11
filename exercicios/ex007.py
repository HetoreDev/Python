import os

os.system('cls')

n1 = float(input('Digeite a primeira nota: '))
n2 = float(input('Digete a segunda nota: '))

media = (n1+n2)/2

print('Com a 1ª nota {:.1f} e a 2ª nota {:.1f} a média foi {:.1f}'.format(n1, n2, media))