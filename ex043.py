import math
altura =  float(input('Digite a sua altura (m): '))
peso = float(input('Digite o seu peso (Kg): '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você foi classificado com: MAGREZA')
elif  imc <= 24.9:
    print('Você foi classificado com: PESO IDEAL')
elif imc <= 29.9:
    print('Você foi classificado com: SOBREPESO')
elif imc <= 39.9:
    print('Você foi classificado com: OBESIDADE')
else: 
    print('Você foi classificado com: OBESIDADE MÓRBIDA')