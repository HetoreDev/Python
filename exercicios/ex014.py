import os

os.system('cls')

c = float(input('Insira a sua temperatura em °C:'))

f = ((c * 9) / 5) + 32

print('A temperatura de {}°C equivalem a {}°F'.format(c,f))

#(25 °C × 9/5) + 32 = 77 °F
