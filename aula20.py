"""def título(txt):
    print('-=-' * 30)
    print(txt)
    print('-=-' * 30)

título('CHARLES')


título('Thomaz')


título('dos Santos')"""

"""def soma(a, b):
    print('___'*5)
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('___'*5)


#Programa principal
soma(4, 5)
soma(2, 1)
soma(8, 9)"""

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
