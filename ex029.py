#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem
#dizendo que ele foi multado.
#A multa vai cusatr R$7,00 por cada km acima do limite


km = float(input('Qual a foi a sua velocidade:'))
multa = (km - 80) * 7

if km <= 79:
  print('Você está dentro da velocidade recomendada, tenha um bom dia!')
else:
  print(f'Você está acima da velocidade: {km:.0f}Km/h\nVocê será multado em R${multa:.1f}')
