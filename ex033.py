a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))
c = int (input('Terceiro numero:'))
#Verificando o Menor
menor = a
if c < a and c < b:
    menor = c
if b < a and b < c:
    menor = b
#Verificando o Maior
maior = a 
if c > a and c > b:
    maior = c
if b > a and b > c:
    maior = b
print('o maior numero é {}\ne o menor é {}'.format(maior,menor))