#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h. Mostra uma mensagem
#dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

km = int(input('Qual a velocidade? '))
multa = (km - 80) * 7
print('Analisando.....')
sleep(1)

if km <= 79:
  print('Ótimo, você está dentro da velocidade')
else:
  print(f'Você está acima da velocidade de {km}Km/h \nE você será multado em R${multa:.1f}')
