from time import sleep
num = int(input('Digite um numero qualquer: '))
print('Processando...')
sleep(2)
if num % 2 == 0:
    print('O numero {} é par!'.format(num))
else:
    print('O numero {} é impar!'.format(num))