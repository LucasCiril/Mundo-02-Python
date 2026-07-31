# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('Serviço Militar Obrigatório.\n')
nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
x = ano_atual - nascimento

print(f'Sua idade atual é {x} anos.\n')

if x < 18:
    saldo = 18 - x
    print(f'Fique calmo, Recruta! Sua hora ainda vai chegar. Você se alista em {saldo} ano(s).')
elif x > 18:
    saldo = x - 18
    print(f'''Eita monstro, esqueceu do servir o Glorioso Exército Brasileiro? Seu tempo já passou!
Deveria ter se alistado há {saldo} ano(s). ''')
else:
    print('Sentar 1 2, de pé 1 2! Você está apto para o alistamento!')
