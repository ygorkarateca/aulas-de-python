#Um professor quer sortear um dos seus quatros alunos para apagar
#o quadro. Faca um programa que ajude ele, lendo o nome deles e
#escrevendo o nome escolhido

from random import choice
al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))
alunos = [al1, al2, al3, al4]
roleta = choice(alunos)
print(f'O aluno escolhido foi: {roleta}')
