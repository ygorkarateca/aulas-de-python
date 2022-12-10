#Crie um programa que leia o nome completo de uma pessoa e mostre:
"""
> O nome com todas as letras maiúsculas
> O nome com todas minúsculas
> Quantas letras ao todos(Sem considerar espacos)
> Quantas letras tem o primeiro nome

"""

nome = str(input('Digite um nome completo: ')).strip()
espaco = nome.count(' ')
primeiro = nome.find(' ')

print(f'Exemplo1 -> {nome.upper()}')
print(f'Exemplo2 -> {nome.lower()}')
print(f'Nome contém total caracteres: {len(nome)} e sem espacos: {len(nome) - espaco} letras')
print(f'Primeiro nome contém total de caracteres: {primeiro} letras')