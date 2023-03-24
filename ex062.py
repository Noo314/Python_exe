print('-='*20)
print('PROGRESSÃO ARITMÉTICA v(².⁰)')
print('-='*20)
pri_termo = int(input('Qual o primeiro termo da pa? '))
razão = int(input('Qual a razão da pa? '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        pri_termo += razão
        print('{}'.format(pri_termo), end=' -> ')
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer ver mais quantos termos? '))