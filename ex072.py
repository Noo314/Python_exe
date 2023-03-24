cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete'
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze'
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número de 0 a 20: '))
if num > 20 or num < 0:
    while True:
        num = int(input('Tente novamente: '))
        if num >= 1 and num <= 20:
            break
print(f'Você digitou o número {cont[num]}')
