import os

os.system('cls')

preco = float(input('Insira o preço de um produto: '))

desconto = preco * float(0.05)

print('O preço original do produto era R${:.2f}, e com o desconto de R${:.2f} ele vai ficar R${:.2f}'.format(preco, desconto, preco - desconto))