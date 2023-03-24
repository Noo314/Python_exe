nome = input('Digite o Nome do aluno: ')
n1 = float(input('Insira a primeira nota do(a) {} '.format(nome)))
n2 =  float(input('Insira a segunda nota do(a) {} '.format(nome)))
md = (n1+n2)/2
print('A média do(a) aluno {} \n é: {}'.format(nome,md))