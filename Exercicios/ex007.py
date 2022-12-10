#Desenvolva um programa que leia as duas notas
#de um aluno, calcule e mostre sua média

aluno  = input('Digite o NOME do ALUNO: ')
nota1 = float(input('Digite a Primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))
media = float((nota1 + nota2) / 2)

print('O aluno: {}, possui notas {} | {}'.format(aluno, nota1, nota2))
print('Média é = {}'.format(media))