#Faca um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente
"""
ex > Ana Maria de Souza
Primeiro = Ana
Último = Souza

"""

nome = str(input('Digite seu nome completo: ')).strip()
nome2 = nome.split()

print(f'Prazer em conhece-lo(a)!\nSeu primeiro nome é: {nome2[0]}')
print(f'E útimo nome é: {nome2[len(nome2)-1]}')
