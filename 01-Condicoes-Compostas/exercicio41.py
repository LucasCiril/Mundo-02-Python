# A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

print('''\nConfederação Nacional de Natação.
Informe o seu ano de nascimento abaixo para ver sua categoria.\n''')

nasc = int(input('Seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print(f'\nVocê tem atualmente {idade} anos.')

if idade <10:
    print('Sua categoria é MIRIM.')
elif idade <15:
    print('Sua categoria é INFANTIL.')
elif idade <20:
    print('Sua categoria é JÚNIOR.')
elif idade <26:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
