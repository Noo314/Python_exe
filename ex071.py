print('='*25)
print('BANCO CV'.center(23,' '))
print('='*25)
valor = int(input('Qual o valor vc quer sacar? '))
total = valor
totcéd = 0
céd = 50
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de cédulas {totcéd} de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*25)
print('Volte sempre ao BANCO CV! Tenha um bom dia!')