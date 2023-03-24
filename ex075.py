num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))
number = [num1,num2,num3,num4]
if 3 in number:
    print(f'O número 3 apareceu na {number.index(3)+1}ª posição.')
else:
    print('O número 3 não apareceu em nenhuma posição.')
print(f'O número 9 apareceu {number.count(9)} vezes.')
for n in number:
    if n % 2 == 0:
        print(f'Os números pares digitados foram {n}', end=' ')