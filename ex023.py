#Faca um programa que leia um número de 0 a 9999 e mostre na tela
#cada um dos digitos separados. Segue o exemplo!
"""
Digite um número: 1834
unidade: 4 dezena: 3 centena: 8 milhar: 1
"""


num = int(input('Informe um número: '))

print(f'Analisando o numero = {num}....')
print(f'Unidade = {num // 1 % 10}\nDezena = {num // 10 % 10}\nCentena = {num // 100 % 10}\nMilhar = {num // 1000 % 10}')
