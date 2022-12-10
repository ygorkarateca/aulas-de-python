#Faca um algoritmo que leia o sálario de um funcionário
#e mostre seu novo salário, com 15% de aumento.

sal = float(input('O salário do funcionario é R$:'))
nsal = sal + (sal * (15 / 100))
print(f'O Salário antigo R${sal:.1f}\nE com reajuste de 15% - R${nsal:.2f}')
