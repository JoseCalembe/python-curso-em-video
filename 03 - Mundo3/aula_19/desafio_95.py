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

    if n<0 or n>len(jogadores):
        if n!=99:
           print("Erro! nao existe jogador com o codigo {}! Tente novamente".format(n))
    elif n>=0 and n<=len(jogadores):
         print(f'LEVANTAMENTO DO JOGADOR {jogadores[n]["Nome"]}')
         for partidas, golos in enumerate(jogadores[n]['Gols']):
             print(f'No jogo {partidas+1} fez {golos} gols')
    if n==99:
            break
print("<<<ENCERRADO>>>")





