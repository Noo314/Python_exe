from time import sleep
from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano
print('Processando...')
sleep(1)
if idade <= 9 and idade > 0:
    print('O atleta tem {} anos.\nClassificação: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos.\nClassificação: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos.\nClassificação: JÚNIOR'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos.\nClassificação: SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos.\nClassificação: MASTER'.format(idade))
else:
    print('Tá maluco, o mulek nem nasceu e vc quer colocar ele para nadar?')
