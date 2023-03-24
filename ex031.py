from time import sleep
via = float(input('Qual é o tamanho da viagem? '))
print(via)
print('Calculando...')
sleep(2)
if via < 200:
    price = via * 0.50
    print('O preço da viajem vai ser de R${:1f}!'.format(price))
else:
    price = via * 0.45
    print('O preço da viajem vai ser de R${:1f}!'.format(price))


