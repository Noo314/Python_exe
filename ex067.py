while True:
    num = int(input('Qual tabuada vôce gostaria de ver? '))
    cont = 0
    
    if num < 0:
        break
    print('-='*10)
    for c in range (1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-='*10)
print('PROGRAMA TABUADA 3.0 ENCERRADA. Volte sempre!')
        