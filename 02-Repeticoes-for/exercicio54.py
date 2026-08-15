# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a 
# maioridade e quantas já são maiores.
from datetime import date

contup = 0
contdown = 0
ano_atual = date.today().year

for i in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {i}ª pessoa: '))
    idade = ano_atual - nasc
    if idade >= 18:
        contup += 1
    elif idade <= 18:
        contdown += 1
print(f'{contup} pessoas atingiram a maioridade.')
print(f'{contdown} pessoas ainda são menores de idade.')
