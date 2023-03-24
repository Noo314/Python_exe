frase = str(input('Digite uma Frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
invertido = ''
for letra in range (len(junto) - 1 , -1 , -1):
    invertido += junto[letra]
print('Você digitou {} e o inverso é {}.'.format(junto,invertido))
if junto == invertido:
    print('Você digitou um palindromo!!!')
else:
    print('Você não digitou um palindromo!!!')