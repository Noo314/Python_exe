calc =  int(input('Qual número você quer saber a tabuada?'))
print('-=-'*5)
for c in range(0,11):
    print('{} x {} = {}'.format(c,calc,c*calc))
print('-=-'*5)