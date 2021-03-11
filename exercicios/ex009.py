import os

os.system('cls')

n = int(input('Insira o número para ver a sua tabuada: '))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, i * n))
