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
print(f'{"COD":<4}{"NOME":<15}{"GOLS":<14}{"TOTAL"}')
print('-'*40)
for pos,atleta in enumerate(jogadores):
    print(f'{pos:<4}{atleta["Nome"]:<15}{str(atleta["Gols"]):<14}{atleta["Total"]}')
print()
while True:
    print('-'*40)
    n=int(input("Mostrar dados de qual jogador?"))
    if n == 99:
       print("<<<ENCERRADO>>>")

       break

    if n<0 or n>len(jogadores)-1:
           print("Erro! nao existe jogador com o codigo {}! Tente novamente".format(n))
    elif n>=0 and n<=len(jogadores)-1:
         print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[n]["Nome"]}:')
         for partidas, golos in enumerate(jogadores[n]['Gols']):
             print(f'No jogo {partidas+1} fez {golos} gols')





