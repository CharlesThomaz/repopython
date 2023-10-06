"""dados =[]
pessoas = []
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas.append(dados[:])
print (pessoas[0])
"""
teste = []
galera = []

while True:
    teste.append(str(input('Digite seu nome: ')))
    teste.append(int(input('Digite sua idade: ')))
    galera.append(teste[:])
    teste.clear()

    continuar = str(input('Continuar: [s/n]'))
    if continuar == 'n':
        break


print(teste)

print(galera)



