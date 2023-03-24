from math import hypot
caop = float(input('Insira o tamanho do cateto oposto: '))
caad = float(input('Insira o tamanho do cateto adjacent: '))
hi = hypot(caop, caad)
print('A hipotenusa é {:.2f}'.format(hi))