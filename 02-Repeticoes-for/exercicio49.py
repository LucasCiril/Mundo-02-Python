# Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Escolha um número para ver sua tabuada: '))
cont = 0
for i in range(1, 11):
    cont = num * i
    print(f'{num} x {i} = {cont}')
