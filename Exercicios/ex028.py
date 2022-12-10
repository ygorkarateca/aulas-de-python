#Escreva um programa que faça o computador "pensar" em um
#número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O Programa deverá
#escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num = randint(0, 10)
play = int(input('Escolha um número para advinhar: '))
print('Processando....')
sleep(2)

if play == num:
    print(f'Você ganhou! - Número escolhido pelo computador foi = {num}')
else:
    print(f'Você perdeu! - Número escolhido pelo computador foi = {num}')
