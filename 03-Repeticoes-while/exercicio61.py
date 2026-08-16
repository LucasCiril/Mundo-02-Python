# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' *20)
print('10 TERMOS DE UMA PA')
print('=' *20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
x = termo
while cont <=10:
    print(x, end=' -> ')
    x += razao
    cont += 1
print('Acabou')