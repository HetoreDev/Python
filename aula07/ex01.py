import os

os.system('cls')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digeite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2

print('A soma é {}, o produto é {}, a divisão é {:.2f}'.format(s, m, d))# {:.2f} vai formatar a saída para duas casas decimais após o ponto, f para saída de ponto flutuante
print('A divisão inteira é {}, e a exponenciação é {}'.format(di, e))