nota_1 =  float(input('Digite a primeira nota: '))
nota_2 =  float(input('Digite a segunda: '))
média = (nota_1 + nota_2) / 2
if média > 7: 
    print('Parabéns sua média foi {:.1f} você foi APROVADO!'.format(média))
elif média > 5 and média < 7:
    print('Quase sua méida foi {:.1f} e você está de RECUPERAÇÃO!'.format(média))
else:
    print('Infelizmente sua média foi {:.1f}  e vocÊ está REPROVADO'.format(média))