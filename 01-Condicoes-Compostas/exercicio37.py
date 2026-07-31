# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# -1 Para Binário, -2 para octal, -3 para Hexadecimal

import sys

print("Este programa faz uma conversão de números.")
num = int(input("Primeiro, escolha um número inteiro: \n"))

if not isinstance(num,int):
    print("Número Inválido! Escolha um número inteiro!")
    sys.exit()
else:
    print('Escolha a base para conversão:\n')
    print('''[1]- Base Binária
[2]- Base Octal
[3]- Base Hexadecimal\n''')

escolha = int(input('Escolha uma das opções acima: '))

if escolha == 1:
    numberbin = bin(num)
    print(f'O número {num} transformado em binário é: {numberbin[2:]}')

elif escolha == 2:
    numberoctal = oct(num)
    print(f'O número {num} transformado em octal é: {numberoctal[2:]}')

else:
    numberhexa = hex(num)
    print(f'O número {num} transformado em hexadecimal é: {numberhexa[2:]}')