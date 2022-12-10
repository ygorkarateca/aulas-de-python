#Criei um programa que leia um número REAL qualquer pelo teclado e
#mostre na tela a sua porcao inteira.

from math import trunc

num = float(input('Digite um valor: '))
num1 = trunc(num)
print(f'O valor real é {num} e sua porcao inteira é {num1}')
