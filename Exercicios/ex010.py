#Criei um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos DÓLARES ela pode comrpar
#Faca a conversão com valor do DOLAR atual

real = float(input('Quando você possui na carteira R$: '))
print(f'Total em REAL R${real:.2f}')
print(f'Convertendo em US$ = {real/5.24:.2f} | € = {real/5.13:.2f}')
