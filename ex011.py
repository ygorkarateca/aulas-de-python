#Faca um programa que leia a largura e a altura de uma parede em
#metros, calcule a sua área e a quantidade de tinta necessária para
#pinta-lá, sabendo que a cada litro de tinta, pinta uma área de 2m².

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual altura da parede? '))
area = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} e a sua area é de {area}m²')
print(f'O total de litros de tinta que você precisará para pintar sua parede é {area / 2}l')
