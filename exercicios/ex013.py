import os

os.system('cls')

salario = float(input('Insira o valor do seu atual salário: '))

print('Seu salário era de R${:.2f} e com 15% de aumento vai ficar R${:.2f}'.format(salario, salario * 1.15))