palavra = (
    'Naruto', 'Sasuke', 'Shino', 'Minato', 'Itachi', 'Kakashi', 'Sakura', 'Obito', 'Neji', 'Zabuza', 'Konan',
    'Zetsu', 'Guy', 'Rock Lee'
)

for i in range(len(palavra)):
    nome = palavra[i]
    print(f"Na palavra {nome.upper()} temos", end= ' ')
    
    for vogais in nome:
        if vogais in 'aeiou':
            print(vogais, end= ' ')
    print()
            