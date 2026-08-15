# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = None

for i in range(1 , 6):
    peso = float(input(f'O peso da {i}ª pessoa: '))
    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso

print(f'Maior peso informado: {maior:.2f}')
print(f'Menor peso informado: {menor:.2f}')
