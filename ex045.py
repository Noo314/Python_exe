import random
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)
print("""Escolha uma opção
[0] PEDRA
[1] PAPEL
[2] TESOURA""") 
jogada = int(input('Qual va ser a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=-'*11)
print("""O computador jogou {}
e você jogou {}""".format(itens[computador],itens[jogada]))
print('-=-'*11)
if computador == 0: #Papel
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('O JOGADOR VENCEU!')
    elif jogada == 2:
        print('A MAQUINA VENCEU!')
    else:
        print('OPÇÃO INVALIDA!!!')
elif computador == 1: #Pedra
    if jogada == 0:
        print('O JOGADOR VENCEU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('A MAQUINA VENCEU')
    else:
        print('OPÇÃO INVALIDA!!!')
elif computador == 2: #Tesoura
    if jogada == 0:
        print('A MAQUINA VENCEU!')
    elif jogada == 1:
        print('O JOGADOR VENCEU!')
    elif jogada == 2:
        print('EMPATE!')
    else: 
        ('OPÇÃO INVALIDA!!!')
