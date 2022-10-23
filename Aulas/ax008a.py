#Modúlos em PYTHON
"""
import -> Importa toda funcionalidade de uma biblioteca
from -> Selecionar algumas das funcões que uma biblioteca possui
"""

#Biblioteca - Math
"""
ceil -> Faz um arredondamento para +
floor -> Faz um arredondamento para -
trunc -> Elimina qualquer valor depois da ,
pow -> Calcula potência dos valores
sqrt -> Calcula a RaizQ
factorial -> Fatoração de valores
"""

import math 
num = float(input('Digite um valor: '))
pot = math.pow(num , 2)
raiz = math.sqrt(num)
print(f'Valor da RaizQ {raiz:.2f} e Potência {pot}')
