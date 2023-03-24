c = 0
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
while c != 5:
    print('='*20)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('='*20)
    c = int(input('>>>Qual é a sua opção? '))
    if c == 1:
        calc = num_1 + num_2
        print('O resultado entre {} + {} é igual a {}'.format(num_1,num_2,calc))
    if c == 2:
        calc = num_1 * num_2
        print('O resultado entre {} x {} é igual a {}'.format(num_1,num_2,calc))
    if c == 3:
        if num_1 > num_2:
            maior = num_1
        if num_2 > num_1:
            maior = num_2
    print('Entre {} e {} o maior é {}'.format(num_1,num_2,maior))
    if c == 4:
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o segundo número: '))
    elif c < 1 or c > 5:
        c = int(input('Opção invalida por favor digite novamente: '))
