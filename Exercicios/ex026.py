#Faca um programa que leia uma frase pelo teclado e mostre:
"""
>Quantas vezes aparece a letra 'A'.
>Em que posicao ela aparece a primeira vez.
>Em que posicao ela aparece a última vez.
"""

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aprece = {frase.count("A")}x')
print(f'Primeira vez que a letra "A" aprece é = {frase.find("A")+1}')
print(f'Última vez que a letra "A" aprece é = {frase.rfind("A")+1}')
print(f'Essa frase tem no total de = {len(frase)}')
