#Faca um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e
#tangente desse ângulo.


from math import acos, asin, atan, radians
angulo = float((input('Digite o valor do ângulo: ')))
print(f'O ângulo de {angulo} tem o SENO = {acos(radians(angulo)):.2f} / COSSENO = {asin(radians(angulo)):.2f} / TANGENTE = {atan(radians(angulo)):.2f}')
