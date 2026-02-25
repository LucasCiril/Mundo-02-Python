#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salario = float(input('Informe o salário do pagador: '))
anos = int(input('Em quantos anos vai ser pago?: '))

prestacao = casa / (anos * 12)

print(f'A prestação da casa ficará: {prestacao:.3f} R$')
