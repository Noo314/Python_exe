mcont = fidade = mdezoito = 0
sexo = ' '
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MFmf':
        sexo = str(input('Sexo: [M/F] '))
    
    print('-'*20)
    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if idade >= 18:
        mdezoito += 1
    if sexo in 'Ff' and idade < 20:
        fidade += 1
    if sexo in 'Mm':
        mcont += 1
    if escolha in 'Nn':
        break
print(f'Total de pessoas com maiores de 18 anos: {mdezoito}\nAo todo temos {mcont} homens cadastrados\n e temos {fidade} mulher com menos de 20 anos')