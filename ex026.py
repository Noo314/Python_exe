frase = str(input('Insira uma frase: ')).strip().lower()
print('a letra A apareceu {} vezes'.format(frase.count('a')))
print('a letra A apareceu primeira vez na posição {}'.format(frase.find('a')+1))
print('a ultima vez que apareceu a letra A foi {}'.format(frase.rfind('a')+1))
