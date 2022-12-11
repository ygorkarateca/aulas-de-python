#Criei um programa que leia um número inteiro
#e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um valor: '))
resul = num % 2

if resul == 0:
  print('Número é PAR!')
else:
  print('Número é ÍMPAR!')
