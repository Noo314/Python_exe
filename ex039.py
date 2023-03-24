from datetime import date
ano = int(input('Qual ano você nasceu? '))
idade = date.today().year - ano
if idade > 18:
    tempo = idade - 18
    da = date.today().year - tempo
    print('Você tem {} e deveria ter se alistado a {} anos atrás'.format(idade,tempo))
    print('E seu alistamento foi {}'.format(da))
elif idade < 18:
    tempo = 18 - idade
    da = date.today().year + tempo
    print('Você tem {} anos e deverá se alistar em {} anos'.format(idade,tempo))
    print('seu alistamento vai ser no ano de {}'.format(da))
else:
    print('Você tem {} anos e tem que ser alistar IMEDIATAMENTE!!!'.format(idade))