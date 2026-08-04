listagem=('Lapis', 2.20,
          'Borracha', 1.70,
          'Caderno', 5.70,
          'Estojo', 10.60,
          'Transferidor', 4.40,
          'Mochila', 9,
          'Compasso', 8,
          'Canetas', 3,
          'Livro', 7.10,
          'Afialapis', 4)
print("-"*40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print("-"*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print("-"*40)
