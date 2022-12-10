#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentacao de trabalhos dos alunos. Faca um programa que leia
#o nome dos quatros alunos e mostre a ordem sorteada
from random import shuffle

al1 = str(input('Primero aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
alunos = [al1, al2, al3, al4]
shuffle(alunos)
print('Os Alunos sorteados são: ')
print(alunos)
