from time import sleep
n = int(input('Digite um número para saber sua tabuada: '))
for c in range(1, 11):
    sleep(0.5)
    print('{} x {} = {}'.format(n, c, n*c))
