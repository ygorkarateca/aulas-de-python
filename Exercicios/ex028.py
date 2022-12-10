#Escreva um programa que faça o computador "pensar" em um
#número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O Programa deverá
#escrever na tela se o usuário venceu ou perdeu.

from random import randint

num = randint(0, 10)
jogador = int(input('Escolha um número para advinhar: '))
print(num)

if num == jogador:
    print('Você ganhou!')
else:
    print('Você perdeu!')
