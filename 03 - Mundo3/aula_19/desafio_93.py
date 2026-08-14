jogador=dict()
gols=list()
jogador['Nome']=input("Nome do jogador?")
partidas=int(input(f'Quantas partidas {jogador["Nome"]}  jogou? '))
for c in range(1,partidas+1):
    gols.append(int(input(f'Quantos golos na {c} partidas?')))
jogador['Gols']=gols
jogador['Total']=sum(jogador['Gols'])
print(jogador)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print("="*32)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')
for pos, v in enumerate(jogador['Gols']):
    print(f'=> Na partida {pos+1} fez {v} gols')
print(f'Foi um total de {jogador["Total"]} gols')