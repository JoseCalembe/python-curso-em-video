from random import randint
tem=dict()
tem["jogador 1"]=(randint(1,6))
tem["jogador 2"]=(randint(1,6))
tem["jogador 3"]=(randint(1,6))
tem["jogador 4"]=(randint(1,6))
for k, v in tem.items():
    print(f'{k} tirou {v}')
print('-='*12)
ordenado = sorted(tem.items(), key=lambda item: item[1], reverse=True)

print('Ranking dos jogadores:')

for pos, jogador in enumerate(ordenado):
    print(f'{pos + 1}º lugar: {jogador[0]} com {jogador[1]}')
