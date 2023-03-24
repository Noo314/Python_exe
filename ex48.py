s = 0
cont = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        cont += 1
        s += count
print('O somátorio de todos os {} números solicitados foi {}'.format(cont,s))