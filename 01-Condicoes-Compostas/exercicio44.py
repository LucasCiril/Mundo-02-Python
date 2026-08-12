# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

import sys

print('='*17)
print("Lojas American's")
print('='*17)

sasha = float(input('\nPREÇO DAS COMPRAS: R$'))

print('''\nFORMAS DE PAGAMENTOS: 
[1] À vista em Dinheiro/Cheque
[2] À vista no Cartão
[3] Em até 2x no Cartão
[4] Em 3x ou mais no Cartão''')

options = int(input('\nEscolha uma opção: '))
if options > 4 or options < 1:
    print('OPÇÃO INVÁLIDA!')
    sys.exit()

if options == 1:
    val1 = (sasha * 0.1)
    print(f'Sua compra no valor de R${sasha:.2f} custará R${sasha - val1:.2f}')
elif options == 2:
    val2 = (sasha * 0.05)
    print(f'Sua compra no valor de R${sasha:.2f} custará R$ {sasha - val2:.2f}')
elif options == 3:
    print(f'Sua compra foi parcelada em 2x, sairá no valor normal de R${sasha}')
else:
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela <3:
        print('A parcela precisa ser de, no mínimo, 3x.')
        sys.exit()
    juros = (sasha * 0.2)
    calc = (sasha/parcela) + (juros/parcela)
    print(f'Sua compra será parcelada em {parcela}x de R${calc:.2f} COM JUROS!')
    print(f'Sua compra de R${sasha:.2f} sairá por R${sasha + juros:.2f}')
