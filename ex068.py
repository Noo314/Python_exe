from random import randint
print('-='*18)
print('VAMOS JOGAR ÍMPAR OU PAR')
print('-='*18)
cont = 0
while True:
    valor = int(input('Digite um valor de 0 a 10: '))
    escolha = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    escolha_comp = randint(1,10)
    soma = escolha_comp + valor
    print('-'*36)
    print(f'Você jogou {valor} e o jogou computador {escolha_comp}. O total de {soma} ')
    print('-'*36)
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você venceu!!!')
            print('Vamos de novo...')
            print('-='*18)
            cont +=1
        else:
            print('Você perdeu!!!')
            print('-='*18)
            break
    elif escolha == 'I':
        if soma % 2 == 0:
            print('Você perdeu!!!')
            print('-='*18)
            break
        else:
            print('Você venceu!!!')
            print('Vamos de novo...')
            print('-='*18)
            cont += 1
print(f'GAME OVER você ganhou {cont} vezes!')