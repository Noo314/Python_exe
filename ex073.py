print('-='*40)
times = ('Botafogo - RJ', 'Athletico Paranaense - PR', 'Atlético Mineiro - MG', 'Bahia - BA',
         'América Fc Saf - MG', 'Corinthians - SP', 'Coritiba - PR', 'Cruzeiro Saf - MG', 'Cuiabá Saf - MT', 
         'Flamengo - RJ',  'Fluminense - RJ', 'Fortaleza - CE', 'Goiás - GO', 'Grêmio - RS', 'Internacional - RS'
         'Palmeiras - SP', 'Red Bull Bragantino - SP', 'Santos - SP', 'São Paulo - SP' ,'Vasco da Gama S.a.f. - RJ')
print('-='*35)
print(f'Lista de times no brasileirão: {times}')
print('-='*35)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*35)
print(f'Os últimos 4 são: {times[-4:]}')
print('-='*35)
print(f'Times em ordem alfabética{sorted(times)}')
print('-='*35)
print(f'Fortaleza está em {times.index("Fortaleza - CE")+1}º posição')