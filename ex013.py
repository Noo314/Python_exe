func = float(input('Digite seu salário: '))
desc = func*15/100
st = func+desc
print('Você recebeu um aumento de 15% \nagora seu salario é: R${:.2f}'.format(st))