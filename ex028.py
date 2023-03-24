import random
from time import sleep
npc = random.randint(1,5)
cores = {'limpa' : '\033[m',
 'amarelo' : '\033[33m',
  'azul' : '\033[34m',
   'verde' : '\033[32m',
    'vermelho' : '\033[31m',
    'lilas' : '\033[35m'}
print('{}-=-{}'.format(cores['azul'],cores['limpa'])*16)
print('{}Vou pensar em um numero de 1 a 5. Tente advinhar{}'.format(cores['amarelo'], cores['limpa']))
print('{}-=-{}'.format(cores['azul'], cores['limpa'])*16)
num = int(input('Tente: '))
print('{}PROCESSANDO...{}'.format(cores['lilas'], cores['limpa']))
sleep(3)
if num == npc:
    print('{}Acertouuuuuuu!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Errouuuu!{}'.format(cores['vermelho'], cores['limpa']))
    print('{}O numero era {}'.format(cores['vermelho'],npc))