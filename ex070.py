print('-'*25)
print('LOJÃO SUPER BARATÃO'.center(25, ' '))
print('-'*25)
total = cont = mais_1000 = 0
while True:
    cont += 1
    nome_p = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if cont == 1 or preço < menor:
        nome_menor = nome_p
        menor = preço
    if preço > 1000:
        mais_1000 += 1
    choice = ' '
    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] ')).strip()[0]
    if choice in 'Nn':
        break
print('FIM DO PROGRAMA'.center(25,'-'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos no total de {mais_1000} produto maior que R$1000')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}')