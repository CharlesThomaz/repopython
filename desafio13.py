sal = int(input('Qual o seu salário atual?R$ '))
porc = sal * (15/100)
newsal = sal + porc
print ('Após reforma salarial vôce passará a receber R${}'.format(newsal))