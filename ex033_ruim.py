num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
if num1 > num2 and num2 > num3:
    print('O numero {} é o maior'.format(num1))
    print('O numero {} é o intermediario'.format(num2))
    print('E o numero {} é o menor'.format(num3))
elif num3 > num2 and num2 > num1:
    print('O numero {} é o maior'.format(num3))
    print('O numero {} é o intermediario'.format(num2))
    print('E o numero {} é o menor'.format(num1))
elif num2 > num1 and num1 > num3:
    print('O numero {} é o maior'.format(num2))
    print('O numero {} é o intermediario'.format(num1))
    print('E o numero {} é o menor'.format(num3))
elif num3 > num1 and num1 > num2:
    print('O numero {} é o maior'.format(num3))
    print('O numero {} é o intermediario'.format(num1))
    print('E o numero {} é o menor'.format(num2))
elif num1 > num3 and num3 > num2:
    print('O numero {} é o maior'.format(num1))
    print('O numero {} é o intermediario'.format(num3))
    print('E o numero {} é o menor'.format(num2))
else:
    print('O numero {} é o maior'.format(num2))
    print('O numero {} é o intermediario'.format(num3))
    print('E o numero {} é o menor'.format(num1))