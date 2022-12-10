#Escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milímetros

medida = float(input('Digite em metros: '))
print(f'O valor da medida = {medida}m ')
print(f'Convertidos em {medida * 10}dm | {medida * 100}cm | {medida * 1000}m')
print(f'{medida / 10}dam | {medida / 100}hm | {medida / 1000}km')
