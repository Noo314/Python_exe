c = 0
soma = 0
cont = 0
c = int(input('Digte um número [999 para parar]: '))
while c != 999:
    soma += c
    cont += 1
    c = int(input('Digte um número [999 para parar]: '))
print('A soma dos {} números é igual a {}!'.format(cont,soma))