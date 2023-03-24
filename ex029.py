vel = int(input('Qual a sua velocidade? '))
if vel < 80:
    print('Tudo certo! dirija com cuidado.')
else:
    multa = (vel - 80) * 7
    print('Você excedeu o limite de 80km \nvocê foi multado em R${}'.format(multa))