num = int(input('Digite um numero: '))
print('Escollha uma das bases de conversão')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('O numero {} em binário é {}'.format(num,bin(num) [2:]))
elif escolha == 2:
    print('O numero {} em octal é {}'.format(num,oct(num) [2:]))
elif escolha == 3:
    print('O numero {} em hexadecimal é {}'.format(num,hex(num) [2:]))
else:
    print('Não tem esta opção!')