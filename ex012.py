#Faca um algoritmo que leia o preço de um produto
#e mostre seu novo preco, com 5% de desconto.

item = float(input('Valor do produto custa é R$:'))
print(f'O valor do produto sem desconto é R${item} \nE com desconto de 5% é R${item - (item * 5/100):.2f}')
