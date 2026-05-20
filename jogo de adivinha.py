#Jogo de adivinhação

import random 
n = random.randint (1, 5)

while True:
    jogador = int(input('digite um numero de 1 a 5: '))

    if jogador == n:
        print ('parabens, voce acertou o numero')
        break
    else:
        print ('voce errou o numero, tente novamente')
        print ('tente novamente')