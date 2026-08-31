jogadores=list()
atleta=dict()
gols = list()

while True:

    total=0
    atleta['Nome'] = input("Nome do jogador:")
    atleta['Partida'] = int(input(f'Quantas partidas o {atleta["Nome"]} jogou?'))
    for c in range(1,atleta['Partida']+1):
        gols.append(int(input(f'Quantos gols na {c} partida?')))
    atleta['Gols'] = gols.copy()
    atleta['Total'] = sum(gols)
    jogadores.append(atleta.copy())
    gols.clear()
    resp=str(input("Quer continuar? [S/N]")).upper().strip()[0]
    while resp not in 'SN':
        resp=str(input("Quer continuar? [S/N]")).upper().strip()
    if resp=='N':
       break
print('COD NOME GOLS TOTAL')
for pos,atleta in enumerate(jogadores):
    print(f'{pos}{atleta["Nome"]} {atleta["Gols"]} {atleta["Total"]}')
print()
print('-='*30)
while True:
    n=int(input("Mostrar dados de qual jogador?"))
    if 0<n<=len(jogadores):
        for partidas in (jogadores[n]):
            for golos in partidas:
                print(f'No jogo {partidas} fez {golos} gols')





