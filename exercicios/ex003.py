import os

os.system('cls')

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

soma = n1 + n2

print('A soma de {0} e {1} é igual a {2}'.format(n1, n2, soma))


# os.system('cls' if os.name == 'nt' else 'clear')
