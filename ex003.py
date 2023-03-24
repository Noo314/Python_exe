cores = {'limpa' : '\033[m',
        'amarelo' : '\033[33m',
        'azul' : '\033[34m',
        'verde' : '\033[32m'}
n1=int(input('{}Digite o primeiro numero: '.format(cores['azul'])))
n2=int(input('{}Digite o segundo numero: '.format(cores['amarelo'])))
soma=n1+n2
print('{}O resultado é {}'.format(cores['verde'],soma))