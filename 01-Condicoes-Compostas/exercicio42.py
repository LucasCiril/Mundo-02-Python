# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

# Acrescente o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
import sys

print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)

a = float(input('Informe o primeiro segmento: '))
b = float(input('Informe o segundo segmento: '))
c = float(input('Informe o terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos FORMAM um triângulo!')
    if a == b and b == c:
        print('O Triângulo formado é Equilátero!')
    elif a != b != c != a:
        print('O triânuglo formado é Escaleno!')
    else:
        print('O triângulo formado é Isósceles!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')
    sys.exit()



