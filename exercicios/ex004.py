import os

os.system('cls')

v = input('Digite algo: ')

print('Qual o tipo primitivo dete conteúdo? {}'.format(type(v)))
print('O conteúdo {}'.format(v),' é numérico? ',v.isnumeric())
print('O conteudo {}'.format(v),' é alfabético? ',v.isalpha())
print('O Conteúdo {}'.format(v),' é alfanumérico? ', v.isalnum())
print('O Conteúdo {}'.format(v),' está em maiúsculo? ', v.isupper())
print('O Conteúdo {}'.format(v),' está em minúsculo? ', v.islower())
print('O Conteúdo {}'.format(v),' está capitalizado? ', v.istitle())
