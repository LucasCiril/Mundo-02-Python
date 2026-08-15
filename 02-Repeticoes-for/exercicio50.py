# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for i in range(1, 7):
    num = int(input('Informe os seis números: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'Você informou {cont} números pares e teve como resultado da soma: {soma}')
