escolha = 'S'
cont = 0
soma = 0
while escolha != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if cont == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if escolha != 'S':
        print('Opção inválida!')
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
média = soma / cont
print('Você digitou {} números e a média foi {} \nO maior valor foi {} e o menor foi {}'.format(cont,média,maior,menor))

