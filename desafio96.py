def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de : {a} m2 ')

print('CONTROLE DE TERRENOS')
print('___'*20)
c = float(input('Comprimento: '))
l = float(input('Largura: '))
area(l, c)

