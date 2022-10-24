#Faca um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e
#tangente desse ângulo.


from math import cos, sin, tan, radians
angulo = float((input('Digite o valor do ângulo: ')))
print(f'O ângulo de {angulo} tem o SENO = {cos(radians(angulo)):.2f} / COSSENO = {sin(radians(angulo)):.2f} / TANGENTE = {tan(radians(angulo)):.2f}')
