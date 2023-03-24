from time import sleep
print('-=-'*8)
print('Analisador de Triângulos')
print('-=-'*8)
seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o Segundo segmento: '))
seg3 = float(input('Digite o Terceiro segmento:'))
print('Loading...')
sleep(2)
if seg1 < seg2 + seg3 and seg2 < seg1 +seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmento acima NÃO PODEM formar um triãngulo!')