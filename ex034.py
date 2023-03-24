salário = float(input('Qual é o seu salário? '))
if salário >= 1250:
    aumento = (10/100 * salário) + salário
else:
    aumento = (15/100 * salário) + salário
print('Você recebeu um aumento! seu salário atual é de R${:.2f}'.format(aumento))