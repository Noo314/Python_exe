num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))
numbers = [num1, num2, num3, num4]
print(f'O número 9 apareceu {numbers.count(9)} vezes.')
if 3 in numbers:
    print(f'O número 3 apareceu na {numbers.index(3)}ª posição.')
else:
    print('Não foi digitado nenhum número 3.')
for n in numbers:
    if n % 2 == 0:
        print(f'Os valores pares foram {n}',end=' ')
    else:
        print('Não teve nenhum número par.')