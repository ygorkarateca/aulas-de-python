#Faca um programa que leia o comprimento do
#cateto oposto e do cateto adjacente de um
#triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print(f'Valores do cateto oposto / adjacente é: {co} | {ca}')
print(f'Que tem a hipostenusa {hypot(co, ca):.2f}')
