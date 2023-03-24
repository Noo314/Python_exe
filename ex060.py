fat = int(input('Digite o número para \ncalcular o fatorial: '))
soma = 1
print('Calculando fatorial de {}! = '.format(fat),end='')
for c in range (fat, 0 , -1):
    soma *= c
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end='')
print('{}'.format(soma))
