# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120


print('\nEste programa resolve fatoriais:\n ')
fat = int(input('Número para fatorial: '))
x = 1
while fat > 0:
    print(f'{fat}', end='')
    print(' x ' if fat > 1 else ' = ', end='')
    x *= fat
    fat -= 1
print(f'{x}')
