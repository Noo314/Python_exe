r = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while r != 'M' and r != 'F':
    r = str(input('Dados invalidos, por favor insira novamente: ')).upper()
if r == 'M':
    print('Sexo salvo com sucesse seu sexo é MASCULINO')
if r == 'F':
    print('Sexo salvo com sucesso seu sexo é FEMININO')