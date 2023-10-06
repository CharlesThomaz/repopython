palavras = (str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')),
str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')), str(input('Digite uma palavra: ')))

for item in palavras:
    print(f'\nAs  vogais da palavra {item.upper()} são: ' , end ='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end='')
