#Um algoritmo que leia o sucessor e o antecessor
cores = {'verde' : '\033[32m',
        'roxo' : '\033[35m'}
num = int(input('{}Digite um numero: '.format(cores['verde'])))
ant = num-1
suc = num+1
print('{}O sucessor é {} e o antecessor é {}'.format(cores['roxo'],suc,ant))