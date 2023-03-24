cont = 0
num = int(input('\033[35mDigite um numero: '))
for c in range (1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c),end=' ')
if cont > 2:
    print('\nO número {} foi divisivel {} vezes \npor isso ele \033[31mNÃO É UM NUMERO PRIMO!!! '.format(num,cont))
elif cont == 2: 
    print('\nO número {} é divisivel apenas por 1 e \nele mesmo então ele \033[32mÉ UM NÚMERO PRIMO!!! '.format(num))