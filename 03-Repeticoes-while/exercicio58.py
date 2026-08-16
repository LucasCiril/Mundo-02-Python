# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
# em um número entre 0 e 10. Só que agora o jogador vai 
# tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

sorteado = randint(1,10)
cont = 0

print('----- Jogo da Adivinhação -----')
print('Eu pensei em um número de 1 a 10. Tente adivinha qual é!')
tent = int(input('Qual número você escolhe? '))

while tent != sorteado:
    if tent < sorteado:
        tent = int(input('Mais... Tente mais alto! '))
        cont += 1
    if tent > sorteado:
        tent = int(input('Menos... Um pouco mais baixo! '))
        cont += 1
    if tent == sorteado:
        print(f'Parabéns! Eu pensei no número {sorteado}!!')
        print(f'Foram precisas {cont} tentativas para acertar, parabéns!')
