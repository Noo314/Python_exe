print('-='*20)
print('PROGRESSÃO ARITMÉTICA v(².⁰)')
print('-='*20)
pri_termo = int(input('Qual o primeiro termo da pa? '))
razão = int(input('Qual a razão da pa? '))
dez_termo = pri_termo + (10 - 1) * razão
while pri_termo < dez_termo + 1:
    pri_termo += razão
    print('{}'.format(pri_termo), end=' -> ')
print('FIM')