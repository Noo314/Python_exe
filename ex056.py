soma_id = 0
maior_id = 0
for c in range (1,5):
    print('-----{}* Pessoa-----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_id += idade
    md_id = soma_id / 2
    if sexo == 'M':
        maior_id = idade
        if idade > maior_id:
            maior_id = idade           
print('A média de idade do grupo é {}'.format(md_id))
print ('o homen mais velho tem {} anos e se chama '.format(maior_id))