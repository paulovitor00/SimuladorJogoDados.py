import random
from time import sleep
from operator import itemgetter
jogo = {}
ranking = {}
listprinc = []
cont = 1
for i in range(0, 4):
    a = f'jogador {cont}'
    jogo[a] = f'pontos: {random.randint(1,6)}'
    cont += 1
    listprinc.append(jogo.copy())
for k, e in jogo.items():
    print(f'O {k} tirou: {e}')
    sleep(1)
print('=-'* 30)
print('O ranking dos jogadores foi: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com: {v[1]} pontos.')
    sleep(1)






