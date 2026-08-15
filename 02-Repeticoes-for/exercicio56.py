# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = mulher_idade = 0
homem_idade = mais_velho = None

for i in range(1,5):
    print(f'----- {i}ª PESSOA -----')

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F] ')).strip()
    media += idade

    if sexo in 'Mm':
        if homem_idade is None or idade > homem_idade:
                homem_idade = idade
                mais_velho = nome

    if sexo in 'Ff':
         if idade <20:
              mulher_idade +=1
         
media = (media) / 4        
print(f'A média de idade do grupo é de {media:.1f} anos;')
print(f'O homem mais velho tem {homem_idade} anos e se chama {mais_velho}; ')
print(f'Ao todo, {mulher_idade} mulher(es) tem menos de 20 anos.')
