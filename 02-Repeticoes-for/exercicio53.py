# Crie um programa que leia uma frase qualquer 
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper().split()
frjunta = ''.join(frase)
inverso = ''

for i in range(len(frjunta) - 1, -1, -1):
    inverso +=frjunta[i]

if inverso == frjunta:
    print(f'A frase é um palíndromo.')
else:
    print(f'A frase não é um palíndromo.')
