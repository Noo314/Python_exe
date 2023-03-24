import random
cont = 0
print('Eae, sou eu o pc ')
rand = random.randint(0,10)
print('Eu acabei de pensar em um número de 0 a 10.')
print(rand)
num = int(input('Tente advinhar: '))
while num != rand:
    if rand > num:
        num = int(input('Mais tente mais uma vez: '))
        cont += 1
    else:
        num = int(input('Menos tente mais uma vez: '))
        cont += 1
print('Você acertou parabêns você tentou {} vezes'.format(cont))
