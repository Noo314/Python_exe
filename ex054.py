from datetime import date
cont_up = 0
cont_down = 0
for c in range (1,8):
    idades = int(input('Digite o ano em que a {}* pessoa nasceu: '.format(c)))
    if date.today().year - idades >= 21:
        cont_up += 1
    else:
        cont_down += 1
print('Ao todo temos {} pessoas maiores de idade \ne {}  menores de idade.'.format(cont_up,cont_down))
