cores = {'limpa' : '\033[m',
        'azul' : '\033[33m,',
        'vermelho' : '\033[31m'}
z=input('{}Insira algo: '.format(cores['vermelho']))
print('O tipo primitivo é ',type(z))
print('Só a espaço?',z.isspace ())
print('Está em minusculo?',z.islower ())
print('Está em Maiusculo?',z.isupper ())
print('Só é um numero?',z.isnumeric ())
print('É alphanumérico?',z.isalnum ())
print('É capitalizada?',z.title ())
