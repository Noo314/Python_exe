import time
cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
        'amarelo' : '\033[33m',
        'verde' : '\033[32m',
        'vermelho' : '\033[31m',
        'lilas' : '\033[35m' }

print('{}-=-'.format(cores['azul'])*14)
print('         {}Analisador de Triângulos'.format(cores['amarelo']))
print('{}-=-'.format(cores['azul'])*14)
seg = float(input('{}Primeiro segmento: '.format(cores['lilas'])))
seg_2 = float(input('Segundo segmento: '))
seg_3 = float(input('Terceiro segmento: '))
print('{}Processando...'.format(cores['vermelho']))
time.sleep(2)
if seg < seg_2 + seg_3 and seg_2 < seg_3 + seg and seg_3 < seg_2 + seg:
    print('{}Os segmentos podem formar um triângulo '.format(cores['verde']), end = '' )
    if seg == seg_2 == seg_3:
        print('EQUILÁTERO!')
    elif seg != seg_2 != seg_3 != seg:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmento não formam um triângulo')