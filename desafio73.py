
times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Bragantino', 'Fluminense','Athletico-PR', 'Flamengo','Fortaleza','Atlético-MG',
         'São Paulo','Corinthians','Cuiabá','Cruzeiro','Internacional','Vasco','Goiás','Bahia','Santos','América-MG','Coritiba')
print('-=-'*15)
print(f'Lista de times: {times}' )
print('-=-'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*15)
print(f'O Bragantino está na {times.index("Bragantino")+1}ª posição.')
