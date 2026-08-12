# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print('-=-' * 10)
print('Calculadora de IMC')
print('-=-' * 10)

peso = float(input('Informe seu peso (em kilos):\n '))
altura = float(input('Informe sua altura (em metros):\n'))

calc = peso / (altura * altura)
print(f'Seu IMC é de: {calc:.2f}\n')

if calc <= 18.5:
    print('Você está abaixo do peso!')
elif calc >= 18.5 and calc <= 25:
    print('Você está no peso ideal!')
elif calc >=25 and calc <= 30:
    print('Cuidado! Você está sobrepeso!')
elif calc >= 30 and calc <= 40:
    print('Hora de se cuidar, você está obeso!')
else:
    print('Procure ajuda, pois seu quadro é de obesidade mórbida!')
