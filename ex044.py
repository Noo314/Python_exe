print('----------Venda de anões----------')
preço = float(input('Digite qual foi o valor da compra: '))
print('Qual vai ser a forma de pagamento?')
print('[1] Á vista dinheiro/cheque ')
print('[2] Á vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
escolha = int(input('Qual vai ser? '))
if escolha ==  1:
    desconto = preço - (10/100 * preço)
    print ('Sua compra de R${:.2f} irá custar R${:.2f} após o desconto a vista.'.format(preço,desconto))
elif escolha == 2:
    desconto = preço - (5/100 * preço)
    print('Sua compra de R${:.2f} irá custar R${:.2f} após o desconto a prazo.'.format(preço,desconto))
elif escolha == 3:
    print('Sua compra deu R${:.2f}'.format(preço))
elif escolha == 4:
    prazo = int(input('Em quantas vezes? '))
    if prazo >= 3:
        juros = (20/100 * preço)* prazo + preço
        print('Sua compra deu R${:.2f} com juros aplicado.'.format(juros))
    else:
        print('Selecione uma das opções anteriores!')
else:
    print('OPÇÃO INVALIDA!!!')