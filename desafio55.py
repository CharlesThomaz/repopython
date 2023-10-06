npessoas = 0
maiorpeso = 0
menorpeso = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    npessoas = npessoas + 1
    if peso == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print('{} pessoas foram pesadas e o maior peso lido foi de {}Kg e o menor foi de {} Kg'.format(npessoas, maiorpeso, menorpeso))






