#Desenvolva um programa que pergunte a distância de uma viagem
#em KM. Calcule o preco da passagem, cobrando R$0,50 por Km para
#viagem de até 200Km em R$0,45 para viagem mais longas.

from time import sleep

transp = float(input('Digite a distância da viagem: '))
print(f'Sua vaigem de {transp}Km')
sleep(2)

if transp <= 200:
    print(f'O valor da passagem será R${transp * 0.50:.2f}')
else:
    print(f'O valor da passagem será R${transp * 0.45:.2f}')
