cont = 0
while True:
    n = int(input('Quer saber a tabuada de qual valor?'))
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
    print('___'* 12)


print('___'* 12)
print('FIM')

