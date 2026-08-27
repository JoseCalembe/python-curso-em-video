jogadores=list()
total = 0
atleta=dict()
while True:
    gols = []

    total=0
    atleta['Nome'] = input("Nome do jogador:")
    atleta['Partida'] = int(input(f'Quantas partidas o {atleta["Nome"]} jogou?'))
    for c in range(1,atleta['Partida']+1):
        gols.append(int(input(f'Quantos gols na {c} partida?')))
    atleta['Gols'] = gols
    atleta['Total'] = sum(gols)
    jogadores.append(atleta.copy())
    gols.clear()
    resp=str(input("Quer continuar? [S/N]")).upper().strip()[0]
    while resp not in 'SN':
        resp=str(input("Quer continuar? [S/N]")).upper().strip()
    if resp=='N':
       break
print('COD NOME GOLS TOTAL')





