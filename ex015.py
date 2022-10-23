#Escreve um programa que pergunte a quantidade de KM
#percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por KM rodado.

Aluguel = int(input('Quanto tempo de alugado? '))
KM = float(input('Quantidade de KM percorrido? '))
pago = (Aluguel * 60) + (KM * 0.15)
print(f'Total a pagar pelo serviço é - R${pago}')
