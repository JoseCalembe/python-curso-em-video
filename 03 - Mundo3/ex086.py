Lista=('pao', 'Bolacha', 'Arooz', 'Maca','Feijao', 'Frango',
        'Repolho','Cove','Tomate')
for palavra in Lista:
    print(f'As vogais que constam na palavra {palavra} sao:',end="")
    for letra in palavra:
        if letra in "aeiou":
            print(letra,end="")
    print()
