# Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opc = None
while opc != 5:
    print('-=-' *8)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opc = int(input('>>>>> Qual sua opção? '))
    if opc == 1:
        soma = valor1 + valor2
        print(f' A soma de {valor1}+{valor2} resulta em {soma}')
        sleep(3)
    elif opc == 2:
        mult = valor1 * valor2
        print(f'A multiplicação de {valor1}x{valor2} resulta em {mult}')
        sleep(3)
    elif opc == 3:
        if valor1 > valor2:
            print(f'O número {valor1} é maior que {valor2}')
        else:
            print(f'O núemro {valor2} é maior que {valor1}')
        sleep(3)
    elif opc == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        sleep(3)
    elif opc == 5:
        print('Finalizando...')
        sleep(3)
    else:
        print('Opção inválida, tente novamente!')
print('Fim do programa, volte sempre!')
