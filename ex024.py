#Crie um programa que leia o nome de uma cidade e diga se ela
#comeca ou não com o nome " Santo ".

cid = str(input('Qual a cidade que você nasceu: ')).strip()

print(cid[:5].upper() == 'SANTO')
