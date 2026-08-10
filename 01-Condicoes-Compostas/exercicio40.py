# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

import sys

print('''\nCalculadora de notas IFRN
Informe as suas duas notas bimestrais.\n''')

nota1 = float(input('Primeiro bimestre: '))
nota2 = float(input('Segundo bimestre: '))

if nota1 or nota2 < 0:
    print('Nota Inválida. Informe uma nota válida.')
    sys.exit()
elif nota1 or nota2 > 10:
    print('Nota Inválida. Informe uma nota válida.')
    sys.exit()

media = (nota1 + nota2) / 2
print(f'Sua média é de {media}')

if media < 5.0:
    print('Infelizmente, você está reprovado.')
elif media > 4.9 and media <7:
    print('Você está na recuperação, estude!')
else:
    print('Você está aprovado!')
