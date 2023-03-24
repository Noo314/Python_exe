import math
ang = float(input('Digite o angulo: '))
sen = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan =  math.tan(math.radians(ang))
print('O Seno é {:.2f}\nO Coseno é {:.2f}\ne a tangente é {:.2f}'.format(sen,con,tan))