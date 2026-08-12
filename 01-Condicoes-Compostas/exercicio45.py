# Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time 

print('-=-' *10)
print('JOKENPO')
print('-=-' *10)

print('''\nEscolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

escolha = int(input('\nQual a sua jogada? '))
escolhanpc = random.randint(0,2)
itens = ('Pedra', 'Papel', 'Tesoura')

print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!')

print('-=-' *9)
print(f'Computador jogou {(itens[escolhanpc])}')
print(f'Jogador jogou {(itens[escolha])}')
print('-=-' *9)

if escolhanpc == 0:
    if escolha == 0:
        print('EMPATE!')
    elif escolha == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
elif escolhanpc == 1:
    if escolha == 0:
        print('COMPUTADOR VENCEU!')
    elif escolha == 1:
        print('EMPATE!')
    else:
        print('JOGADOR VENCEU!')
else:
    if escolha == 0:
        print('JOGADOR VENCEU!')
    elif escolha == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('EMPATE!')
