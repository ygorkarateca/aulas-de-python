#Faça um programa que leia algo pelo teclado e mostre na tela seu
#tipo primitivos e toda as informações possíveis sobre ela

n = input('Digite algo: ')
print('É Letra ?', n.isalpha())
print('É Número ?', n.isalnum())
print('É Alfanumerico? ', n.isalnum())
print('Pode ser usando como titulo? ', n.istitle)