#Escreva um programa que converta uma temperatura
#digitada em °C e converta para °F
#Formula Celsius -> Fahrenheit C = F - 32/1,8
#Formula Celsus -> Kelvin K = C + 273

C = float(input('Informe a temperatura em °C: '))
F = (C * 1.8) + 32
K = C + 273
print(f'A temperatura em Celsius {C}°C \nConvertida em Fahrenheit {F}°F') 
print(f'A temperatura em Celsius {C}°c \nConvertida em Kelvin {K}°K')
