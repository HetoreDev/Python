import os

os.system('cls')

real = float(input('Insira a quantidade de reais que você tem? R$'))
cotacao = float(input('Qual a cotação do dolár de hoje: '))

dolar = real / cotacao

print('Com R${:.2f} pela cotação de US${:.2f}, você pode comprar US${:.2f}'.format(real, cotacao, dolar))