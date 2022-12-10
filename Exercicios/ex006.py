#Crie um algoritmo que leia um número
#e mostre o seu dobro, triplo e RaizQ

n = int(input('Digite um número: '))
print('O Dobro é = {}\nE Triplo é = {}\nE a Raiz Quadrada é = {:.1f}'.format((n * 2), (n * 3), (n ** (1/2))))