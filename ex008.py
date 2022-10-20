#Escreva um programa que leia um valor em metros
#e o exiba convertido em centimetros e milímetros

medida = float(input('Digite um número: '))
cm = medida * 100
mm = medida * 1000
print('O valor da medida = {}m \nconvertida em {}cm | {}mm'.format(medida, cm, mm))
