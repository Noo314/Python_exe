import random
numbers = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
print('Os números sorteador foram:', end=" ")
for n in numbers:
    print(n, end=" ")
print(f'\nO maior número sorteado foi {max(numbers)}!')
print(f'O menor número sorteado foi {min(numbers)}!')