from time import sleep
import math
cores = {'limpa' : '\033[m',
        'azul' : '\033[34m',
        'amarelo' : '\033[33m',
        'verde' : '\033[32m',
        'vermelho' : '\033[31m',
        'lilas' : '\033[35m' }

casa = float(input('{}Valor da casa: '.format(cores['amarelo'])))
salário = float(input('{}Salário do comprador: '.format(cores['azul'])))
anos = int(input('{}Quantos anos de financiamento? '.format(cores['amarelo'])))*12
print('{}Processando...'.format(cores['lilas']))
sleep(3)
prest = casa/anos
print('{}Para pagar uma casa de R${:.2f} em {} meses a prestação será de R${:.2f}'.format(cores['azul'],casa,anos,prest))
if 30/100 * salário >= prest:
    print('{}Empréstimo Aceito!!!'.format(cores['verde']))
elif 30/100 * salário < prest:
    print('{}Empréstimo Negado!!!'.format(cores['vermelho']))
    
